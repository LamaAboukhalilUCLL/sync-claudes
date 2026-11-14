#!/usr/bin/env python3
"""
build_catalogue.py - builds the Flame in Freefall investigation catalogue from
NASA's Physical Sciences Informatics (PSI) repository.

Source: https://psi.nasa.gov/physci/repo/search?q=combustion
Output: catalogue.json and catalogue.js (same data, loadable by index.html)

Standard library only:  python build_catalogue.py
Raw API responses are cached in ./raw so re-runs do not hit NASA again.

Parts of this script were written with AI assistance (Claude); see README / SI disclosure.
"""
import csv, io, json, os, re, sys, time, urllib.parse, urllib.request

BASE = "https://psi.nasa.gov/geode-py/ws"
SEARCH = BASE + "/repo/search?term=combustion&source=psi&type=investigation&sort=Public%20Release%20Date&order=desc"
PAGE = "https://psi.nasa.gov/physci/repo/data/investigations/"
RAW = "raw"

# Combustion Science investigations seen in the PSI search on 14 Nov 2026.
# The live search result is merged with this list, so new entries are picked up too.
KNOWN_IDS = ["PSI-26", "PSI-25", "PSI-98", "PSI-99", "PSI-100", "PSI-102", "PSI-101", "PSI-47",
             "PSI-69", "PSI-68", "PSI-39", "PSI-20", "PSI-159", "PSI-22", "PSI-10", "PSI-21",
             "PSI-23", "PSI-107", "PSI-106", "PSI-117", "PSI-142", "PSI-62", "PSI-60", "PSI-115"]

# Hand curation: what is burning, and which fire-safety pillar the work informs.
# Pillars follow NASA's framing in the challenge statement: prevention, detection, suppression.
# "fundamental" = combustion science that supports fire safety less directly; "modeling" = ground study reusing flight data.
CURATED = {
    "PSI-26":  dict(short="BASS",        phase="solid",  pillars=["prevention", "suppression"]),
    "PSI-25":  dict(short="BASS-II",     phase="solid",  pillars=["prevention"]),
    "PSI-98":  dict(short="Saffire-I",   phase="solid",  pillars=["prevention"]),
    "PSI-99":  dict(short="Saffire-II",  phase="solid",  pillars=["prevention"]),
    "PSI-100": dict(short="Saffire-III", phase="solid",  pillars=["prevention"]),
    "PSI-102": dict(short="SAME",        phase="smoke",  pillars=["detection"]),
    "PSI-101": dict(short="SAME-R",      phase="smoke",  pillars=["detection"]),
    "PSI-47":  dict(short="DAFT / DAFT-2", phase="smoke", pillars=["detection"]),
    "PSI-69":  dict(short="FLEX",        phase="liquid", pillars=["suppression", "prevention"]),
    "PSI-68":  dict(short="FLEX-2",      phase="liquid", pillars=["suppression"]),
    "PSI-39":  dict(short="CFI",         phase="liquid", pillars=["fundamental"]),
    "PSI-20":  dict(short="ACME BRE",    phase="gas",    pillars=["prevention"]),
    "PSI-159": dict(short="ACME CFI-G",  phase="gas",    pillars=["fundamental"]),
    "PSI-22":  dict(short="ACME E-FIELD Flames", phase="gas", pillars=["fundamental"]),
    "PSI-10":  dict(short="ACME Flame Design",   phase="gas", pillars=["fundamental"]),
    "PSI-21":  dict(short="ACME CLD Flame",      phase="gas", pillars=["fundamental"]),
    "PSI-23":  dict(short="ACME s-Flame",        phase="gas", pillars=["fundamental"]),
    "PSI-107": dict(short="SPICE",       phase="gas",    pillars=["fundamental"]),
    "PSI-106": dict(short="SLICE",       phase="gas",    pillars=["fundamental"]),
    "PSI-117": dict(short="Cool-flame CFD (FLEX data)",        phase="liquid", pillars=["modeling"]),
    "PSI-142": dict(short="Cool-flame transitions (FLEX data)", phase="liquid", pillars=["modeling"]),
    "PSI-62":  dict(short="Flame-spread modeling (BASS data)",  phase="solid",  pillars=["modeling", "prevention"]),
    "PSI-60":  dict(short="SPICE data analysis",                phase="gas",    pillars=["modeling"]),
    "PSI-115": dict(short="Smoke simulation (SAME data)",       phase="smoke",  pillars=["modeling", "detection"]),
}


