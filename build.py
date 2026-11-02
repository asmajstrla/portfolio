"""
Builds every page of the site from the content below.

To update the site: edit the lists in this file (case studies, illustration,
graphic design, about), then run `python3 build.py`. Images go in /images
and are referenced by file name, e.g. "images/asbestos-cover.jpg".
"""

from pathlib import Path
from html import escape

ROOT = Path(__file__).parent

NAME_FIRST = "Adam"
NAME_LAST = "Smajstrla"
TITLE = "Creative Director & Product Design"
LOCATION = "Orlando, FL"
LINKEDIN = "https://www.linkedin.com/in/adam-smajstrla/"
DRIBBBLE = "https://dribbble.com/smaj"
EMAIL = ""          # add an email to show a "Email me" button
RESUME = ""         # e.g. "files/adam-smajstrla-resume.pdf"
PORTRAIT = ""       # e.g. "images/adam.jpg"

# ---------------------------------------------------------------------------
# UX case studies (shown on Home and the UX page, each gets its own page).
# Fill in what you have; empty fields show a placeholder.
# ---------------------------------------------------------------------------
CASE_STUDIES = [
    {
        "slug": "asbestos-com",
        "title": "Asbestos.com",
        "summary": "Redesigning the homepage and mobile experience for a patient resource site.",
        "meta": "Add role and year",
        "color": "var(--c1)",
        "cover": "",
        "facts": {"Role": "", "Team": "", "Timeline": "", "Tools": ""},
    },
    {
        "slug": "red-6-ar",
        "title": "Red 6 AR",
        "summary": "Marketing website for an augmented reality flight training company.",
        "meta": "Add role and year",
        "color": "var(--c2)",
        "cover": "",
        "facts": {"Role": "", "Team": "", "Timeline": "", "Tools": ""},
    },
    {
        "slug": "case-study-3",
        "title": "Case study three",
        "summary": "One sentence on the problem and what changed because of your work.",
        "meta": "Add role and year",
        "color": "var(--c3)",
        "cover": "",
        "facts": {"Role": "", "Team": "", "Timeline": "", "Tools": ""},
    },
    {
        "slug": "case-study-4",
        "title": "Case study four",
        "summary": "One sentence on the problem and what changed because of your work.",
        "meta": "Add role and year",
        "color": "var(--c4)",
        "cover": "",
        "facts": {"Role": "", "Team": "", "Timeline": "", "Tools": ""},
    },
    {
        "slug": "case-study-5",
        "title": "Case study five",
        "summary": "One sentence on the problem and what changed because of your work.",
        "meta": "Add role and year",
        "color": "var(--c5)",
        "cover": "",
        "facts": {"Role": "", "Team": "", "Timeline": "", "Tools": ""},
    },
    {
        "slug": "case-study-6",
        "title": "Case study six",
        "summary": "One sentence on the problem and what changed because of your work.",
        "meta": "Add role and year",
        "color": "var(--c6)",
        "cover": "",
        "facts": {"Role": "", "Team": "", "Timeline": "", "Tools": ""},
    },
]

# Sections every case study page walks through, with prompts shown until filled.
CS_SECTIONS = [
    ("The problem", "What was broken or missing, for whom, and why it mattered to the business."),
    ("Research", "What you learned and how: interviews, analytics, audits, competitive review."),
    ("Process", "Key flows, wireframes and iterations. Show one decision you changed your mind on."),
    ("The solution", "The final design and the reasoning behind its most important choices."),
    ("Outcome", "Results with numbers where you have them, and what you'd do next."),
]

# ---------------------------------------------------------------------------
# Illustration and graphic design galleries. "ar" is the image shape
# (1 = square, 0.8 = tall, 1.33 = wide). "link" can point to Dribbble.
# ---------------------------------------------------------------------------
def shot(path):
    return f"https://dribbble.com/shots/{path}"

