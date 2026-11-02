"""
Builds every page of the site from content.py.

    python3 build.py

Content (words, images, projects) lives in content.py; styles in
assets/styles.css. You shouldn't need to edit this file for content changes.
"""

from html import escape
from pathlib import Path

import content as C

ROOT = Path(__file__).parent

PIECES = {p["slug"]: p for p in C.PIECES}
IN_CLIENT = {slug: c for c in C.CLIENTS for _, slugs in c["groups"] for slug in slugs}
for c in C.CLIENTS:
    # a client page's covers: the first piece from each group
    c["images"] = [PIECES[g[1][0]]["images"][0] for g in c["groups"] if g[1]][:4]
    c.setdefault("videos", {})
    for _, slugs in c["groups"]:
        for slug in slugs:
            c["videos"].update(PIECES[slug].get("videos", {}))
SELECTED = [p for p in C.PIECES if p["slug"] not in IN_CLIENT]
BRAND = C.CLIENTS + SELECTED

SECTIONS = [
    # key, nav label, page, projects, intro
    ("ux", "UX", "ux.html", C.UX,
     "Case studies covering research, interaction design and the outcomes of shipped work."),
    ("brand", "Brand", "brand.html", BRAND,
     "Brand systems, illustration and graphic design for restaurants, universities and personal projects."),
]
NAV = [("index.html", "Home")] + [(s[2], s[1]) for s in SECTIONS] + [("about.html", "About")]

# Tiles featured on the home page, after the UX case studies.
HOME_PICKS = ["hawkers", "ucf", "project-hail-mary-patch", "kabuki-mask", "nice-buns-neon",
              "geisha-and-koi", "spicy-smile-neon-sign", "streets-of-asia"]

for key, label, page_name, projects, _ in SECTIONS:
    for p in projects:
        p["section"], p["section_label"], p["section_page"] = key, label, page_name
ALL = {p["slug"]: p for s in SECTIONS for p in s[3]}


# ---------------------------------------------------------------- pieces

def media(src, alt, videos=None, prefix=""):
    """An image, or a looping video using the image as its still."""
    v = (videos or {}).get(src)
    if v:
        return (f'<video src="{prefix}{v}" poster="{prefix}{src}" muted loop playsinline preload="metadata" '
                f'aria-label="{escape(alt)}" data-autoplay></video>')
    return f'<img src="{prefix}{src}" alt="{escape(alt)}" loading="lazy">'


def head(title, prefix):
    full = f"{title} | {C.NAME}" if title else f"{C.NAME} | {C.TITLE}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full)}</title>
<meta name="description" content="{escape(C.NAME)}, {escape(C.TITLE)}. UX case studies, illustration and graphic design.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/styles.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%2317181A'/%3E%3Ctext x='16' y='22' font-family='Helvetica' font-weight='700' font-size='15' fill='%23F5F5F3' text-anchor='middle'%3Eas%3C/text%3E%3C/svg%3E">
</head>"""


def header(current, prefix="", views=False):
    cur = ' aria-current="page"'
    links = "".join(f'<li><a href="{prefix}{h}"{cur if h == current else ""}>{l}</a></li>' for h, l in NAV)
    toggle = ('<div class="views" role="group" aria-label="Layout">'
              '<button type="button" data-set="list" aria-pressed="false">List</button>'
              '<button type="button" data-set="grid" aria-pressed="true">Grid</button></div>') if views else "<span></span>"
    return f"""<header class="top">
  <a class="brand" href="{prefix}index.html">{escape(C.NAME)}</a>
  {toggle}
  <nav aria-label="Main"><button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button>
  <ul class="links" id="menu">{links}</ul></nav>
</header>"""


def project_header(p, prefix):
    return f"""<header class="top">
  <a class="brand" href="{prefix}index.html">{escape(C.NAME)}</a>
  <span></span>
  <a class="close" href="{prefix}{p['section_page']}">Close</a>
