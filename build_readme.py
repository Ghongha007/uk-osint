#!/usr/bin/env python3
"""Builds README.md from research/entries.json so the list and its 'checked' dates never drift apart.
Usage: python3 build_readme.py            (run from this folder)"""
import json, os, re, sys
from collections import Counter, OrderedDict
H = os.path.dirname(os.path.abspath(__file__))
E = json.load(open(os.path.join(H, "research", "entries.json"), encoding="utf-8"))
ORDER = [l.strip() for l in open(os.path.join(H, "categories.txt"), encoding="utf-8") if l.strip()]
ACCESS = {"open": "Open", "free login": "Free login", "captcha": "Captcha", "paid": "Paid", "partly paid": "Partly paid"}
def cell(s):
    return re.sub(r"\s+", " ", str(s or "")).replace("|", "\\|").strip()
def anchor(s):
    return re.sub(r"[^a-z0-9 -]", "", s.lower()).replace(" ", "-")
cats = OrderedDict()
for e in E:
    cats.setdefault(e["category"], []).append(e)
names = [c for c in ORDER if c in cats] + [c for c in cats if c not in ORDER]
missing = [c for c in cats if c not in ORDER]
if missing:
    print("warning: categories not in categories.txt:", missing, file=sys.stderr)
checked = max(e.get("checked", "") for e in E)
st = Counter(e.get("status", "ok") for e in E)
head = open(os.path.join(H, "HEADER.md"), encoding="utf-8").read()
head = (head.replace("{N}", str(len(E))).replace("{CHECKED}", checked).replace("{OK}", str(st["ok"] + st["changed"]))
            .replace("{UNREACHABLE}", str(st["unreachable"])))
out = [head.rstrip(), "", "## Contents", ""]
out += [f"- [{c}](#{anchor(c)}) ({len(cats[c])})" for c in names]
for c in names:
    out += ["", f"## {c}", "", "| Source | What you can find | Access | Run by | Checked |", "|---|---|---|---|---|"]
    for e in sorted(cats[c], key=lambda e: e["name"].lower()):
        what = cell(e["what"])
        if e.get("note"):
            what += f" *{cell(e['note'])}*"
        mark = e.get("checked", "")
        if e.get("status") == "unreachable":
            mark += " (not reachable from our checker)"
        out.append(f"| [{cell(e['name'])}]({e['url'].strip()}) | {what} | {ACCESS.get(e.get('access'), cell(e.get('access')))} | {cell(e.get('run_by'))} | {mark} |")
out += ["", open(os.path.join(H, "FOOTER.md"), encoding="utf-8").read().rstrip(), ""]
open(os.path.join(H, "README.md"), "w", encoding="utf-8").write("\n".join(out))
print(len(E), "entries,", len(names), "categories; status", dict(st))