ILLUSTRATION = [
    ("Project Hail Mary patch", shot("24406871-Project-Hail-Mary-Patch"), 1),
    ("Japanese hero mask lockup", shot("18768773-Japanese-Hero-Mask-lockup"), 0.8),
    ("Hero trainer shirt", shot("18768765-Hero-Trainer-Shirt"), 1),
    ("Year of the Tiger", shot("17400512-Lunar-New-Year-Year-of-the-Tiger"), 1.33),
    ("Year of the Ox", shot("15220921-Year-of-the-Ox"), 1),
    ("Asian neon masks", shot("16815939-Asian-Neon-Masks"), 0.8),
    ("Dumplings and Dragons mural", shot("16497704-Dumplings-and-Dragons-Mural"), 1.33),
    ("Gan Bei garden mural", shot("23851276-Gan-Bei-garden-mural"), 1.33),
    ("I Wanna Wok", shot("15269558-I-Wanna-Wok"), 1),
    ("Ghost Chicken", shot("14330013-Ghost-Chicken"), 0.8),
    ("Foo dog drink coaster", shot("18206271-Foo-Dog-Drink-Coaster"), 1),
    ("Daruma lucky cat coaster", shot("17164490-Daruma-Lucky-Cat-Drink-Coaster"), 1),
]

GRAPHIC = [
    ("UCF MBA downtown wall wrap", shot("25710813-UCF-MBA-Downtown-Wall-Wrap"), 1.33),
    ("Hawkers brunch menu", shot("23805985-Hawkers-Brunch-Menu"), 0.8),
    ("Hawkers takeout bag", shot("23851265-Hawkers-takeout-bag"), 1),
    ("Hawkers beverage coasters", shot("23851250-Hawkers-beverage-coasters"), 1),
    ("Brunch photoshoot", shot("23805896-Brunch-Photoshoot"), 1.33),
    ("Spicy Smile neon sign", shot("17328539-Spicy-Smile-Neon-Sign"), 0.8),
    ("Nice Buns neon", shot("17328280-Nice-Buns-Neon"), 1),
    ("Hutch Studio logo", shot("15241727-Hutch-Studio-Logo"), 1.33),
    ("Lucky cat anniversary pin", shot("15155282-Luck-Cat-Anniversary-Pin"), 1),
]
TILE_COLORS = ["var(--c1)", "var(--c3)", "var(--c5)", "var(--c4)", "var(--c6)", "var(--c2)"]

# Images for gallery tiles, keyed by title, e.g. {"Year of the Ox": "images/ox.jpg"}
GALLERY_IMAGES = {}

# ---------------------------------------------------------------------------
# About page
# ---------------------------------------------------------------------------
ABOUT_BIO = [
    "I'm a creative director and product designer in Orlando, Florida. I lead product work from early research through launch, and I keep a steady practice in illustration and graphic design.",
    "Draft bio: replace this paragraph with a few sentences on how you work, the teams you've led, and what you care about in a product.",
]
EXPERIENCE = [
    ("Company name", "Role, years"),
    ("Company name", "Role, years"),
    ("Company name", "Role, years"),
]
SKILLS = "UX strategy, product design, design systems, prototyping, user research, art direction, illustration, branding"

# ===========================================================================
# Templates below. You shouldn't need to edit these for content changes.
# ===========================================================================

SPARK = '<svg class="spark" viewBox="0 0 40 40" aria-hidden="true"><g fill="currentColor">' + "".join(
    f'<ellipse cx="20" cy="9" rx="4.2" ry="9" transform="rotate({a} 20 20)"/>' for a in range(0, 360, 45)
) + '<circle cx="20" cy="20" r="4"/></g></svg>'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>'
MENU = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'

NAV = [("index.html", "Home"), ("ux.html", "UX"), ("illustration.html", "Illustration"),
       ("graphic-design.html", "Graphic design"), ("about.html", "About")]


def contact_href():
    return f"mailto:{EMAIL}" if EMAIL else LINKEDIN


def page(title, body, current, prefix="", description=""):
    cur = ' aria-current="page"'
    links = "".join(
        f'<li><a href="{prefix}{href}"{cur if href == current else ""}>{label}</a></li>'
        for href, label in NAV
    )
    favicon = (SPARK.replace('class="spark"', 'xmlns="http://www.w3.org/2000/svg"')
               .replace("currentColor", "%239BCB3C").replace('"', "'")
               .replace("<", "%3C").replace(">", "%3E"))
    desc = escape(description or f"{NAME_FIRST} {NAME_LAST}, {TITLE}. UX case studies, illustration and graphic design.")
    full_title = f"{title} | {NAME_FIRST} {NAME_LAST}" if title else f"{NAME_FIRST} {NAME_LAST} | {TITLE}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full_title)}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800;900&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/styles.css">