</header>"""


def footer():
    links = [(C.LINKEDIN, "LinkedIn"), (C.DRIBBBLE, "Dribbble")]
    if C.EMAIL:
        links.insert(0, (f"mailto:{C.EMAIL}", C.EMAIL))
    nav = "".join(f'<a href="{h}">{escape(l)}</a>' for h, l in links)
    return f'<footer class="foot"><span>{escape(C.NAME)}, {escape(C.LOCATION)}</span><nav aria-label="Elsewhere">{nav}</nav></footer>'


SCRIPT = """<script>
(() => {
  // mobile menu
  const mb = document.querySelector('.menu-btn'), menu = document.getElementById('menu');
  mb && mb.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    mb.setAttribute('aria-expanded', open); mb.textContent = open ? 'Close' : 'Menu';
  });

  // list / grid toggle, remembered per page
  const key = 'view:' + location.pathname;
  const setView = v => {
    document.body.dataset.view = v;
    document.querySelectorAll('.views button').forEach(b => b.setAttribute('aria-pressed', b.dataset.set === v));
    try { localStorage.setItem(key, v); } catch (e) {}
  };
  if (document.querySelector('.views')) {
    let saved = null; try { saved = localStorage.getItem(key); } catch (e) {}
    if (saved) setView(saved);
    document.querySelectorAll('.views button').forEach(b => b.addEventListener('click', () => setView(b.dataset.set)));
  }

  // looping videos play only while visible, and never for reduced motion
  const vids = document.querySelectorAll('video[data-autoplay]');
  if (vids.length && !matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver(es => es.forEach(e =>
      e.isIntersecting ? e.target.play().catch(() => {}) : e.target.pause()), { threshold: 0.25 });
    vids.forEach(v => io.observe(v));
  }

  // lightbox
  const lb = document.querySelector('.lightbox');
  if (lb) {
    const frame = lb.querySelector('.frame'), closeBtn = lb.querySelector('button');
    let last = null;
    const close = () => { lb.classList.remove('open'); frame.innerHTML = ''; document.body.style.overflow = ''; last && last.focus(); };
    document.querySelectorAll('button.shot').forEach(b => b.addEventListener('click', () => {
      last = b;
      const m = b.querySelector('img, video').cloneNode(true);
      m.removeAttribute('loading'); m.removeAttribute('data-autoplay');
      frame.innerHTML = ''; frame.appendChild(m);
      if (m.tagName === 'VIDEO' && !matchMedia('(prefers-reduced-motion: reduce)').matches) m.play().catch(() => {});
      lb.classList.add('open'); document.body.style.overflow = 'hidden'; closeBtn.focus();
    }));
    closeBtn.addEventListener('click', close);
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && lb.classList.contains('open')) close(); });
  }
})();
</script>"""


def page(title, body, prefix="", view=None):
    attr = f' data-view="{view}"' if view else ""
    return f"{head(title, prefix)}\n<body{attr}>\n{body}\n{footer()}\n{SCRIPT}\n</body>\n</html>\n"


GRID_MAX = 10  # 4 across the bottom, 4 above, 2 on top; the List view shows everything


def tiles(projects, prefix="", cols=4):
    out = []
    for i, p in enumerate(projects[:GRID_MAX]):
        inner = (f'<img src="{prefix}{p["images"][0]}" alt="" loading="lazy">' if p["images"]
                 else f'<span class="empty">{escape(p["title"])}</span>')
        out.append(f'<li style="--i:{i}"><a href="{prefix}work/{p["slug"]}.html">{inner}'
                   f'<span class="cap">{escape(p["title"])}<span>{escape(p["type"])}</span></span></a></li>')
    return f'<ul class="tiles" style="--cols:{cols}">{"".join(out)}</ul>'


def rows(projects, prefix="", switchable=True):
    out = []
    for p in projects:
        imgs = "".join(media(src, p["title"], p.get("videos"), prefix) for src in p["images"][:3])
        strip = imgs or '<span class="empty">Add images</span>'
        out.append(f'<a class="row" href="{prefix}work/{p["slug"]}.html"><div class="strip">{strip}</div>'
                   f'<h3>{escape(p["title"])}</h3><p>{escape(p["type"])}</p></a>')
    return f'<div class="list{" switchable" if switchable else ""}">{"".join(out)}</div>'


def masonry(projects, prefix=""):
    """The "List" view on section pages: every piece at its natural shape."""
    out = []
    for p in projects:
        pic = (media(p["images"][0], p["title"], p.get("videos"), prefix) if p["images"]
               else '<span class="empty">Add images</span>')
        out.append(f'<a class="brick" href="{prefix}work/{p["slug"]}.html">{pic}'
                   f'<h3>{escape(p["title"])}</h3><p>{escape(p["type"])}</p></a>')
    return f'<div class="masonry switchable">{"".join(out)}</div>'


# ---------------------------------------------------------------- pages

def build_home():
    # the home page only shows work that has images; empty case studies still appear on the UX page
    ready = [p for p in C.UX if p["images"]]
    featured = ready + [ALL[s] for s in HOME_PICKS if s in ALL]
    sections = "".join(
        f'<li><a href="{pg}">{escape(label)}<span>{len(projs)} {"case studies" if key == "ux" else "projects"}</span></a></li>'
        for key, label, pg, projs, _ in SECTIONS
    ) + '<li><a href="about.html">About<span>Bio, experience and contact</span></a></li>'
    first, last = C.NAME.split(" ", 1)
    body = f"""{header("index.html")}
