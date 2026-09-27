#!/usr/bin/env python3
"""Build the YES (Yindyamarra Environmental Sustainability) unlisted draft site.

Page fragments live in _src/pages/*.html. Each is wrapped in the shared shell (draft ribbon, header,
footer) and written to the repo root, e.g. _src/pages/method.html -> method/index.html.
Links are relative so the site works under any path (GitHub Pages project path now, yes.com.au later).
Run from anywhere:  python3 _src/build.py
"""
import os, re, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_src", "pages")

EMAIL = "contact@yes.com.au"
NAME = "Yindyamarra Environmental Sustainability"

# path, fragment, title, description, nav key
PAGES = [
    ("", "home.html", "YES · Yindyamarra Environmental Sustainability", "Whole-of-council environmental reporting. Enter the raw numbers once; YES calculates the emissions, the rates, the trends and the Yindyamarra Environmental Score.", "home"),
    ("score/", "score.html", "The Yindyamarra Environmental Score · YES", "One monthly score out of 100 across ten categories, with the direction of travel. One of the key reports YES provides for councils.", "score"),
    ("portal/", "portal.html", "Customer portal · YES", "The YES customer portal prototype: monthly data entry, evidence, calculations and reports. Demo data only.", "portal"),
    ("data-dictionary/", "dictionary.html", "Data dictionary · YES", "Every field YES collects and every figure it calculates: definition, unit, frequency, source, mandatory status, calculation and score.", "dictionary"),
    ("method/", "method.html", "Method · YES", "How YES calculates emissions, rates and the Yindyamarra Environmental Score. Factors, editions, formulas and limits.", "method"),
    ("contact/", "contact.html", "Contact · YES", "Everything by email. Offices around Australia.", "contact"),
    ("404.html", "404.html", "Not found · YES", "Page not found.", ""),
]

NAV = [("score/", "The Score", "score"), ("portal/", "Portal", "portal"), ("data-dictionary/", "Data dictionary", "dictionary"), ("method/", "Method", "method"), ("contact/", "Contact", "contact")]

ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'

def rel(depth):
    return "../" * depth if depth else "./"

BASE_PATH = os.environ.get("YES_BASE", "/yes-es-draft/")   # "/" once the site moves to yes.com.au

def shell(path, frag, title, desc, key, body, v):
    depth = 0 if path in ("", "404.html") else path.count("/")
    r = BASE_PATH if path == "404.html" else rel(depth)   # the 404 page is served at any depth, so it links absolutely
    body = body.replace("{{R}}", r).replace("{{ARROW}}", ARROW).replace("{{EMAIL}}", EMAIL).replace("{{NAME}}", NAME)
    nav = "".join('<a href="%s%s"%s>%s</a>' % (r, href, ' aria-current="page"' if k == key else "", label) for href, label, k in NAV)
    app = key == "portal"
    head = f'''<!doctype html>
<html lang="en-AU" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow, noarchive">
<meta name="theme-color" content="#0B0B0B">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800;900&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/yes.css?v={v}">
{('<link rel="stylesheet" href="' + r + 'assets/css/portal.css?v=' + v + '">') if app else ''}
<script>document.documentElement.classList.remove('no-js');</script>
</head>
<body class="page-{key or 'misc'}">
<a class="sr-only" href="#main">Skip to content</a>
<div class="draft" role="note"><div class="wrap"><span class="tag">Unlisted draft</span><span><b>Not for public use.</b> Demo data only. <b>Yindyamarra</b> is a Wiradjuri word: it will not be used at launch without the permission of Wiradjuri language custodians, and the logo is to be designed by an Aboriginal artist.</span></div></div>
'''
    header = f'''<header class="hdr"><div class="wrap">
  <a class="brand" href="{r}" aria-label="YES home"><span class="mark silver">YES</span><span class="full">Yindyamarra<br>Environmental Sustainability</span></a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">MENU</button>
  <nav class="nav" id="nav" aria-label="Main">{nav}<a class="btn btn-silver btn-sm" href="{r}portal/">Customer login</a></nav>
</div></header>
'''
    footer = f'''<footer class="ftr"><div class="wrap">
  <div class="ack"><p class="kicker" style="margin-bottom:10px">Acknowledgement of Country</p><p style="margin:0">YES acknowledges the Traditional Owners of the lands and waters across Australia where we work, and pays respect to Elders past and present. We acknowledge the Wadawurrung People, Traditional Owners of the land where our North Geelong office stands. Sovereignty was never ceded.</p></div>
  <div class="ftr-grid mt-4">
    <div><div class="brand" style="margin-bottom:14px"><span class="mark silver">YES</span><span class="full">Yindyamarra<br>Environmental Sustainability</span></div><p style="max-width:40ch">Monthly environmental reporting for councils, businesses and government. Everything by email.</p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
    <div><h2 class="fh">Reporting</h2><ul><li><a href="{r}score/">The Yindyamarra Environmental Score</a></li><li><a href="{r}portal/">Customer portal</a></li><li><a href="{r}data-dictionary/">Data dictionary</a></li><li><a href="{r}method/">Method</a></li></ul></div>
    <div><h2 class="fh">Offices</h2><ul><li>North Geelong VIC<br><span class="muted">116 Furner Avenue, North Geelong VIC 3215</span></li><li><span class="muted">Other offices to be confirmed</span></li></ul></div>
    <div><h2 class="fh">Contact</h2><ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><span class="muted">No phone line. Every enquiry is answered by email.</span></li><li><a href="{r}contact/">Contact page</a></li></ul></div>
  </div>
  <div class="base"><span>© {datetime.date.today().year} {NAME} · Unlisted draft v0.1</span><span>Scores are self-declared under the published YES method. Not an accredited rating.</span></div>
</div></footer>
'''
    scripts = f'<script src="{r}assets/js/site.js?v={v}"></script>\n'
    extra = ""
    m = re.search(r"<!--SCRIPTS(.*?)-->", body, re.S)
    if m:
        extra = m.group(1).strip().replace("{{R}}", r).replace("{{V}}", v) + "\n"
        body = body.replace(m.group(0), "")
    if app:
        return head + body + scripts + extra + "</body>\n</html>\n"
    return head + header + '<main id="main">\n' + body + "\n</main>\n" + footer + scripts + extra + "</body>\n</html>\n"

def build():
    v = datetime.datetime.now().strftime("%Y%m%d%H%M")
    out = []
    for path, frag, title, desc, key in PAGES:
        fp = os.path.join(SRC, frag)
        if not os.path.exists(fp):
            print("skip (no fragment):", frag); continue
        body = open(fp, encoding="utf-8").read()
        html = shell(path, frag, title, desc, key, body, v)
        dest = os.path.join(ROOT, path, "index.html") if path.endswith("/") or path == "" else os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8").write(html)
        out.append(path or "/")
    open(os.path.join(ROOT, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
    open(os.path.join(ROOT, ".nojekyll"), "w").write("")
    print("built", len(out), "pages:", ", ".join(out))

if __name__ == "__main__":
    build()