<link rel="icon" href="data:image/svg+xml,{favicon}">
</head>
<body>
<header class="nav">
  <div class="wrap">
    <a class="logo" href="{prefix}index.html">{SPARK}<span>{NAME_LAST}</span></a>
    <nav aria-label="Main">
      <button class="menu-btn" aria-expanded="false" aria-controls="menu" aria-label="Open menu">{MENU}</button>
      <ul id="menu">{links}</ul>
    </nav>
    <a class="btn" href="{contact_href()}">Get in touch</a>
  </div>
</header>
<main>
{body}
</main>
<footer>
  <div class="wrap">
    <span>&copy; {NAME_FIRST} {NAME_LAST}, {LOCATION}</span>
    <nav aria-label="Elsewhere"><a href="{LINKEDIN}">LinkedIn</a><a href="{DRIBBBLE}">Dribbble</a></nav>
  </div>
</footer>
<script>
  const b = document.querySelector('.menu-btn'), m = document.getElementById('menu');
  b.addEventListener('click', () => {{
    const open = m.classList.toggle('open');
    b.setAttribute('aria-expanded', open);
    b.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  }});
</script>
</body>
</html>
"""


def art(src, alt, label, color, prefix=""):
    if src:
        return f'<img src="{prefix}{src}" alt="{escape(alt)}" loading="lazy">'
    return f'<div class="ph" style="--ph:{color}">{escape(label)}</div>'


def panels(prefix=""):
    out = []
    for cs in CASE_STUDIES:
        href = f"{prefix}work/{cs['slug']}.html"
        out.append(f"""<section class="panel" style="--bg:{cs['color']}">
  <div class="wrap">
    <div class="art">{art(cs['cover'], cs['title'] + ' cover', 'Add a cover image for ' + cs['title'], cs['color'], prefix)}</div>
    <div>
      <div class="meta">{escape(cs['meta'])}</div>
      <h3>{escape(cs['title'])}</h3>
      <p>{escape(cs['summary'])}</p>
      <a class="btn" href="{href}">Read the case study {ARROW}</a>
    </div>
  </div>
</section>""")
    return "\n".join(out)


def cta(prefix=""):
    actions = f'<a class="btn" href="{contact_href()}">{"Email me" if EMAIL else "Message me on LinkedIn"}</a>'
    if RESUME:
        actions += f'<a class="btn ghost" href="{prefix}{RESUME}">Download résumé</a>'
    return f"""<section class="cta wrap">
  <h2>Let's work together {SPARK}</h2>
  <p>Open to product design and creative leadership roles.</p>
  <div class="actions">{actions}</div>
</section>"""


def build_home():
    portrait = art(PORTRAIT, f"Portrait of {NAME_FIRST} {NAME_LAST}", "Add your photo", "#F7C9A0")
    resume_btn = f'<a class="btn" href="{RESUME}">Download résumé</a>' if RESUME else f'<a class="btn" href="{LINKEDIN}">View LinkedIn</a>'
    thumbs = {"UX & product design": "var(--c4)", "Illustration": "var(--c1)", "Graphic design": "var(--c5)"}
    disciplines = [
        ("ux.html", "UX & product design", "Research, flows and shipped products, told as case studies."),
        ("illustration.html", "Illustration", "Patches, murals, characters and lettering."),
        ("graphic-design.html", "Graphic design", "Brand systems, menus, packaging, signage and print."),
    ]
    d_items = "".join(
        f'<li><a href="{h}"><span class="thumb" style="background:{thumbs[t]}"></span><h3>{t}</h3><p>{d}</p><span class="round">{ARROW}</span></a></li>'
        for h, t, d in disciplines
    )
    body = f"""<section class="hero">
  <div class="wrap">
    <div class="stage">
      <h1 class="first"><span aria-hidden="true">{NAME_FIRST}</span><span class="sr">{NAME_FIRST} {NAME_LAST}</span></h1>
      <div class="portrait">{portrait}{SPARK}</div>
      <div class="intro"><p>Creative director and product designer in {LOCATION}. I take products from research to launch.</p>{resume_btn}</div>
      <div class="last display" aria-hidden="true">{NAME_LAST}</div>
    </div>
    <div class="role"><strong>{TITLE}</strong><a href="{LINKEDIN}">LinkedIn</a><a href="{DRIBBBLE}">Dribbble</a></div>
  </div>
</section>

<section class="statement wrap">
  <p>I design products people find easy to use, and I bring an illustrator's eye to every screen.</p>
</section>

<section class="disciplines wrap">
  <h2>What I do</h2>
  <ul class="d-list">{d_items}</ul>
