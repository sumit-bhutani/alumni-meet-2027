#!/usr/bin/env python3
"""Generates pamphlet.html from the sponsorship data below. Then render:
   Chrome --headless=new --no-pdf-header-footer --print-to-pdf=pamphlet.pdf file://$PWD/pamphlet.html"""
import html

PREMIER = [
  ("Grand Patron", "$15,000+", [
    "Event naming: “[Company / Individual] DCE DIT 2027 World Alumni Event”",
    "Exclusive presenting sponsor recognition",
    "Premier logo placement across event materials, entrance and at the buffet tables",
    "Premium stage and backdrop branding",
    "Opportunity to introduce a keynote speaker, subject to approval",
    "Special recognition at the gala",
    "10 complimentary event passes",
    "Dedicated sponsor spotlight on the event website and social media",
    "Recognition in post-event highlights"]),
  ("Diamond Partner", "$10,000", [
    "Event naming: “[Company / Individual] DCE DIT 2027 Grand Gala World Alumni Event”",
    "Premier logo placement on promotional materials",
    "Prominent stage and gala recognition, at the entrance and at the buffet tables",
    "6 complimentary event passes",
    "Dedicated sponsor spotlight on the website",
    "Recognition in event video highlights",
    "Recognition by the event host"]),
  ("Platinum Partner", "$5,000", [
    "Event naming: “[Company / Individual] DCE DIT 2027 Friday Welcome World Alumni Event”",
    "Prominent logo on website and event materials",
    "Stage acknowledgment during the event and at the buffet table",
    "5 complimentary event passes",
    "Featured sponsor recognition on social media",
    "Recognition in post-event communications"]),
]
STANDARD = [
  ("Gold Partner", "$4,000", [
    "Logo on website and selected event materials",
    "Recognition by the event host",
    "4 complimentary event passes",
    "Recognition in sponsor appreciation communications"]),
  ("Silver Partner", "$2,000", [
    "Logo on the official event website",
    "Recognition during the event",
    "2 complimentary event passes",
    "Inclusion in sponsor appreciation communications"]),
  ("Friends of DCE/DIT", "$500+", [
    "Name recognition on the event website",
    "Collective acknowledgment during the event",
    "Inclusion in sponsor appreciation communications"]),
]
MEALS = [
  ("Friday Welcome Reception Partner", "$1,500", "Dhamaal", [
    "Recognition as Friday Welcome Reception Sponsor",
    "Logo on reception signage and at the buffet table",
    "Recognition by the event host",
    "Logo on website and agenda",
    "1 complimentary event pass"]),
  ("Saturday Networking Lunch Partner", "$1,500", "", [
    "Recognition as Saturday Lunch Sponsor",
    "Logo on lunch signage and at the buffet table",
    "Recognition during the lunch program",
    "Logo on event website and agenda",
    "1 complimentary event pass"]),
  ("Saturday Grand Gala Dinner Partner", "$3,000", "Jalwa", [
    "Premier recognition as Gala Dinner Sponsor",
    "Logo on gala signage and screens",
    "Special acknowledgment during dinner and at the buffet table",
    "Logo on website and event materials",
    "3 complimentary event passes"]),
  ("Sunday Morning Breakfast Partner", "$500", "Chai Pila De", [
    "Recognition as Sunday Morning Breakfast Sponsor",
    "Logo at the event",
    "Recognition during the event",
    "Logo on event website and agenda"]),
]
# Contact numbers are NOT stored in this repo. Put them in sponsorship/contacts.local.json
# (git-ignored): [{"name": "...", "phone": "..."}, ...]. If that file exists the script also builds
# pamphlet-with-contacts.html (git-ignored) for private sharing. The public pamphlet.html never has them.
import json, os
CONTACTS = []
if os.path.exists("contacts.local.json"):
    CONTACTS = [(c["name"], c["phone"]) for c in json.load(open("contacts.local.json"))]
e = html.escape
def ul(items): return "<ul>" + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"


def tier(i, n, a, b, dark=False, compact=False):
    return f'''<article class="tier{" dark" if dark else ""}{" compact" if compact else ""}"><div class="head"><h3>{e(n)}</h3><p class="amt">{e(a)}</p></div>{ul(b)}</article>'''
def meal(n, a, t, b):
    return f'''<article class="meal"><p class="tag">{e(t) if t else "&nbsp;"}</p><h3>{e(n)}</h3><p class="amt">{e(a)}</p>{ul(b)}</article>'''