<main>
  <section class="stage">
    <div>
      <p class="lede">{escape(C.INTRO)}</p>
      <h1 class="word long">{escape(first)}<br>{escape(last)}</h1>
    </div>
    {tiles(featured, cols=4)}
  </section>
  <section class="home-list" aria-labelledby="cs">
    <h2 class="label" id="cs">Case studies</h2>
    {rows(ready, switchable=False)}
  </section>
  <section class="more" aria-labelledby="all">
    <h2 class="label" id="all">All work</h2>
    <ul>{sections}</ul>
  </section>
</main>"""
    return page("", body)


def build_index(key, label, pg, projects, intro):
    long = " long" if len(label) > 10 else ""
    body = f"""{header(pg, views=True)}
<main>
  <section class="stage">
    <div>
      <p class="lede">{escape(intro)}</p>
      <h1 class="word{long}">{escape(label)}</h1>
    </div>
    {tiles(projects)}
  </section>
  {masonry(projects)}
</main>"""
    return page(label, body, view="grid")


def build_project(p):
    pre = "../"
    projs = next(s[3] for s in SECTIONS if s[0] == p["section"])
    i = projs.index(p)
    prev, nxt = projs[i - 1], projs[(i + 1) % len(projs)]

    shots = "".join(
        f'<button class="shot" type="button" aria-label="View larger">{media(src, p["title"], p.get("videos"), pre)}</button>'
        for src in p["images"]
    ) or '<div class="empty">Add images for this project</div>'
    nimg = f'<img src="{pre}{nxt["images"][0]}" alt="">' if nxt["images"] else ""
    next_panel = (f'<a class="next-panel" href="{nxt["slug"]}.html">{nimg}'
                  f'<div><strong>Next: {escape(nxt["title"])}</strong><span>{escape(nxt["type"])}</span></div></a>')

    left = ""
    if p.get("client"):
        left += f'<div><span class="muted">Designed for</span><br>{escape(p["client"])}</div>'
    if p.get("year"):
        left += f'<div><span class="muted">Year</span><br>{escape(p["year"])}</div>'

    text = p.get("description") or p.get("summary") or ""
    desc = f"<p>{escape(text)}</p>" if text else '<p class="prompt">Add a short description of this project.</p>'

    facts = story = groups = ""
    if p.get("groups"):
        secs = ""
        for name, prompt in C.BRAND_PROMPTS.items():
            txt = p.get("sections", {}).get(name, "")
            paras = "".join(f"<p>{escape(t)}</p>" for t in txt.split("\n\n")) if txt else f'<p class="prompt">{escape(prompt)}</p>'
            secs += f'<section><h2>{escape(name)}</h2><div class="body">{paras}</div></section>'
        story = f'<div class="story">{secs}</div>'
        for heading, slugs in p["groups"]:
            bricks = "".join(
                f'<figure class="brick"><button class="shot" type="button" aria-label="View {escape(PIECES[s]["title"])} larger">'
                f'{media(PIECES[s]["images"][0], PIECES[s]["title"], PIECES[s].get("videos"), pre)}</button>'
                f'<figcaption><h3>{escape(PIECES[s]["title"])}</h3><p>{escape(PIECES[s]["type"])}</p></figcaption></figure>'
                for s in slugs)
            groups += f'<section class="group"><h2>{escape(heading)}</h2><div class="masonry">{bricks}</div></section>'
        groups = f'<div class="groups">{groups}</div>'
    if p["section"] == "ux":
        facts = '<dl class="facts">' + "".join(
            f'<div><dt>{k.title()}</dt><dd>{escape(p.get(k) or "—")}</dd></div>' for k in ("role", "team", "timeline", "tools")
        ) + "</dl>"
        secs = ""
        for name, prompt in C.CASE_STUDY_PROMPTS.items():
            txt = p.get("sections", {}).get(name, "")
            paras = "".join(f"<p>{escape(t)}</p>" for t in txt.split("\n\n")) if txt else f'<p class="prompt">{escape(prompt)}</p>'
            secs += f'<section><h2>{escape(name)}</h2><div class="body">{paras}</div></section>'
        story = f'<div class="story">{secs}</div>'

    year = (escape(p["year"]) + "<br>") if p.get("year") else ""
    body = f"""{project_header(p, pre)}
