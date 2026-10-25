#!/usr/bin/env python3
"""Generates the static pages in ./site from the content below.
Run:  python3 build.py
Edit copy here (or edit the generated HTML directly), shared look lives in site/styles.css."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

# Final facts. Keep consistent on every page.
DATES = "April 16–18, 2027"
VENUE = "Maison 6405"
ADDRESS = "6405 Sugarloaf Parkway, Duluth, GA 30097"
MAPS = "https://www.google.com/maps/search/?api=1&query=Maison%206405%206405%20Sugarloaf%20Parkway%20Duluth%20GA%2030097"
SITE = "Jashn-e-Yaarana"
# Paste the external registration site URL here when it exists. Empty = Register buttons open the
# prices page (register.html), where the registration button stays disabled.
REGISTER_URL = ""
REG = REGISTER_URL or "register.html"
REG_ATTR = ' target="_blank" rel="noopener"' if REGISTER_URL else ""

NAV = [("index.html", "Home"), ("about.html", "About"), ("program.html", "Program"),
       ("speakers.html", "Speakers"), ("venue.html", "Venue"), ("committee.html", "Committee"),
       ("sponsors.html", "Sponsors")]


def nav(active):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a>' for h, t in NAV)
    return f'''<nav class="nav" id="nav" aria-label="Main">
  <div class="wrap">
    <a class="brand" href="index.html">{SITE}</a>
    <div class="links">{links}</div>
    <div class="nav-right">
      <a class="pill" href="{REG}"{REG_ATTR}>Register</a>
      <button class="burger" id="burger" type="button" aria-expanded="false" aria-controls="drawer">Menu</button>
    </div>
  </div>
  <div class="drawer" id="drawer"><div class="wrap">{links}<a href="{REG}"{REG_ATTR} class="drawer-reg">Register</a></div></div>
</nav>'''


CTA = f'''<section class="cta">
  <div class="wrap">
    <div>
      <p class="label">Save your seat</p>
      <h2>Be at the table.</h2>
      <p>{DATES} · {VENUE}, Duluth, Georgia</p>
    </div>
    <a class="btn" href="{REG}"{REG_ATTR}>Register now</a>
  </div>
</section>'''


def footer():
    cols = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f'''<footer>
  <div class="wrap">
    <div><b>{SITE}</b>DCE · DIT · DTU · NSIT · NSUT<br>World Alumni Meet 2027<br>{DATES} · {VENUE}, Duluth, Georgia</div>
    <div class="fcols">{cols}<a href="{REG}"{REG_ATTR} class="freg">Register</a></div>
  </div>
</footer>
<a class="sticky-reg" id="sticky-reg" href="{REG}"{REG_ATTR}>Register · {DATES}</a>'''


def page(slug, title, active, body, head="", desc=""):
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc or "DCE · DIT · DTU · NSIT · NSUT World Alumni Meet, " + DATES + ", " + VENUE + ", Duluth, Georgia."}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Hanken+Grotesk:wght@400;500;600&display=swap">
<link rel="stylesheet" href="styles.css?v=11">
</head>
<body{" class=\"on-register\"" if slug == "register.html" else ""}>
{nav(active)}
{body}
{CTA}
{footer()}
<script src="site.js?v=11"></script>
</body>
</html>
'''
    with open(os.path.join(OUT, slug), "w") as f:
        f.write(html)


def inner_head(img, label, title, intro, pos="50% 50%"):
    return f'''<header class="phead">
  <div class="photo"><img src="images/{img}" alt="" style="object-position:{pos}"></div>
  <div class="wrap">
    <p class="kicker">{label}</p>
    <h1>{title}</h1>
    <p class="intro">{intro}</p>
  </div>
</header>'''


# ---------------------------------------------------------------- Home
home = f'''<header class="hero" id="top">
  <div class="photo"><img src="images/hero-skyline.jpg" alt="Atlanta skyline and Centennial Olympic Park at dusk"></div>
  <div class="wrap">
    <p class="kicker">DCE · DIT · DTU · NSIT · NSUT &nbsp;World Alumni Meet 2027</p>
    <h1>Jashn-e-<br><em>Yaarana</em></h1>
    <p class="tag">The years change. But the friendship stays forever.</p>
    <div class="hero-actions">
      <a class="btn" href="{REG}"{REG_ATTR}>Register now</a>
      <a class="btn ghost" href="program.html">See the program</a>
    </div>
    <div class="hero-bar">
      <div class="hero-facts">
        <div><span>When</span>{DATES}</div>
        <div><span>Where</span>{VENUE}, Duluth · Greater Atlanta</div>
      </div>
      <p class="count"><strong data-countdown>000</strong>days to go</p>
    </div>
  </div>
</header>

<section class="moment">
  <div class="wrap">
    <figure class="wide">
      <img src="images/dc26-gala.jpg" alt="Alumni waving together on a wooden terrace at the 2026 reunion in Washington, D.C." style="object-position:50% 78%">
      <figcaption><span>Last year</span>DC26, Washington, D.C. Alumni at the 2026 reunion.</figcaption>
    </figure>
  </div>
</section>

<section class="evenings" id="evenings">
  <div class="wrap">
    <div class="head">
      <h2>Three days, four moments</h2>
      <p>From Friday evening to Sunday breakfast. <a href="program.html">Full program →</a></p>
    </div>
    <div class="cards">
      <article class="card">
        <img src="images/venue-night.jpg" alt="Maison 6405 lit in purple and gold at night, reflected in the pond">
        <div class="in">
          <p class="date">Fri · April 16 · Evening</p>
          <h3>Dhamaal</h3>
          <p class="mood">Welcome night</p>
          <p class="d">Music, chai and hostel stories. Find your batch and pick up where you left off.</p>
        </div>
      </article>
      <article class="card">
        <img src="images/atlanta-park.jpg" alt="Atlanta towers reflected in Piedmont Park's lake">
        <div class="in">
          <p class="date">Sat · April 17 · Daytime</p>
          <h3>Ek Saath</h3>
          <p class="mood">Leadership Conclave</p>
          <p class="d">Talks, panels and conversations led by alumni, with a mentorship circle and the group photo.</p>
        </div>
      </article>
      <article class="card">
        <img src="images/venue-hall.jpg" alt="Tiered auditorium with red seats and tall arched windows">
        <div class="in">
          <p class="date">Sat · April 17 · Evening</p>
          <h3>Jalwa</h3>
          <p class="mood">Gala and awards</p>
          <p class="d">Alumni awards, a toast to the milestone batches, then the dance floor.</p>
        </div>
      </article>
      <article class="card">
        <img src="images/venue-aerial.jpg" alt="Aerial view of Maison 6405 beside the pond">
        <div class="in">
          <p class="date">Sun · April 18 · Morning</p>
          <h3>Chai Pila De</h3>
          <p class="mood">Chai and breakfast</p>
          <p class="d">One more cup and one more conversation before the goodbyes.</p>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="teaser">
  <div class="wrap grid2">
    <div>
      <p class="label">The venue</p>
      <h2>{VENUE}</h2>
      <p class="lede">{ADDRESS}. A lakeside building in greater Atlanta with a tiered auditorium and room for long conversations.</p>
      <p class="more"><a href="venue.html">Venue and travel →</a></p>
    </div>
    <div class="shot"><img src="images/venue-aerial.jpg" alt="Aerial view of Maison 6405 beside a pond, surrounded by woods"></div>
  </div>
</section>

<section class="refs">
  <div class="wrap">
    <div class="refgrid">
      <a class="ref" href="speakers.html">
        <p class="label">Speakers</p>
        <h2>Who is on stage</h2>
        <p>Keynotes, panels and conversations led by alumni. Names and bios will be announced here.</p>
        <span class="arrow">Meet the speakers →</span>
      </a>
      <a class="ref" href="sponsors.html">
        <p class="label">Sponsors</p>
        <h2>Partner with us</h2>
        <p>Back a reunion of engineers, founders and leaders from five institutions.</p>
        <span class="arrow">Become a sponsor →</span>
      </a>
    </div>
  </div>
</section>'''
page("index.html", "Jashn-e-Yaarana 2027", "index.html", home)

# ---------------------------------------------------------------- About
about = inner_head("atlanta-park.jpg", "About", "The story behind<br>Jashn-e-Yaarana",
                   "Why we are coming back together, and what the name means.", "50% 45%") + f'''
<section>
  <div class="wrap grid">
    <p class="label">The name</p>
    <div>
      <h2>Celebration and friendship, in one phrase.</h2>
      <div class="words">
        <div><b>Jashn</b><i>celebration</i></div>
        <div><b>Yaarana</b><i>friendship</i></div>
      </div>
      <div class="prose">
        <p>DC26 in Washington brought more than 300 of us together, and the question at the end was how to stay connected. This year's answer is a reunion built around the yaar: the batchmate from your hostel, the senior who got you your first job, the junior you now mentor.</p>
        <p>Bring them, find them, or meet them for the first time.</p>
      </div>
    </div>
  </div>
</section>

<section class="lineage">
  <div class="wrap">
    <div class="head">
      <h2>Two lineages, one table</h2>
      <p>The names changed. The people kept finding each other.</p>
    </div>
    <div class="routes">
      <div class="route"><h3>Route one</h3><div class="chain">DCE <i>→</i> DTU</div><p>Delhi College of Engineering, which began as Delhi Polytechnic in 1941, became Delhi Technological University in 2009.</p></div>
      <div class="route"><h3>Route two</h3><div class="chain">DIT <i>→</i> NSIT <i>→</i> NSUT</div><p>Delhi Institute of Technology, then NSIT, now Netaji Subhas University of Technology.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="head">
      <h2>Not just to survive. To soar.</h2>
      <p>Four ideas the reunion is built on.</p>
    </div>
    <div class="vals">
      <div class="val"><h3>Courage</h3><p>Stories from alumni who took the leap: new countries, companies and careers.</p></div>
      <div class="val"><h3>Inclusion</h3><p>Every batch, branch and ability. Families welcome at every event.</p></div>
      <div class="val"><h3>Opportunity</h3><p>Jobs, mentorship and introductions shared freely across the network.</p></div>
      <div class="val"><h3>Together</h3><p>One community, from Kashmere Gate to Bawana Road to Dwarka.</p></div>
    </div>
  </div>
</section>'''
page("about.html", "About · Jashn-e-Yaarana 2027", "about.html", about)

# ---------------------------------------------------------------- Program
def day(date, name, mood, blurb, dress, who, img, alt):
    return f'''<article class="day">
  <div class="dimg"><img src="images/{img}" alt="{alt}"></div>
  <div class="dtext">
    <p class="date">{date}</p>
    <h2>{name}</h2>
    <p class="mood">{mood}</p>
    <p>{blurb}</p>
    <dl><dt>Dress</dt><dd>{dress}</dd><dt>For</dt><dd>{who}</dd><dt>Timings</dt><dd class="tbc">To be shared by the organizers</dd></dl>
  </div>
</article>'''

program = inner_head("venue-night.jpg", "Program", "Three days, four moments",
                     f"{DATES} at {VENUE}. Friday evening, all of Saturday and Sunday morning. Timings will be shared by the organizers.", "50% 40%") + f'''
<section class="days">
  <div class="wrap">
    {day("Friday · April 16 · Evening", "Dhamaal", "Welcome night", "Arrive and find your people. Music, chai and the hostel stories everyone still wants to hear again.", "Hostel casual", "Every batch", "venue-night.jpg", "Maison 6405 lit at night")}
    {day("Saturday · April 17 · Daytime", "Ek Saath", "Leadership Conclave", "Keep the day open. Talks, panels and conversations led by alumni, with a mentorship circle for younger alumni and the group photo.", "Daytime comfortable", "Families welcome", "atlanta-park.jpg", "Atlanta skyline across Piedmont Park's lake")}
    {day("Saturday · April 17 · Evening", "Jalwa", "Gala and awards", "Alumni awards, a toast to the milestone batches, dinner and the dance floor.", "Black tie or festive Indian", "Alumni and guests", "venue-hall.jpg", "The auditorium at Maison 6405")}
    {day("Sunday · April 18 · Morning", "Chai Pila De", "Chai and breakfast", "Start the last morning with chai, breakfast and one more round of conversations before everyone heads home. At least stay for chai.", "Sunday comfortable", "Everyone", "venue-aerial.jpg", "Aerial view of Maison 6405 beside the pond")}
    <article class="depart">
      <p class="date">Sunday · After breakfast</p>
      <h2>Departure</h2>
      <p>Check out and travel home.</p>
    </article>
    <p class="note">Session details and speakers are still being finalised. See <a href="speakers.html">Speakers</a> for who is joining us.</p>
  </div>
</section>'''
page("program.html", "Program · Jashn-e-Yaarana 2027", "program.html", program)

# ---------------------------------------------------------------- Speakers
def speaker(role):
    return f'''<article class="spk">
  <div class="avatar" aria-hidden="true"></div>
  <p class="role">{role}</p>
  <h3>Speaker to be announced</h3>
  <p class="meta">Title · Company</p>
  <p class="meta">Batch · Branch · Institution</p>
  <div class="bio" aria-label="Bio placeholder"><i></i><i></i><i></i><i class="short"></i></div>
</article>'''

roles = ["Keynote", "Keynote", "Panel", "Panel", "Fireside chat", "Mentorship circle"]
speakers = inner_head("venue-hall.jpg", "Speakers", "The people on stage",
                      "Keynotes, panels and conversations led by alumni. Names and bios will appear here as they are confirmed.", "50% 55%") + f'''
<section>
  <div class="wrap">
    <div class="head">
      <h2>Announcing soon</h2>
      <p>Each speaker gets a card with their photo, role, batch and a short bio.</p>
    </div>
    <div class="spk-grid">
      {"".join(speaker(r) for r in roles)}
    </div>
    <div class="format">
      <h3>What each bio will include</h3>
      <ul>
        <li>Name, current title and company</li>
        <li>Batch, branch and institution (DCE, DIT, DTU, NSIT or NSUT)</li>
        <li>A bio of about 60 words</li>
        <li>Their session title and which day it is on</li>
      </ul>
    </div>
  </div>
</section>'''
page("speakers.html", "Speakers · Jashn-e-Yaarana 2027", "speakers.html", speakers)

# ---------------------------------------------------------------- Venue
venue = inner_head("venue-aerial.jpg", "Venue", VENUE, f"{ADDRESS}. Greater Atlanta, Georgia.", "50% 45%") + f'''
<section class="venue">
  <div class="wrap grid2">
    <div>
      <p class="label">The details</p>
      <h2>Where we gather</h2>
      <dl class="facts">
        <dt>Venue</dt><dd>{VENUE}</dd>
        <dt>Address</dt><dd>{ADDRESS}</dd>
        <dt>Dates</dt><dd>{DATES}</dd>
        <dt>Setting</dt><dd>Lakeside building with wooded grounds</dd>
        <dt>Main hall</dt><dd>Tiered auditorium with tall arched windows</dd>
        <dt>Hotels</dt><dd class="tbc">Room block to be confirmed</dd>
        <dt>Getting there</dt><dd class="tbc">Airport and transfer details to follow</dd>
      </dl>
      <p class="more"><a href="{MAPS}" target="_blank" rel="noopener">Open in Maps ↗</a></p>
    </div>
    <div class="shot"><img src="images/venue-aerial.jpg" alt="Aerial view of Maison 6405 beside a pond, surrounded by woods"></div>
  </div>
</section>

<section class="gallery">
  <div class="wrap">
    <div class="head"><h2>Inside and out</h2><p>The building by day and by night, and the hall where the program happens.</p></div>
    <div class="trip">
      <div class="shot"><img src="images/venue-night.jpg" alt="Maison 6405 lit in purple and gold at night"></div>
      <div class="shot"><img src="images/venue-hall.jpg" alt="Tiered auditorium with red seats"></div>
    </div>
  </div>
</section>

<section class="around">
  <div class="wrap">
    <div class="head"><h2>Around Atlanta</h2><p>Picks from Atlanta-based alumni will be added here.</p></div>
    <div class="trip">
      <figure class="shot"><img src="images/hero-skyline.jpg" alt="Downtown Atlanta at dusk"><figcaption>Downtown Atlanta</figcaption></figure>
      <figure class="shot"><img src="images/atlanta-park.jpg" alt="Midtown towers across Piedmont Park's lake"><figcaption>Piedmont Park, Midtown</figcaption></figure>
    </div>
  </div>
</section>'''
page("venue.html", "Venue · Jashn-e-Yaarana 2027", "venue.html", venue)

# ---------------------------------------------------------------- Committee
def member(role, focus):
    return f'''<article class="mem"><div class="avatar" aria-hidden="true"></div><p class="role">{role}</p><h3>Name to be added</h3><p class="meta">{focus}</p></article>'''

mems = [("Chair", "Overall direction"), ("Program lead", "Sessions, speakers and awards"),
        ("Venue and logistics", "Maison 6405, hotels and travel"), ("Sponsorship lead", "Partners and funding"),
        ("Registration lead", "Tickets and attendee list"), ("Communications lead", "Website, invitations and updates")]
committee = inner_head("hero-skyline.jpg", "Committee", "The volunteers behind it",
                       "Alumni organising the reunion. Names and batches will be added as roles are confirmed.", "50% 40%") + f'''
<section>
  <div class="wrap">
    <div class="head"><h2>Organising committee</h2><p>Roles planned for the 2027 reunion.</p></div>
    <div class="mem-grid">{"".join(member(*m) for m in mems)}</div>
  </div>
</section>'''
page("committee.html", "Committee · Jashn-e-Yaarana 2027", "committee.html", committee)

# ---------------------------------------------------------------- Sponsors
sponsors = inner_head("atlanta-park.jpg", "Sponsors", "Partner with us",
                      "Back a reunion of engineers, founders and leaders from five institutions.", "50% 50%") + f'''
<section>
  <div class="wrap">
    <div class="head"><h2>Why partner</h2><p>Packages and pricing are still being finalised.</p></div>
    <div class="trio">
      <div><h3>Reach</h3><p>Put your name in front of senior alumni across technology, finance, healthcare and more.</p></div>
      <div><h3>Community</h3><p>Support a network that mentors younger alumni and shares opportunities.</p></div>
      <div><h3>Presence</h3><p>Be part of a three-day program at {VENUE}, from the welcome night to the gala.</p></div>
    </div>
    <div class="format">
      <h3>Sponsorship enquiries</h3>
      <p class="tbc">Contact details to be added.</p>
    </div>
  </div>
</section>'''
page("sponsors.html", "Sponsors · Jashn-e-Yaarana 2027", "sponsors.html", sponsors)

# ---------------------------------------------------------------- Register
# Prices copied from the committee flyer. Confirm before going live.
TICKETS = [("single", "Single"), ("couple", "Couple (2 tickets)"), ("nextgen", "NextGen"), ("parent", "Parent")]
TIERS = [
    dict(id="presale", name="Private Placement", sub="Presale", when="Through November 15, 2026", prices=dict(single=199, couple=390, nextgen=100, parent=179), feature=False),
    dict(id="early", name="IPO", sub="Early bird", when="November 16 – December 15, 2026", prices=dict(single=250, couple=450, nextgen=140, parent=229), feature=True),
    dict(id="market", name="Market Price", sub="Regular admission", when="From December 16, 2026", prices=dict(single=325, couple=600, nextgen=160, parent=250), feature=False),
]

def tier_card(t):
    rows = "".join(f'<li><span>{lab}</span><b>${t["prices"][k]}</b></li>' for k, lab in TICKETS)
    return f'''<article class="tier{" feature" if t["feature"] else ""}" data-tier="{t["id"]}">
  <p class="badge" data-badge>&nbsp;</p>
  <h3>{t["name"]}</h3>
  <p class="tsub">{t["sub"]}</p>
  <p class="twhen">{t["when"]}</p>
  <ul>{rows}</ul>
</article>'''

if REGISTER_URL:
    action = f'<a class="btn buy" href="{REGISTER_URL}" target="_blank" rel="noopener">Payment link →</a>'
else:
    action = '<button class="btn buy" type="button" disabled>Payment link</button>'

register = inner_head("venue-aerial.jpg", "Register", "Tickets and pricing",
                      f"{DATES} at {VENUE}, Duluth. Prices rise on each date, so the earlier you book, the less you pay.", "50% 45%") + f'''
<section class="dates-strip">
  <div class="wrap">
    <div><span>Arrival welcome</span><b>Friday, April 16, 2027</b></div>
    <div><span>Departure</span><b>Sunday, April 18, 2027</b></div>
  </div>
</section>

<section class="pricing">
  <div class="wrap">
    <div class="head"><h2>Three prices, three windows</h2><p>The price depends on the day you register. These prices are for information. Registration happens on a separate site.</p></div>
    <div class="tiers">{"".join(tier_card(t) for t in TIERS)}</div>
    <div class="regaction">{action}</div>
  </div>
</section>

<section class="perks">
  <div class="wrap">
    <ul>
      <li>Reunite with classmates</li><li>Expand your network</li><li>Inspiring panels and speakers</li><li>Great food and entertainment</li><li>Support our community</li>
    </ul>
  </div>
</section>'''
page("register.html", "Tickets · Jashn-e-Yaarana 2027", "register.html", register)
print("Built", len(os.listdir(OUT)), "files in", OUT)