</section>

<div class="wrap work-head">
  <h2>Selected case studies</h2>
  <p>How I approach product problems, from the first conversation to the shipped design.</p>
</div>
{panels()}
{cta()}"""
    return page("", body, "index.html")


def build_ux():
    body = f"""<section class="page-head wrap">
  <h1>UX & product design</h1>
  <p>Case studies covering research, interaction design and the outcomes of shipped work.</p>
</section>
{panels()}
{cta()}"""
    return page("UX & product design", body, "ux.html")


def build_gallery(title, intro, items, current):
    tiles = []
    for i, (name, link, ar) in enumerate(items):
        color = TILE_COLORS[i % len(TILE_COLORS)]
        img = GALLERY_IMAGES.get(name, "")
        inner = art(img, name, "Add image", color)
        tiles.append(f'<a class="tile" href="{link}" style="--ar:{ar}"><figure style="margin:0">{inner}<figcaption>{escape(name)}</figcaption></figure></a>')
    body = f"""<section class="page-head wrap">
  <h1>{escape(title)}</h1>
  <p>{escape(intro)}</p>
</section>
<section class="wrap gallery">{''.join(tiles)}</section>
{cta()}"""
    return page(title, body, current)


def build_about():
    portrait = art(PORTRAIT, f"Portrait of {NAME_FIRST} {NAME_LAST}", "Add your photo", "#F7C9A0")
    bio = "".join(f"<p>{escape(p)}</p>" for p in ABOUT_BIO)
    xp = "".join(f"<li><span>{escape(c)}</span><span>{escape(r)}</span></li>" for c, r in EXPERIENCE)
    body = f"""<section class="wrap about">
  <div class="portrait">{portrait}</div>
  <div class="bio">
    <h1>About me</h1>
    {bio}
    <h2>Experience</h2>
    <ul class="xp">{xp}</ul>
    <h2>What I bring</h2>
    <p>{escape(SKILLS)}</p>
  </div>
</section>
{cta()}"""
    return page("About", body, "about.html")


def build_case_study(i, cs):
    p = "../"
    facts = "".join(f"<div><dt>{k}</dt><dd>{escape(v) if v else '—'}</dd></div>" for k, v in cs["facts"].items())
    sections = "".join(
        f'<section><h2>{t}</h2><div><p class="note">{escape(prompt)}</p><div class="ph" style="--ph:{cs["color"]}">Add an image</div></div></section>'
        for t, prompt in CS_SECTIONS
    )
    nxt = CASE_STUDIES[(i + 1) % len(CASE_STUDIES)]
    body = f"""<section class="cs-hero" style="--bg:{cs['color']}">
  <div class="wrap">
    <a class="back" href="{p}ux.html">All case studies</a>
    <h1>{escape(cs['title'])}</h1>
    <p class="lede">{escape(cs['summary'])}</p>
    <div class="cs-cover">{art(cs['cover'], cs['title'] + ' cover', 'Add a cover image', cs['color'], p)}</div>
  </div>
</section>
<div class="wrap">
  <dl class="facts">{facts}</dl>
  <div class="cs-body">{sections}</div>
  <section class="cs-next">
    <p>Next case study</p>
    <h2>{escape(nxt['title'])}</h2>
    <a class="btn" href="{nxt['slug']}.html">Read it {ARROW}</a>
  </section>
</div>"""
    html = page(cs["title"], body, "ux.html", prefix=p)
    return html.replace(f'href="{p}ux.html" aria-current', f'href="{p}ux.html" aria-current')


def main():
    (ROOT / "work").mkdir(exist_ok=True)
    (ROOT / "images").mkdir(exist_ok=True)
    files = {
        "index.html": build_home(),
        "ux.html": build_ux(),
        "illustration.html": build_gallery("Illustration", "Patches, murals, characters and lettering for restaurants, brands and personal projects.", ILLUSTRATION, "illustration.html"),
        "graphic-design.html": build_gallery("Graphic design", "Brand identity, menus, packaging, signage and environmental graphics.", GRAPHIC, "graphic-design.html"),
        "about.html": build_about(),
    }
    for i, cs in enumerate(CASE_STUDIES):
        files[f"work/{cs['slug']}.html"] = build_case_study(i, cs)
    for name, html in files.items():
        (ROOT / name).write_text(html, encoding="utf-8")
    print(f"Built {len(files)} pages")


if __name__ == "__main__":
    main()
