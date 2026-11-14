#!/usr/bin/env python3
"""
evidence_oxygen.py - reads the PSI snapshot in app/raw/ and writes a plain
evidence note about oxygen: which investigations state oxygen values in their
Experimental Table, what those values are, and what kind of oxygen they are.

Rules this script follows:
  * Nothing is fetched from the internet; only app/raw/ is read.
  * Ambient oxygen (the atmosphere around the flame) and burner-flow oxygen
    (oxygen blown out of the burner into a fuel atmosphere) are never mixed.
  * A cell is used as a number only if it IS a plain number, or a list of
    plain numbers separated by ";". Every other cell ("~ 21.5", "3400%",
    "RAMP", blank ...) is printed exactly as PSI wrote it and left out of
    the ranges. Nothing is corrected.
  * Units are not converted, with one marked exception: in the summary,
    mole fractions are multiplied by 100 so they can be read as percent.

Which column means what is declared by hand in COLUMNS below, after reading
each table's header and notes. That declaration is our reading, not PSI's.

Run from the app/ folder:   py evidence_oxygen.py
Output: ../03 Data/Oxygen evidence (generated).md   (do not edit by hand)

This script was written with AI assistance (Claude Code, Anthropic).
"""
import collections, csv, io, json, os, re, time

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
OUT = os.path.join(HERE, "..", "03 Data", "Oxygen evidence (generated).md")
PAGE = "https://psi.nasa.gov/physci/repo/data/investigations/"

# Our own draft labels for "what burns" (from 02 Domain/Investigations overview). Not PSI data.
WHAT_BURNS = {
    "PSI-26": "Solids", "PSI-25": "Solids", "PSI-98": "Solids", "PSI-99": "Solids", "PSI-100": "Solids",
    "PSI-102": "Smoke", "PSI-101": "Smoke", "PSI-47": "Dust",
    "PSI-69": "Liquid droplets", "PSI-68": "Liquid droplets", "PSI-39": "Liquid droplets",
    "PSI-20": "Gas (burner emulating solids and liquids)",
    "PSI-159": "Gas", "PSI-22": "Gas", "PSI-10": "Gas", "PSI-21": "Gas", "PSI-23": "Gas",
    "PSI-107": "Gas", "PSI-106": "Gas",
    "PSI-117": "Ground study (FLEX data)", "PSI-142": "Ground study (FLEX data)",
    "PSI-62": "Ground study (BASS data)", "PSI-60": "Ground study (SPICE data)",
    "PSI-115": "Ground study (SAME data)",
}

# (file, exact column header, kind, unit as PSI states it, why we read it this way)
# kind: ambient_o2 | ambient_o2_after | burner_o2 | pressure
COLUMNS = [
    ("PSI-10_table_1.csv", "XO2 (init)", "ambient_o2", "mole fraction", "Normal flames: fuel leaves the burner into an oxygen atmosphere; value before the test"),
    ("PSI-10_table_1.csv", "XO2 (final)", "ambient_o2_after", "mole fraction", "Same atmosphere after the test"),
    ("PSI-10_table_1.csv", "pinit (atm)", "pressure", "atm", "Chamber pressure before the test"),
    ("PSI-10_table_2.csv", "XO2", "burner_o2", "mole fraction", "Inverse flames: oxygen leaves the burner into a fuel atmosphere (column 'XC2H4 initial')"),
    ("PSI-10_table_2.csv", "pinit (atm)", "pressure", "atm", "Chamber pressure before the test"),
    ("PSI-159_table_1.csv", " XO2 before test", "ambient_o2", "mole fraction", "Normal flames: oxygen atmosphere before the test"),
    ("PSI-159_table_1.csv", "XO2  after test", "ambient_o2_after", "mole fraction", "Same atmosphere after the test"),
    ("PSI-159_table_1.csv", "approx p (bar)", "pressure", "bar", "Approximate chamber pressure"),
    ("PSI-159_table_2.csv", "XO2", "burner_o2", "mole fraction", "Inverse flames: oxygen leaves the burner into a fuel atmosphere (column 'Xf  before test')"),
    ("PSI-159_table_2.csv", "approx p (bar)", "pressure", "bar", "Approximate chamber pressure"),
    ("PSI-20_table_1.csv", "Oxygen Conc (percent)", "ambient_o2", "percent", "Table note: chamber oxygen 'as diluted with nitrogen on a volume basis'; one row per test day, listing the concentrations of tests that ignited"),
    ("PSI-23_table_1.csv", "Atmosphere*", "ambient_o2", "text", "Chamber atmosphere described in words; one row per test day"),
    ("PSI-25_table_1.csv", "Calibrated  initial O2 % by vol ", "ambient_o2", "percent by volume", "Oxygen in the glovebox work volume before the test"),
    ("PSI-25_table_1.csv", "Calibrated final O2 % by vol", "ambient_o2_after", "percent by volume", "Same, after the test"),
    ("PSI-39_table_1.csv", "Oxygen", "ambient_o2", "mole fraction (unit not stated in header)", "Listed beside Nitrogen and Helium, which together sum to 1"),
    ("PSI-39_table_1.csv", "Pressure", "pressure", "text with unit", "Chamber pressure"),
    ("PSI-68_table_1.csv", "Oxygen Mole Fraction", "ambient_o2", "mole fraction", "One row per fuel, listing the planned values; column 'Ambient Gas Mixture'"),
    ("PSI-68_table_1.csv", "Ambient Pressure (atm)", "pressure", "atm", "One row per fuel, listing the planned values"),
    ("PSI-69_table_1.csv", "O initial ambient composition; mole fraction", "ambient_o2", "mole fraction", "Header says initial ambient composition"),
    ("PSI-69_table_1.csv", "Ambient pressure; mmHg", "pressure", "mmHg", "Header says ambient pressure"),
    ("PSI-98_table_1.csv", "Percent O2", "ambient_o2", "percent", "Oxygen in the Cygnus cabin air flowing over the sample"),
    ("PSI-99_table_1.csv", "Percent O2 (Note 1)", "ambient_o2", "percent", "Table note 1: derived from measured CO2 and the initial O2 reported by ISS"),
]