<main>
  <div class="gallery">{shots}{next_panel}</div>
  <div class="info">
    <div class="left">{left}</div>
    <div>
      <h1>{escape(p["title"])}</h1>
      <div class="type">{escape(p["type"])}</div>
      <div class="desc">{desc}</div>
      {facts}
    </div>
  </div>
  {story}
  {groups}
  <nav class="pager" aria-label="More projects">
    <a href="{prev["slug"]}.html"><strong>{escape(prev["title"])}</strong><span>Previous project</span></a>
    <div class="mid"><span>{year}{escape(p["section_label"])}, {escape(p["type"])}</span></div>
    <a class="next" href="{nxt["slug"]}.html"><strong>{escape(nxt["title"])}</strong><span>Next project</span></a>
  </nav>
</main>
<div class="lightbox" role="dialog" aria-modal="true" aria-label="{escape(p["title"])}">
  <div class="bar"><span>{escape(p["title"])}</span><button type="button">Close</button></div>
  <div class="frame"></div>
</div>"""
    return page(p["title"], body, prefix=pre)


def build_about():
    portrait = (f'<img src="{C.PORTRAIT}" alt="Portrait of {escape(C.NAME)}">' if C.PORTRAIT
                else '<span class="empty">Add your photo</span>')
    bio = "".join(f"<p>{escape(t)}</p>" for t in C.ABOUT)
    row = lambda a, b_, c: f"<li><span>{escape(a)}</span><span>{escape(b_)}</span><span>{escape(c)}</span></li>"
    shown = "".join(row(c, r, y) for c, r, y, show in C.EXPERIENCE if show)
    hidden = "".join(row(c, r, y) for c, r, y, show in C.EXPERIENCE if not show)
    xp = f'<ul class="xp">{shown}</ul>'
    if hidden:
        xp += (f'<details class="more-xp"><summary><span class="when-closed">Show more</span>'
               f'<span class="when-open">Show less</span></summary><ul class="xp">{hidden}</ul></details>')
    edu = "".join(row(a, p, y) for a, p, y in C.EDUCATION)
    awards = "".join(row(a, p, y) for a, p, y in C.AWARDS)
    mentor = "".join(f"<li><span>{escape(m)}</span></li>" for m in C.MENTORSHIP)
    logos = "".join(f'<li><img src="{src}" alt="{escape(n)}"></li>' for n, src in C.LOGOS)
    hl = "".join(f"<li><span>{escape(h)}</span></li>" for h in C.HIGHLIGHTS)
    contact = [f'<a href="{C.LINKEDIN}">LinkedIn</a>', f'<a href="{C.DRIBBBLE}">Dribbble</a>']
    if C.EMAIL:
        contact.insert(0, f'<a href="mailto:{C.EMAIL}">{escape(C.EMAIL)}</a>')
    if C.RESUME:
        contact.append(f'<a href="{C.RESUME}">Résumé (PDF)</a>')
    body = f"""{header("about.html")}
<main>
  <section class="stage">
    <div>
      <ul class="logos" aria-label="Companies I've worked with">{logos}</ul>
      <h1 class="word">About</h1>
    </div>
    <div class="about-portrait">{portrait}</div>
  </section>
  <div class="story" style="padding-top:24px">
    <section><h2>Bio</h2><div class="body">{bio}</div></section>
    <section><h2>Experience</h2><div>{xp}</div></section>
    <section><h2>Awards and recognition</h2><div><ul class="xp">{awards}</ul><p class="note-sm">{escape(C.AWARDS_NOTE)}</p></div></section>
    <section><h2>Education and mentoring</h2><div><ul class="xp">{edu}</ul></div></section>
    <section><h2>Contact</h2><div class="body"><p>{"<br>".join(contact)}</p></div></section>
  </div>
</main>"""
    return page("About", body)


def main():
    (ROOT / "work").mkdir(exist_ok=True)
    for old in (ROOT / "work").glob("*.html"):
        old.unlink()
    files = {"index.html": build_home(), "about.html": build_about()}
    for s in SECTIONS:
        files[s[2]] = build_index(*s)
    for p in ALL.values():
        files[f"work/{p['slug']}.html"] = build_project(p)
    # old addresses keep working
    def redirect(to):
        return f'<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url={to}"><link rel="canonical" href="{to}"><a href="{to}">Moved here</a>'
    files["illustration.html"] = redirect("brand.html")
    files["graphic-design.html"] = redirect("brand.html")
    for slug, c in IN_CLIENT.items():
        files[f"work/{slug}.html"] = redirect(f"{c['slug']}.html")
    for name, html in files.items():
        (ROOT / name).write_text(html, encoding="utf-8")
    print(f"Built {len(files)} pages")


if __name__ == "__main__":
    main()