def contact_block(items):
    if not items:
        return '<div class="contact"><div class="cta">Sponsorship contacts are available from the organizing committee</div></div>'
    cells = "".join(f'<div class="ct"><b>{e(n)}</b><span>{e(p)}</span></div>' for n, p in items)
    return f'<div class="contact"><p class="label">Sponsorship contacts</p><div class="cts">{cells}</div></div>'
TOP = '''<div class="top"><span class="brand">Jashn-e-Yaarana</span><span class="kicker">Sponsorship · Atlanta, Georgia · April 16–18, 2027</span></div>'''
glance = "".join(f'<div class="row"><span>{e(n)}</span><b>{e(a)}</b></div>' for n,a,_ in PREMIER+STANDARD) + "".join(f'<div class="row"><span>{e(n)}</span><b>{e(a)}</b></div>' for n,a,_,_ in MEALS)

doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Jashn-e-Yaarana 2027 Sponsorship</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Hanken+Grotesk:wght@400;500;600;700&display=swap">
<style>
@page {{ size: 8.5in 11in; margin: 0; }}
:root {{ --bg:#faf7f2; --ink:#1d1416; --muted:#6a5b5d; --maroon:#701818; --red:#c4161c; --line:#ddd3c6; --surface:#f1ebe2; }}
* {{ box-sizing: border-box; margin: 0; }}
html, body {{ background: var(--bg); color: var(--ink); font-family: "Hanken Grotesk", system-ui, sans-serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.page {{ width: 8.5in; height: 11in; position: relative; overflow: hidden; page-break-after: always; break-after: page; padding: .55in .65in; display: flex; flex-direction: column; }}
.page:last-child {{ page-break-after: auto; break-after: auto; }}
h1, h2, h3, .amt {{ font-family: "Instrument Serif", serif; font-weight: 400; }}
ul {{ list-style: none; padding: 0; }}
li {{ position: relative; padding-left: 18px; font-size: 15px; line-height: 1.4; margin-bottom: 7px; }}
li::before {{ content: ""; position: absolute; left: 0; top: .55em; width: 6px; height: 6px; border-radius: 50%; background: var(--red); }}
.kicker {{ font-size: 11px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; }}
.label {{ font-size: 12px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; color: var(--red); }}

.cover {{ color: #fbf6ef; background: #130b0c; padding: .7in .75in; justify-content: flex-end; }}
.cover .photo {{ position: absolute; inset: 0; z-index: 0; }}
.cover .photo img {{ width: 100%; height: 100%; object-fit: cover; object-position: 62% 50%; display: block; }}
.cover::after {{ content: ""; position: absolute; inset: 0; background: linear-gradient(180deg, rgba(19,11,12,.45) 0%, rgba(19,11,12,0) 28%, rgba(19,11,12,.55) 50%, rgba(19,11,12,.9) 72%, rgba(19,11,12,.97) 100%); }}
.cover > * {{ position: relative; z-index: 1; }}
.cover .kicker {{ color: rgba(251,246,239,.85); }}
.cover h1 {{ font-size: 88px; line-height: .92; letter-spacing: -.02em; margin-top: 16px; white-space: nowrap; }}
.cover h1 em {{ font-style: italic; }}
.cover .tag {{ font-family: "Instrument Serif", serif; font-style: italic; font-size: 27px; color: rgba(251,246,239,.85); margin-top: 14px; }}
.cover .big {{ font-family: "Instrument Serif", serif; font-size: 54px; line-height: 1; margin-top: 44px; padding-top: 26px; border-top: 1px solid rgba(251,246,239,.35); }}
.cover .meta {{ display: flex; gap: 40px; margin-top: 18px; font-size: 15px; color: rgba(251,246,239,.92); }}
.cover .meta b {{ display: block; font-size: 10.5px; letter-spacing: .18em; text-transform: uppercase; color: rgba(251,246,239,.7); margin-bottom: 2px; }}

.top {{ display: flex; justify-content: space-between; align-items: baseline; padding-bottom: 10px; border-bottom: 1px solid var(--line); margin-bottom: 18px; }}
.top .brand {{ font-family: "Instrument Serif", serif; font-size: 24px; }}
.top .kicker {{ color: var(--muted); font-size: 10.5px; }}
h2 {{ font-size: 42px; line-height: 1.04; margin: 6px 0 16px; }}
.tier {{ border: 1.5px solid var(--line); border-radius: 16px; padding: 20px 26px 14px; margin-bottom: 18px; }}
.tier .head {{ display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px; padding-bottom: 10px; border-bottom: 1px solid var(--line); }}
.tier h3 {{ font-size: 38px; line-height: 1; }}
.amt {{ font-size: 38px; line-height: 1; color: var(--maroon); }}
.tier.dark {{ background: #2a0b0e; color: #fbf6ef; border-color: #2a0b0e; }}
.tier.dark .head {{ border-color: rgba(251,246,239,.25); }}
.tier.dark .amt {{ color: #ffb3a8; }}
.tier.dark li::before {{ background: #ff8a7c; }}
.tier.compact {{ padding: 12px 26px 4px; margin-bottom: 10px; }}
.tier.compact .head {{ margin-bottom: 7px; padding-bottom: 5px; }}
.tier.compact h3, .tier.compact .amt {{ font-size: 32px; }}
.tier.compact li {{ font-size: 14px; margin-bottom: 3px; line-height: 1.35; }}
.grid2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
.meal {{ background: var(--surface); border-radius: 16px; padding: 14px 22px 8px; }}
.meal .tag {{ font-size: 11px; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: var(--red); min-height: 15px; }}
.meal h3 {{ font-size: 28px; line-height: 1.05; margin-top: 3px; }}
.meal .amt {{ font-size: 32px; margin: 4px 0 9px; }}
.meal li {{ font-size: 14.5px; margin-bottom: 5px; line-height: 1.35; }}
.contact {{ margin-top: auto; padding-top: 10px; }}
.cts {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 4px 28px; margin-top: 6px; }}
.ct {{ display: grid; padding: 7px 0 8px; border-bottom: 1px solid var(--line); }}
.ct b {{ font-family: "Instrument Serif", serif; font-weight: 400; font-size: 24px; line-height: 1.1; }}
.ct span {{ font-size: 18px; font-weight: 600; color: var(--maroon); font-variant-numeric: tabular-nums; letter-spacing: .02em; }}
.glance .row {{ display: flex; justify-content: space-between; align-items: baseline; padding: 11px 0; border-bottom: 1px solid var(--line); font-size: 16px; }}
.glance .row:first-child {{ border-top: 1px solid var(--line); }}
.glance .row b {{ font-family: "Instrument Serif", serif; font-weight: 400; font-size: 26px; color: var(--maroon); }}
.cta {{ margin-top: auto; background: var(--surface); border: 1.5px solid var(--line); border-radius: 16px; padding: 22px; text-align: center; font-family: "Instrument Serif", serif; font-size: 34px; }}
</style></head><body>

<section class="page cover">
  <div class="photo"><img src="hero-skyline.jpg" alt=""></div>
  <p class="kicker">DCE / DIT World Alumni Reunion 2027</p>
  <h1>Jashn-e-<em>Yaarana</em></h1>
  <p class="tag">The years change. But the friendship stays forever.</p>
  <p class="big">Sponsorship Opportunities</p>
  <div class="meta"><div><b>When</b>April 16 – 18, 2027</div><div><b>Where</b>Atlanta, Georgia, USA</div></div>
</section>

<section class="page">{TOP}
  <p class="label">Premier sponsorship packages</p>
  <h2>Headline the reunion</h2>
  {tier(0, *PREMIER[0], dark=True)}
  {tier(1, *PREMIER[1])}
</section>

<section class="page">{TOP}
  <p class="label">Premier and partner packages</p>
  <h2>Stand with the community</h2>
  {tier(2, *PREMIER[2], compact=True)}
  {tier(3, *STANDARD[0], compact=True)}
  {tier(4, *STANDARD[1], compact=True)}
  {tier(5, *STANDARD[2], compact=True)}
</section>

<section class="page">{TOP}
  <p class="label">Meal and hospitality sponsorships</p>
  <h2>Host a moment</h2>
  <div class="grid2">{"".join(meal(*m) for m in MEALS)}</div>
  @@CONTACTS@@
</section>

</body></html>'''
open("pamphlet.html", "w").write(doc.replace("@@CONTACTS@@", contact_block([])))
if CONTACTS:
    open("pamphlet-with-contacts.html", "w").write(doc.replace("@@CONTACTS@@", contact_block(CONTACTS)))
print("ok", "(+ private version with contacts)" if CONTACTS else "(public version only)")