KIND_LABEL = {"ambient_o2": "Ambient oxygen, before test", "ambient_o2_after": "Ambient oxygen, after test",
              "burner_o2": "Burner-flow oxygen", "pressure": "Pressure"}


def read_text(path):
    """PSI tables are UTF-8 except FLEX, which is Windows-1252. Returns (text, encoding)."""
    data = open(path, "rb").read()
    try:
        return data.decode("utf-8-sig"), "UTF-8"
    except UnicodeDecodeError:
        return data.decode("cp1252"), "Windows-1252"


def load_table(name):
    text, enc = read_text(os.path.join(RAW, name))
    rows = list(csv.reader(io.StringIO(text)))
    blank = sum(1 for r in rows[1:] if not any(c.strip() for c in r))
    body = [r for r in rows[1:] if any(c.strip() for c in r)]
    return rows[0], body, blank, enc


def plain(cell):
    """float if the cell is exactly a plain number, else None."""
    return float(cell) if re.fullmatch(r"\d+(\.\d+)?|\.\d+", cell.strip()) else None


def read_cell(cell):
    """('number', [x]) | ('list', [x, y, ...]) | ('blank', []) | ('other', [])"""
    s = cell.strip()
    if not s:
        return "blank", []
    if plain(s) is not None:
        return "number", [plain(s)]
    parts = [p.strip() for p in s.split(";")]
    if len(parts) > 1 and all(plain(p) is not None for p in parts):
        return "list", [plain(p) for p in parts]
    return "other", []


def fmt(x):
    return f"{x:.4g}"


def md(s):
    """Show a cell exactly, safely inside a markdown table."""
    return "`" + s.replace("|", "\\|").replace("`", "'") + "`"


def analyse(name, column):
    header, body, _, _ = load_table(name)
    i = header.index(column)
    cells = [r[i] if i < len(r) else "" for r in body]
    res = {"rows": len(cells), "number": [], "list": [], "list_cells": collections.Counter(),
           "blank": 0, "other": collections.Counter()}
    for c in cells:
        kind, vals = read_cell(c)
        if kind == "number":
            res["number"] += vals
        elif kind == "list":
            res["list"] += vals
            res["list_cells"][c] += 1
        elif kind == "blank":
            res["blank"] += 1
        else:
            res["other"][c] += 1
    return res


