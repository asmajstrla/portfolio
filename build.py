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
        "cover": "images/work/asbestos-com-homepage.webp",
        "video": "images/work/asbestos-com-homepage.mp4",
        # images or videos for sections of the case study page, by section name
        "media": {"The solution": ("images/work/asbestos-com-mobile-homepage.webp", "images/work/asbestos-com-mobile-homepage.mp4")},
        "facts": {"Role": "", "Team": "", "Timeline": "", "Tools": ""},
    },
    {
        "slug": "red-6-ar",
        "title": "Red 6 AR",
        "summary": "Marketing website for an augmented reality flight training company.",
        "meta": "Add role and year",
        "color": "var(--c2)",
        "cover": "images/work/red-6-ar-website.webp",
        "video": "images/work/red-6-ar-website.mp4",
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
# Illustration and graphic design galleries: (title, link, image, shape).
# Shape is width / height (1 = square, 0.8 = tall, 1.33 = wide).
# ---------------------------------------------------------------------------
def shot(path):
    return f"https://dribbble.com/shots/{path}"

ILLUSTRATION = [
    ("Project Hail Mary patch", shot("24406871-Project-Hail-Mary-Patch"), "images/work/project-hail-mary-patch.webp", 1.333),
    ("Gan Bei garden mural", shot("23851276-Gan-Bei-garden-mural"), "images/work/gan-bei-garden-mural.webp", 3.002),
    ("Japanese hero mask lockup", shot("18768773-Japanese-Hero-Mask-lockup"), "images/work/japanese-hero-mask-lockup.webp", 1.333),
    ("Hero trainer shirt", shot("18768765-Hero-Trainer-Shirt"), "images/work/hero-trainer-shirt.webp", 1.333),
    ("Year of the Tiger", shot("17400512-Lunar-New-Year-Year-of-the-Tiger"), "images/work/lunar-new-year-year-of-the-tiger.webp", 1.333),
    ("Dumplings and Dragons mural", shot("16497704-Dumplings-and-Dragons-Mural"), "images/work/dumplings-and-dragons-mural.webp", 1.333),
    ("Year of the Ox", shot("15220921-Year-of-the-Ox"), "images/work/year-of-the-ox.webp", 1.333),
    ("Kabuki mask", shot("14108104-Kabuki-Mask"), "images/work/kabuki-mask.webp", 1.333),
    ("Mother's Day nesting dolls", shot("11223059-Happy-Mother-s-Day-Nesting-Dolls"), "images/work/happy-mother-s-day-nesting-dolls.webp", 1.333),
    ("Lucky cat", shot("11056498-Cute-Lucky-Cat"), "images/work/cute-lucky-cat.webp", 1.008),
    ("Hawkers noodle tiger shirt", shot("10984333-Hawkers-Noodle-Tiger-Shirt"), "images/work/hawkers-noodle-tiger-shirt.webp", 1.333),
    ("Nom Com movie night", shot("10929946-Nom-Com-Movie-Night"), "images/work/nom-com-movie-night.webp", 1.333),
    ("Year of the Rat", shot("9251338-Happy-New-Year-2020-Year-of-the-Rat"), "images/work/happy-new-year-2020-year-of-the-rat.webp", 1.333),
    ("Geisha and koi", shot("8843100-Geisha-and-Koi"), "images/work/geisha-and-koi.webp", 1.333),
    ("Streets of Asia", shot("6964502-Streets-of-Asia"), "images/work/streets-of-asia.webp", 1.333),
    ("Asian food illustrations", shot("6956142-Asian-food-illustrations"), "images/work/asian-food-illustrations.webp", 1.333),
    ("Street of Asia", shot("6681799-Street-of-Asia"), "images/work/street-of-asia.webp", 1.333),
    ("Hawkers tiger", shot("6666118-Hawkers-Tiger"), "images/work/hawkers-tiger.webp", 1.333),
    ("Main Street Bridge", shot("6500266-Main-Street-Bridge"), "images/work/main-street-bridge.webp", 1.333),
    ("Fu lion with noodles", shot("6459728-Fu-Lion-playing-with-noodles"), "images/work/fu-lion-playing-with-noodles.webp", 1.333),
]

GRAPHIC = [
    ("UCF MBA downtown wall wrap", shot("25710813-UCF-MBA-Downtown-Wall-Wrap"), "images/work/ucf-mba-downtown-wall-wrap.webp", 2.27),
    ("Hawkers brunch menu", shot("23805985-Hawkers-Brunch-Menu"), "images/work/hawkers-brunch-menu.webp", 1.5),
    ("Hawkers takeout bag", shot("23851265-Hawkers-takeout-bag"), "images/work/hawkers-takeout-bag.webp", 1.5),
    ("Hawkers beverage coasters", shot("23851250-Hawkers-beverage-coasters"), "images/work/hawkers-beverage-coasters.webp", 1.356),
    ("Brunch photoshoot", shot("23805896-Brunch-Photoshoot"), "images/work/brunch-photoshoot.webp", 1.5),
    ("Spicy Smile neon sign", shot("17328539-Spicy-Smile-Neon-Sign"), "images/work/spicy-smile-neon-sign.webp", 1.333),
    ("Foo dog drink coaster", shot("18206271-Foo-Dog-Drink-Coaster"), "images/work/foo-dog-drink-coaster.webp", 1.333),
    ("Nice Buns neon", shot("17328280-Nice-Buns-Neon"), "images/work/nice-buns-neon.webp", 1.333),
    ("Daruma lucky cat coaster", shot("17164490-Daruma-Lucky-Cat-Drink-Coaster"), "images/work/daruma-lucky-cat-drink-coaster.webp", 1.333),
    ("Asian neon masks", shot("16815939-Asian-Neon-Masks"), "images/work/asian-neon-masks.webp", 1.333),
    ("I Wanna Wok logo", shot("15269558-I-Wanna-Wok"), "images/work/i-wanna-wok.webp", 1.191),
    ("Hutch Studio logo", shot("15241727-Hutch-Studio-Logo"), "images/work/hutch-studio-logo.webp", 1.333),
    ("Lucky cat anniversary pin", shot("15155282-Luck-Cat-Anniversary-Pin"), "images/work/luck-cat-anniversary-pin.webp", 1.333),
    ("Ghost Chicken logo", shot("14330013-Ghost-Chicken"), "images/work/ghost-chicken.webp", 1.368),
    ("I Wanna Wok hat", shot("10482439-I-wanna-wok-hat-design"), "images/work/i-wanna-wok-hat-design.webp", 1.0),
    ("Cocktail icons", shot("7726999-cocktails"), "images/work/cocktails.webp", 1.333),
    ("Neon cocktails", shot("7136746-Neon-Cocktails"), "images/work/neon-cocktails.webp", 1.333),
    ("Drink Like a Fish neon sign", shot("7116300-Drink-Like-a-Fish-Neon-sign"), "images/work/drink-like-a-fish-neon-sign.webp", 1.513),
    ("Lapel pins", shot("7104319-Lapel-Pins"), "images/work/lapel-pins.webp", 1.333),
    ("Hawkers to-go cup", shot("6925201-Hawkers-To-Go-Cup"), "images/work/hawkers-to-go-cup.webp", 1.333),
    ("Hawkers tiger trucker cap", shot("6837331-Hawkers-Tiger-Trucker-Cap"), "images/work/hawkers-tiger-trucker-cap.webp", 1.333),
    ("Nom neon", shot("6661071-Nom-Neon"), "images/work/nom-neon.webp", 1.335),
    ("Lucky cat stamp neon", shot("6655245-Lucky-Cat-Stamp-Neon"), "images/work/lucky-cat-stamp-neon.webp", 1.333),
    ("The Great Wave neon", shot("6620247-The-Great-Wave-Neon"), "images/work/the-great-wave-neon.webp", 1.333),
    ("Custom neons", shot("6494993-Custom-Neons"), "images/work/custom-neons.webp", 1.333),
]
# Pieces that play as looping video instead of a still (title: video file).
# The still image is shown first and to anyone who prefers reduced motion.
GALLERY_VIDEOS = {
    "Nom Com movie night": "images/work/nom-com-movie-night.mp4",
    "Mother's Day nesting dolls": "images/work/happy-mother-s-day-nesting-dolls.mp4",
}

TILE_COLORS = ["var(--c1)", "var(--c3)", "var(--c5)", "var(--c4)", "var(--c6)", "var(--c2)"]


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
               .replace("currentColor", "%23FF7A2F").replace('"', "'")
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
  const vids = document.querySelectorAll('video[data-autoplay]');
  if (vids.length && !matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window) {{
    const io = new IntersectionObserver(es => es.forEach(e => e.isIntersecting ? e.target.play().catch(() => {{}}) : e.target.pause()), {{ threshold: 0.25 }});
    vids.forEach(v => io.observe(v));
  }}
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


def art(src, alt, label, color, prefix="", video=""):
    """An image, a looping video (with the image as its still), or a placeholder."""
    if src and video:
        return (f'<video src="{prefix}{video}" poster="{prefix}{src}" muted loop playsinline '
                f'preload="metadata" aria-label="{escape(alt)}, animated" data-autoplay></video>')
    if src:
        return f'<img src="{prefix}{src}" alt="{escape(alt)}" loading="lazy">'
    return f'<div class="ph" style="--ph:{color}">{escape(label)}</div>'


def panels(prefix=""):
    out = []
    for cs in CASE_STUDIES:
        href = f"{prefix}work/{cs['slug']}.html"
        out.append(f"""<section class="panel" style="--bg:{cs['color']}">
  <div class="wrap">
    <div class="art">{art(cs['cover'], cs['title'] + ' cover', 'Add a cover image for ' + cs['title'], cs['color'], prefix, cs.get('video', ''))}</div>
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
    portrait = art(PORTRAIT, f"Portrait of {NAME_FIRST} {NAME_LAST}", "Add your photo", "#FFB27F")
    resume_btn = f'<a class="btn" href="{RESUME}">Download résumé</a>' if RESUME else f'<a class="btn" href="{LINKEDIN}">View LinkedIn</a>'
    thumbs = {"UX & product design": "images/work/asbestos-com-homepage.webp", "Illustration": "images/work/lunar-new-year-year-of-the-tiger.webp", "Graphic design": "images/work/nice-buns-neon.webp"}
    disciplines = [
        ("ux.html", "UX & product design", "Research, flows and shipped products, told as case studies."),
        ("illustration.html", "Illustration", "Patches, murals, characters and lettering."),
        ("graphic-design.html", "Graphic design", "Brand systems, menus, packaging, signage and print."),
    ]
    d_items = "".join(
        f'<li><a href="{h}"><img class="thumb" src="{thumbs[t]}" alt="" loading="lazy"><h3>{t}</h3><p>{d}</p><span class="round">{ARROW}</span></a></li>'
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
    for i, (name, link, img, ar) in enumerate(items):
        color = TILE_COLORS[i % len(TILE_COLORS)]
        inner = art(img, name, "Add image", color, video=GALLERY_VIDEOS.get(name, ""))
        tiles.append(f'<a class="tile" href="{link}" style="--ar:{ar}"><figure style="margin:0">{inner}<figcaption>{escape(name)}</figcaption></figure></a>')
    body = f"""<section class="page-head wrap">
  <h1>{escape(title)}</h1>
  <p>{escape(intro)}</p>
</section>
<section class="wrap gallery">{''.join(tiles)}</section>
{cta()}"""
    return page(title, body, current)


def build_about():
    portrait = art(PORTRAIT, f"Portrait of {NAME_FIRST} {NAME_LAST}", "Add your photo", "#FFB27F")
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


def section_media(cs, section, prefix):
    img, video = cs.get("media", {}).get(section, ("", ""))
    return art(img, f'{cs["title"]}: {section.lower()}', "Add an image", cs["color"], prefix, video)


def build_case_study(i, cs):
    p = "../"
    facts = "".join(f"<div><dt>{k}</dt><dd>{escape(v) if v else '—'}</dd></div>" for k, v in cs["facts"].items())
    sections = "".join(
        f'<section><h2>{t}</h2><div><p class="note">{escape(prompt)}</p><div class="media">{section_media(cs, t, p)}</div></div></section>'
        for t, prompt in CS_SECTIONS
    )
    nxt = CASE_STUDIES[(i + 1) % len(CASE_STUDIES)]
    body = f"""<section class="cs-hero" style="--bg:{cs['color']}">
  <div class="wrap">
    <a class="back" href="{p}ux.html">All case studies</a>
    <h1>{escape(cs['title'])}</h1>
    <p class="lede">{escape(cs['summary'])}</p>
    <div class="cs-cover">{art(cs['cover'], cs['title'] + ' cover', 'Add a cover image', cs['color'], p, cs.get('video', ''))}</div>
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
