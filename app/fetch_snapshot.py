#!/usr/bin/env python3
"""
fetch_snapshot.py - saves an untouched copy of what NASA's PSI repository says
about its Combustion Science investigations, so every number we later show
can be traced to a file in app/raw/.

It only downloads. It does not clean, convert or interpret anything.

What it saves in app/raw/:
  search.json                 the PSI search result for "combustion"
  PSI-<n>.json                one metadata record per investigation
  PSI-<n>_table_<k>.csv       each Experimental Table, byte for byte
  manifest.json               for every file: source URL, time, size, SHA-256

Run from the app/ folder:   py fetch_snapshot.py
Files already in raw/ are not downloaded again; delete raw/ to refresh.
Raw data files (videos, hundreds of GB) are never touched.

Source: https://psi.nasa.gov/physci/repo/search?q=combustion
This script was written with AI assistance (Claude Code, Anthropic).
"""
import hashlib, json, os, sys, time, urllib.parse, urllib.request

BASE = "https://psi.nasa.gov/geode-py/ws"
SEARCH = (BASE + "/repo/search?term=combustion&source=psi&type=investigation"
          "&sort=Public%20Release%20Date&order=desc&size=50")
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw")
AGENT = "SpaceApps2026-DataBeyondSpace/1.0"
AREA = "Combustion Science"


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": AGENT, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def download(url, name, manifest, signed=False):
    """Save url to raw/name unless it is already there. Returns the bytes.

    signed=True: PSI answers with a temporary download link instead of the file,
    so we follow it. Only the stable PSI url is written to the manifest; the
    temporary link holds short-lived access keys and is never saved.
    """
    path = os.path.join(RAW, name)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f.read()
    data = get(url)
    if signed:
        link = data.decode("utf-8").strip().strip('"')
        if not link.startswith("https://"):
            raise ValueError("expected a download link, got: " + link[:80])
        data = get(link)
    with open(path, "wb") as f:
        f.write(data)
    manifest[name] = {"url": url, "retrieved": now(), "bytes": len(data),
                      "sha256": hashlib.sha256(data).hexdigest()}
    time.sleep(0.5)  # be polite to NASA's server
    return data


def main():
    os.makedirs(RAW, exist_ok=True)
    manifest_path = os.path.join(RAW, "manifest.json")
    manifest = {}
    if os.path.exists(manifest_path):
        with open(manifest_path, encoding="utf-8") as f:
            manifest = json.load(f)

    search = json.loads(download(SEARCH, "search.json", manifest))
    hits = search["hits"]["hits"]
    total = search["hits"]["total"]
    print(f"search: {len(hits)} of {total} hits returned")
    if len(hits) != total:
        print("  WARNING: the search did not return every hit", file=sys.stderr)

    kept = 0
    for h in hits:
        acc, area = h["_source"]["Accession"], h["_source"].get("Research Area")
        if area != AREA:
            print(f"  {acc:8} skipped (research area: {area})")
            continue
        kept += 1
        rec = json.loads(download(f"{BASE}/repo/investigations/{acc}", f"{acc}.json", manifest))
        tables = rec.get("experimentalTable") or []
        for k, t in enumerate(tables, 1):
            url = (f"{BASE}/studies/{acc}/download?file={urllib.parse.quote(t['file_name'])}"
                   f"&version={t.get('version', 1)}&redirect=false")
            try:
                data = download(url, f"{acc}_table_{k}.csv", manifest, signed=True)
                manifest.get(f"{acc}_table_{k}.csv", {}).setdefault("psi_file_name", t["file_name"])
                note = f"{len(data)} bytes"
            except Exception as e:
                note = f"FAILED: {e}"
            print(f"  {acc:8} table {k}: {t['file_name']} ({note})")
        if not tables:
            print(f"  {acc:8} no experimental table")

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, sort_keys=True)
    print(f"{kept} {AREA} investigations saved in {RAW}")


if __name__ == "__main__":
    main()