def main():
    L = []
    w = L.append
    manifest = json.load(open(os.path.join(RAW, "manifest.json"), encoding="utf-8"))
    recs = {}
    for f in os.listdir(RAW):
        if re.fullmatch(r"PSI-\d+\.json", f):
            j = json.load(open(os.path.join(RAW, f), encoding="utf-8"))
            recs[j["accession"]] = j
    order = sorted(recs, key=lambda a: int(a.split("-")[1]))
    tables = sorted((f for f in os.listdir(RAW) if "_table_" in f),
                    key=lambda f: (int(re.search(r"PSI-(\d+)", f).group(1)), f))
    declared = collections.defaultdict(list)
    for c in COLUMNS:
        declared[c[0]].append(c)
    retrieved = sorted(v["retrieved"] for v in manifest.values())

    w("# Oxygen evidence (generated)")
    w("")
    w(f"Written by `app/evidence_oxygen.py` from the snapshot in `app/raw/` "
      f"(PSI files retrieved {retrieved[0]} to {retrieved[-1]}). **Do not edit by hand**; re-run the script.")
    w("")
    w("How to read it:")
    w("- **Ambient oxygen** is the atmosphere around the flame. **Burner-flow oxygen** is oxygen blown out of the burner into a fuel atmosphere (\"inverse\" flames). They are different things and are kept apart.")
    w("- A cell counts as a number only if it is a plain number, or a `;`-separated list of plain numbers. Every other cell is shown exactly as PSI wrote it and is **not** in the ranges.")
    w("- † = mole fraction multiplied by 100 to read as percent. No other conversion is made.")
    w("- \"What burns\" is our own draft label, not a PSI field. \"Rows\" are table rows; in some tables a row is a test day or a fuel, not one test.")
    w("- Which column means what is our reading of each table (section 4).")
    w("")

    # ---------- 1. summary ----------
    w("## 1. Summary: oxygen stated in each Experimental Table")
    w("")
    w("| PSI id | Investigation | What burns (our label) | Table | Rows | Ambient O2 before test, % | Rows at 30 % or more | Burner-flow O2, % | Other cells, as written |")
    w("|---|---|---|---|---|---|---|---|---|")
    for acc in order:
        j = recs[acc]
        name = j.get("investigationAcronym") or "(no acronym)"
        mine = [t for t in tables if t.startswith(acc + "_")]
        if not mine:
            w(f"| [{acc}]({PAGE}{acc}) | {name} | {WHAT_BURNS.get(acc, '?')} | no table | - | - | - | - | |")
            continue
        for t in mine:
            _, body, _, _ = load_table(t)
            label = manifest[t]["psi_file_name"].split("Experimental table_")[-1].replace(".csv", "")
            amb = bur = hi = "not in table"
            other = []
            for (_, col, kind, unit, _) in declared.get(t, []):
                if kind not in ("ambient_o2", "burner_o2"):
                    continue
                r = analyse(t, col)
                scale = 100 if unit.startswith("mole fraction") else 1
                mark = "†" if scale == 100 else ""
                vals = [v * scale for v in r["number"] + r["list"]]
                txt = f"{fmt(min(vals))} to {fmt(max(vals))}{mark}" if vals else "no plain numbers"
                if r["list"]:
                    txt += " (from list cells)"
                if kind == "ambient_o2":
                    amb = txt
                    n_num = sum(1 for v in r["number"] if v * scale >= 30)
                    n_list = sum(n for c, n in r["list_cells"].items()
                                 if any(v * scale >= 30 for v in read_cell(c)[1]))
                    hi = f"{n_num} of {len(r['number'])} numeric rows" if r["number"] else ""
                    if r["list_cells"]:
                        hi += f"{n_list} of {sum(r['list_cells'].values())} list rows"
                    hi = hi or "see cells"
                else:
                    bur = txt
                other += [f"{md(c)} x{n}" for c, n in r["other"].items()]
                if r["blank"]:
                    other.append(f"blank x{r['blank']}")
            w(f"| [{acc}]({PAGE}{acc}) | {name} | {WHAT_BURNS.get(acc, '?')} | {label} | {len(body)} | {amb} | {hi if amb != 'not in table' else '-'} | {bur} | {'; '.join(other)} |")
    w("")

    # ---------- 2. per column detail ----------
    w("## 2. Every oxygen and pressure column, in detail")
    w("")
    w("Units are as PSI states them (no conversion here). \"Lowest / highest\" lists the three smallest and three largest distinct numbers so unusual values stay visible.")
    w("")
    w("| Table file | Column header | Our reading | Unit as stated | Rows | Plain numbers | Lowest | Highest | List cells | Blank | Other cells, as written |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for (t, col, kind, unit, _) in COLUMNS:
        r = analyse(t, col)
        d = sorted(set(r["number"]))
        lo = ", ".join(fmt(x) for x in d[:3]) or "-"
        hi = ", ".join(fmt(x) for x in d[-3:]) or "-"
        lists = "; ".join(f"{md(c)} x{n}" for c, n in r["list_cells"].items()) or "-"
        other = "; ".join(f"{md(c)} x{n}" for c, n in r["other"].items()) or "-"
        w(f"| `{t}` | {md(col)} | {KIND_LABEL[kind]} | {unit} | {r['rows']} | {len(r['number'])} | {lo} | {hi} | {lists} | {r['blank']} | {other} |")
    w("")

    # ---------- 3. ambient oxygen levels ----------
    w("## 3. Ambient oxygen before test: how many rows at each level")
    w("")
    w("Plain-number cells only, rounded to the nearest whole percent (†: mole fractions x100). List and text cells are in section 2.")
    w("")
    w("| Table file | Investigation | What burns (our label) | Rows per whole percent (percent: rows) |")
    w("|---|---|---|---|")
    for (t, col, kind, unit, _) in COLUMNS:
        if kind != "ambient_o2":
            continue
        r = analyse(t, col)
        if not r["number"]:
            continue
        scale = 100 if unit.startswith("mole fraction") else 1
        # int(x + 0.5) rounds halves up, so 26.5 shows as 27
        c = collections.Counter(int(v * scale + 0.5) for v in r["number"])
        acc = t.split("_")[0]
        w(f"| `{t}` | {recs[acc].get('investigationAcronym')} | {WHAT_BURNS.get(acc)} | "
          + ", ".join(f"{k}: {c[k]}" for k in sorted(c)) + " |")
    w("")

    # ---------- 4. declarations ----------
    w("## 4. Why each column is read as ambient or burner-flow oxygen")
    w("")
    w("| Table file | Column header | Our reading | Reason |")
    w("|---|---|---|---|")
    for (t, col, kind, _, why) in COLUMNS:
        w(f"| `{t}` | {md(col)} | {KIND_LABEL[kind]} | {why} |")
    w("")

    # ---------- 5. inventory ----------
    w("## 5. All tables in the snapshot, with their full headers")
    w("")
    w("Tables with no oxygen column are listed too, so absence is visible.")
    w("")
    w("| PSI id | Investigation | DOI | Table file | PSI file name | Rows | Blank rows dropped | Encoding | Oxygen column? | Header |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    for acc in order:
        j = recs[acc]
        doi = f"[{j['doi']}](https://doi.org/{j['doi']})" if j.get("doi") else "none"
        mine = [t for t in tables if t.startswith(acc + "_")]
        if not mine:
            w(f"| {acc} | {j.get('investigationAcronym') or '(no acronym)'} | {doi} | no experimental table | | | | | | |")
        for t in mine:
            header, body, blank, enc = load_table(t)
            has = "yes" if any(k in ("ambient_o2", "burner_o2") for (_, _, k, _, _) in declared.get(t, [])) else "no"
            w(f"| {acc} | {j.get('investigationAcronym') or '(no acronym)'} | {doi} | `{t}` | {manifest[t]['psi_file_name']} | {len(body)} | {blank} | {enc} | {has} | "
              + ", ".join(md(h) for h in header) + " |")
    w("")

    # ---------- 6. records ----------
    w("## 6. The 24 investigation records")
    w("")
    w("Straight from each record's fields. Size is `totalFileSize` in bytes divided by 10^9.")
    w("")
    w("| PSI id | Acronym | Title | Project type | Sub-research area | Hardware | Total size, GB | License | DOI |")
    w("|---|---|---|---|---|---|---|---|---|")
    for acc in order:
        j = recs[acc]
        clean = lambda s: re.sub(r"\s+", " ", s or "").strip().replace("|", "/")
        size = j.get("totalFileSize")
        w(f"| [{acc}]({PAGE}{acc}) | {clean(j.get('investigationAcronym')) or '(none)'} | {clean(j.get('title'))} | {clean(j.get('projectType'))} | "
          f"{clean(j.get('subResearchArea')) or '(blank)'} | {clean(j.get('experimentHardware')) or '(blank)'} | "
          f"{(float(size) / 1e9):.2f} | {j.get('licenseIdentifier') or '(blank)'} | {j.get('doi') or 'none'} |")
    w("")

    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L))
    print("wrote", os.path.normpath(OUT))


if __name__ == "__main__":
    main()