def get(url, cache_name):
    """GET with on-disk cache. Returns text."""
    os.makedirs(RAW, exist_ok=True)
    path = os.path.join(RAW, cache_name)
    if os.path.exists(path):
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    req = urllib.request.Request(url, headers={"User-Agent": "SpaceApps2026-DataBeyondSpace/1.0", "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=60) as r:
        text = r.read().decode("utf-8", errors="replace")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    time.sleep(0.4)  # be polite to NASA's server
    return text


def clean(s):
    return re.sub(r"\s+", " ", s or "").strip()


# ---------- experimental-table parsing ----------

NUM = re.compile(r"(?<![A-Za-z\d.])\d+(?:\.\d+)?|(?<![A-Za-z\d])\.\d+")

def numbers(cell):
    """All plain numbers in a cell: '0.17; 0.21;0.25' -> [0.17, 0.21, 0.25]; '~30% and ~21% O2' -> [30, 21]."""
    cell = re.sub(r"[OoNn]\s?2|CO2|C\d+H\d+|H2", " ", cell or "")   # drop chemical formulas
    return [float(x) for x in NUM.findall(cell)]

def col_kind(name):
    """Classify a column header. Returns 'o2', 'pressure', 'flow', 'fuel' or None."""
    n = name.lower()
    if re.search(r"final|after|mean|loss|co2|co \(|^co |\bco\b initial|n initial|he initial|nitrogen|helium", n):
        return None
    if re.search(r"\bxo2\b|\bo2\b|oxygen|^o initial|atmosphere", n):
        return "o2"
    if re.search(r"press|^pinit|approx p", n):
        return "pressure"
    if re.search(r"air ?flow|air rate|inlet velocity|flow velocity", n):
        return "flow"
    if re.search(r"fuel sample material|^material|sample material|sample type|^fuel$|fuel type|sample \(fuel|fuel bottle", n):
        return "fuel"
    return None

def to_atm(values, header):
    h = header.lower()
    if "mmhg" in h or "torr" in h:
        return [v / 760.0 for v in values]
    if "bar" in h:
        return [v / 1.01325 for v in values]
    if "psi" in h:
        return [v / 14.696 for v in values]
    return values

def summarise_table(text):
    """Turn one experimental-table CSV into ranges and top fuels."""
    rows = [r for r in csv.reader(io.StringIO(text)) if any(c.strip() for c in r)]
    if len(rows) < 2:
        return None
    header = [clean(h) for h in rows[0]]
    body = rows[1:]
    out = {"n_tests": len(body), "columns": header, "o2_pct": None, "pressure_atm": None,
           "flow_cm_s": None, "fuels": [], "o2_values": []}
    o2, pres, flow, fuels = [], [], [], {}
    for i, name in enumerate(header):
        kind = col_kind(name)
        if not kind:
            continue
        cells = [r[i].strip() for r in body if i < len(r) and r[i].strip()]
        if kind == "fuel":
            for c in cells:
                if re.search(r"pre-test|flow visual", c, re.I):
                    continue
                key = clean(c)[:60]
                fuels[key] = fuels.get(key, 0) + 1
            continue
        vals = [v for c in cells for v in numbers(c)]
        if kind == "o2":
            if vals and max(vals) <= 1.0:          # mole fraction -> percent
                vals = [v * 100 for v in vals]
            o2 += [v for v in vals if 1 <= v <= 100]
        elif kind == "pressure":
            pres += [v for v in to_atm(vals, name) if 0.05 <= v <= 50]
        elif kind == "flow":
            flow += [abs(v) for v in vals if abs(v) <= 500]
    rng = lambda xs: [round(min(xs), 2), round(max(xs), 2)] if xs else None
    out["o2_pct"], out["pressure_atm"], out["flow_cm_s"] = rng(o2), rng(pres), rng(flow)
    out["o2_values"] = sorted({round(v, 1) for v in o2})[:400]
    out["fuels"] = [k for k, _ in sorted(fuels.items(), key=lambda kv: -kv[1])[:10]]
    return out


# ---------- fetching ----------

def search_ids():
    ids = []
    for suffix, name in (("", "search.json"), ("&from=25", "search_p2.json")):
        try:
            data = json.loads(get(SEARCH + suffix, name))
            ids += [h["_source"]["Accession"] for h in data.get("hits", {}).get("hits", [])]
        except Exception as e:  # paging parameter is a guess; the known list covers us
            print("  search", suffix or "page 1", "skipped:", e, file=sys.stderr)
    seen, merged = set(), []
    for i in ids + KNOWN_IDS:
        if i not in seen:
            seen.add(i); merged.append(i)
    return merged

def fetch_table(acc, entry):
    fname, ver = entry["file_name"], entry.get("version", 1)
    url = f"{BASE}/studies/{acc}/download?file={urllib.parse.quote(fname)}&version={ver}&redirect=false"
    text = get(url, f"{acc}_table.csv")
    probe = text.strip().strip('"')
    if probe.startswith("http"):                       # API answered with a signed URL
        os.remove(os.path.join(RAW, f"{acc}_table.csv"))
        text = get(probe, f"{acc}_table.csv")
    elif probe.startswith("{"):                        # or a small JSON holding the URL
        m = re.search(r'https?://[^"\\ ]+', probe)
        if m:
            os.remove(os.path.join(RAW, f"{acc}_table.csv"))
            text = get(m.group(0), f"{acc}_table.csv")
    return text

def build_record(acc):
    j = json.loads(get(f"{BASE}/repo/investigations/{acc}", f"{acc}.json"))
    if j.get("researchArea") != "Combustion Science":
        return None
    cur = CURATED.get(acc, {})
    rec = {
        "id": acc,
        "short": cur.get("short") or j.get("investigationAcronym") or acc,
        "title": clean(j.get("title")),
        "url": PAGE + acc,
        "doi": j.get("doi") or "",
        "doi_url": ("https://doi.org/" + j["doi"]) if j.get("doi") else "",
        "license": j.get("licenseIdentifier") or "",
        "type": j.get("projectType") or "",
        "is_flight": "Microgravity" in (j.get("projectType") or ""),
        "platform": clean(j.get("flightProgram")),
        "sub_area": clean(j.get("subResearchArea")),
        "hardware": clean(j.get("experimentHardware")),
        "start": j.get("investigationStartDate") or "",
        "end": j.get("investigationEndDate") or "",
        "related": [x.strip() for x in (j.get("related_glds") or "").split(",") if x.strip()],
        "size_gb": round((j.get("totalFileSize") or 0) / 1e9, 2),
        "objective": clean(j.get("objective")),
        "approach": clean(j.get("approach")),
        "hypothesis": clean(j.get("hypothesis")),
        "impacts": clean(j.get("researchImpacts")),
        "publications": [{"title": clean(p.get("title")), "doi": p.get("doi") or ""} for p in j.get("publications") or []],
        "phase": cur.get("phase", "unknown"),
        "pillars": cur.get("pillars", ["fundamental"]),
        "curated": acc in CURATED,
        "table": None,
    }
    tables = j.get("experimentalTable") or []
    if tables:
        try:
            rec["table"] = summarise_table(fetch_table(acc, tables[0]))
        except Exception as e:
            print(f"  {acc}: experimental table failed: {e}", file=sys.stderr)
    return rec

def main():
    ids = search_ids()
    print(f"{len(ids)} candidate investigations")
    records = []
    for acc in ids:
        try:
            rec = build_record(acc)
        except Exception as e:
            print(f"  {acc}: FAILED {e}", file=sys.stderr)
            continue
        if rec:
            records.append(rec)
            t = rec["table"] or {}
            print(f"  {acc:8} {rec['short'][:28]:28} tests={t.get('n_tests', '-')!s:4} O2%={t.get('o2_pct')} p_atm={t.get('pressure_atm')} flow={t.get('flow_cm_s')}")
    out = {"source": "NASA Physical Sciences Informatics (PSI), https://psi.nasa.gov/physci/repo",
           "generated": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
           "investigations": records}
    with open("catalogue.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    with open("catalogue.js", "w", encoding="utf-8") as f:
        f.write("window.CATALOGUE = " + json.dumps(out, ensure_ascii=False) + ";\n")
    print(f"wrote catalogue.json and catalogue.js with {len(records)} investigations")

if __name__ == "__main__":
    main()
