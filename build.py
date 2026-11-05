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
IN_CLIENT = {slug: c for c in C.CLIENTS for _, slugs in c.get("groups", []) for slug in slugs}
for c in C.CLIENTS:
    # a client page's strip: its cover, its own gallery, then every grouped piece
    c["images"] = ([c["cover"]] if c.get("cover") else []) + \
        [g for g in c.get("gallery", []) if g != c.get("cover")] + \
        [PIECES[s]["images"][0] for _, slugs in c.get("groups", []) for s in slugs]
    c["images"] = list(dict.fromkeys(c["images"]))  # no image twice
    c.setdefault("videos", {})
    for _, slugs in c.get("groups", []):
        for slug in slugs:
            c["videos"].update(PIECES[slug].get("videos", {}))
SELECTED = [p for p in C.PIECES if p["slug"] not in IN_CLIENT and p["slug"] not in C.HIDDEN]
BRAND = C.CLIENTS + SELECTED

SECTIONS = [
    # key, nav label, page, projects, intro
    ("ux", "Product design", "ux.html", C.UX,
     "Case studies covering research, interaction design and the outcomes of shipped work."),
    ("brand", "Design + Branding", "brand.html", BRAND,
     "Brand systems, illustration and graphic design for restaurants, universities and personal projects."),
]
NAV = [("index.html", "Home")] + [(s[2], s[1]) for s in SECTIONS] + [("about.html", "About")]

# Tiles featured on the home page, after the UX case studies.
HOME_PICKS = ["hawkers", "hawkers-apparel", "ucf", "other-works", "hawkers-brunch", "project-hail-mary-patch", "kabuki-mask", "nice-buns-neon",
              "spicy-smile-neon-sign", "streets-of-asia"]

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


def palette_link(prefix):
    p = getattr(C, "PALETTE", "")
    return f'\n<link rel="stylesheet" href="{prefix}assets/palette-{p}.css">' if p else ""


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
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
{THEME_BOOT}
<link rel="stylesheet" href="{prefix}assets/styles.css?v={CSS_VER}">{palette_link(prefix)}
<link rel="icon" href="data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%22-4%20-35%20130.48%20130.48%22%3E%3Cg%20fill%3D%22none%22%20stroke%3D%22%23ffffff%22%20stroke-linejoin%3D%22round%22%20stroke-width%3D%227%22%3E%3Cpolyline%20points%3D%22.5%2043.04%20118.98%2043.04%20118.98%2030.62%203.5%2030.62%203.5%2018.48%20121.98%2018.48%22/%3E%3Cline%20x1%3D%22121.98%22%20y1%3D%2256.02%22%20x2%3D%2289.28%22%20y2%3D%2256.02%22/%3E%3Cline%20x1%3D%2277.59%22%20y1%3D%223.5%22%20x2%3D%2244.89%22%20y2%3D%223.5%22/%3E%3Cline%20x1%3D%2233.2%22%20y1%3D%2256.02%22%20x2%3D%22.5%22%20y2%3D%2256.02%22/%3E%3Cpolyline%20points%3D%22106.63%2056.02%2061.24%203.5%2015.85%2056.02%22/%3E%3C/g%3E%3C/svg%3E">
</head>"""


THEME_TOGGLE = (
    '<button class="theme-toggle" type="button" aria-label="Switch to dark mode">'
    '<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true">'
    '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/></svg>'
    '<svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg></button>')

# set the theme before the page paints (dark unless the visitor chose light), so there's no flash
THEME_BOOT = """<script>var t='dark';try{t=localStorage.getItem('theme')||t}catch(e){}document.documentElement.dataset.theme=t</script>"""


def header(current, prefix="", views=False):
    cur = ' aria-current="page"'
    links = "".join(f'<li><a href="{prefix}{h}"{cur if h == current else ""}>{l}</a></li>' for h, l in NAV)
    toggle = ('<div class="views" role="group" aria-label="Layout">'
              '<button type="button" data-set="list" aria-pressed="false">List</button>'
              '<button type="button" data-set="grid" aria-pressed="true">Grid</button></div>') if views else "<span></span>"
    return f"""<header class="top">
  <a class="brand" href="{prefix}index.html" aria-label="{escape(C.NAME)}, home">{LOGO}</a>
  {toggle}
  <div class="top-right">
    <nav aria-label="Main"><button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button>
    <ul class="links" id="menu">{links}</ul></nav>
    {THEME_TOGGLE}
  </div>
</header>"""


def project_header(p, prefix):
    return f"""<header class="top">
  <a class="brand" href="{prefix}index.html" aria-label="{escape(C.NAME)}, home">{LOGO}</a>
  <span></span>
  <div class="top-right"><a class="close" href="{prefix}{p['section_page']}">Close</a>{THEME_TOGGLE}</div>
</header>"""


def footer():
    links = [(C.LINKEDIN, "LinkedIn"), (C.DRIBBBLE, "Dribbble")]
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

  // Disney projects only: a trail of twinkling four-point stars spills off the cursor
  if (document.body.hasAttribute('data-sparkle') && matchMedia('(hover: hover) and (pointer: fine)').matches && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const cv = document.createElement('canvas'); cv.className = 'sparks'; cv.setAttribute('aria-hidden', 'true');
    document.body.appendChild(cv);
    const cx = cv.getContext('2d'), parts = [];
    let dpr = 1, raf = 0, lx = null, ly = null, last = 0, light = false;
    const PAL = { dark: ['206,176,255', '170,140,255', '160,196,255', '226,236,255'],
                  light: ['132,88,220', '160,110,240', '72,110,225', '96,140,240'] };
    const size = () => {
      dpr = Math.min(devicePixelRatio || 1, 2);
      cv.width = innerWidth * dpr; cv.height = innerHeight * dpr;
      cx.setTransform(dpr, 0, 0, dpr, 0, 0);
    };
    const readTheme = () => {
      const r = document.documentElement;
      light = (r.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'light';
    };
    size(); readTheme(); addEventListener('resize', size);
    new MutationObserver(readTheme).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
    // a classic storybook twinkle: four long points with pinched, curved sides
    const star = (x, y, r, rot) => {
      const w = r * 0.22;
      cx.save(); cx.translate(x, y); cx.rotate(rot); cx.beginPath(); cx.moveTo(0, -r);
      for (let i = 0; i < 4; i++) {
        cx.quadraticCurveTo(w * 0.35, -w * 0.35, r, 0);   // inner curve to the next point
        cx.rotate(Math.PI / 2);
      }
      cx.closePath(); cx.fill(); cx.restore();
    };
    const tick = t => {
      const dt = Math.min((t - (last || t)) / 1000, 0.05); last = t;
      cx.clearRect(0, 0, innerWidth, innerHeight);
      for (let i = parts.length - 1; i >= 0; i--) {
        const q = parts[i];
        q.life -= dt;
        if (q.life <= 0) { parts.splice(i, 1); continue; }
        q.vx *= 0.955; q.vy = q.vy * 0.955 + 26 * dt;
        q.x += q.vx * dt; q.y += q.vy * dt; q.rot += q.spin * dt;
        const k = q.life / q.max, tw = 0.65 + 0.35 * Math.sin(t / 1000 * q.tw + q.ph);
        const r = q.r * (k < 0.25 ? k / 0.25 : 1) * (0.55 + 0.45 * tw);
        cx.globalAlpha = Math.min(1, k * 1.6) * q.a;
        cx.fillStyle = `rgb(${q.c})`;
        if (!light) { cx.shadowColor = `rgba(${q.c},.9)`; cx.shadowBlur = r * 1.6; }
        if (q.dot) { cx.beginPath(); cx.arc(q.x, q.y, r * 0.28, 0, 6.283); cx.fill(); }
        else star(q.x, q.y, r, q.rot);
      }
      cx.globalAlpha = 1; cx.shadowBlur = 0;
      raf = parts.length ? requestAnimationFrame(tick) : (last = 0, 0);
    };
    addEventListener('pointermove', e => {
      const x = e.clientX, y = e.clientY;
      if (lx === null) { lx = x; ly = y; return; }
      const dx = x - lx, dy = y - ly, d = Math.hypot(dx, dy);
      lx = x; ly = y;
      if (d < 2) return;
      const n = Math.min(5, Math.ceil(d / 16)), pal = light ? PAL.light : PAL.dark;
      for (let i = 0; i < n && parts.length < 220; i++) {
        const f = Math.random(), dot = Math.random() < 0.45;
        const ang = Math.atan2(-dy, -dx) + (Math.random() - 0.5) * 2.4;
        const sp = 20 + Math.random() * 70 + Math.min(d, 50);
        const max = 0.8 + Math.random() * 1.0;
        parts.push({ x: x - dx * f, y: y - dy * f, vx: Math.cos(ang) * sp, vy: Math.sin(ang) * sp,
                     r: dot ? 5 + Math.random() * 4 : 4 + Math.random() * 7, rot: Math.random() * 0.6 - 0.3,
                     spin: (Math.random() - 0.5) * 2.5, tw: 6 + Math.random() * 10, ph: Math.random() * 6.3,
                     a: 0.7 + Math.random() * 0.3, c: pal[(Math.random() * pal.length) | 0], dot, life: max, max });
      }
      if (!raf) raf = requestAnimationFrame(tick);
    }, { passive: true });
    document.addEventListener('pointerleave', () => { lx = null; });
  }

  // light / dark toggle
  const tt = document.querySelector('.theme-toggle');
  if (tt) {
    const root = document.documentElement, sys = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme || (sys.matches ? 'dark' : 'light')) === 'dark';
    const label = () => tt.setAttribute('aria-label', isDark() ? 'Switch to light mode' : 'Switch to dark mode');
    tt.addEventListener('click', () => {
      const next = isDark() ? 'light' : 'dark';
      root.dataset.theme = next;
      try { localStorage.setItem('theme', next); } catch (e) {}
      label();
    });
    sys.addEventListener('change', label); label();
  }

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

  // box rails: mark which sides have more to scroll to, so the edges can fade
  document.querySelectorAll('.rail').forEach(r => {
    const wrap = r.parentElement;
    wrap.classList.toggle('spills', r.children.length > 3);
    const prev = wrap.querySelector('.rail-btn.prev'), next = wrap.querySelector('.rail-btn.next');
    const edges = () => {
      const max = r.scrollWidth - r.clientWidth;
      r.classList.toggle('fade-l', r.scrollLeft > 4);
      r.classList.toggle('fade-r', max > 4 && r.scrollLeft < max - 4);
      wrap.classList.toggle('scrolls', max > 4);
      if (prev) { prev.disabled = r.scrollLeft <= 4; next.disabled = r.scrollLeft >= max - 4; }
    };
    const step = dir => {
      const box = r.querySelector('li');
      const w = box ? box.getBoundingClientRect().width + 12 : r.clientWidth * .8;
      r.scrollBy({ left: dir * w, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
    };
    prev && prev.addEventListener('click', () => step(-1));
    next && next.addEventListener('click', () => step(1));
    r.addEventListener('scroll', edges, { passive: true }); addEventListener('resize', edges); edges();
  });

  // project strip: starts tall, shrinks as you scroll, then the text slides underneath
  const slot = document.querySelector('.gallery-slot'), strip = slot && slot.querySelector('.gallery-frame');
  if (strip) {
    // arrows: step one image at a time, hidden at either end
    const g = strip.querySelector('.gallery'), gp = strip.querySelector('.g-btn.prev'), gn = strip.querySelector('.g-btn.next');
    const ends = () => {
      const max = g.scrollWidth - g.clientWidth;
      gp.disabled = g.scrollLeft <= 4; gn.disabled = g.scrollLeft >= max - 4;
    };
    const go = dir => {
      const x = g.scrollLeft, kids = [...g.children].map(k => k.offsetLeft - g.offsetLeft);
      const to = dir > 0 ? kids.find(l => l > x + 4) : kids.filter(l => l < x - 4).pop();
      g.scrollTo({ left: to === undefined ? (dir > 0 ? g.scrollWidth : 0) : to,
                   behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
    };
    gp.addEventListener('click', () => go(-1)); gn.addEventListener('click', () => go(1));
    g.addEventListener('scroll', ends, { passive: true }); addEventListener('resize', ends); addEventListener('load', ends);
    // re-check whenever the strip or any image in it changes size (phones lay out late, images load lazily)
    if ('ResizeObserver' in window) { const ro = new ResizeObserver(ends); ro.observe(g); [...g.children].forEach(k => ro.observe(k)); }
    g.querySelectorAll('img, video').forEach(m => m.addEventListener(m.tagName === 'IMG' ? 'load' : 'loadedmetadata', ends));
    requestAnimationFrame(ends); setTimeout(ends, 300); ends();

    const wide = matchMedia('(min-width: 761px)');
    let ticking = false;
    const fit = () => {
      ticking = false;
      if (!wide.matches) { strip.style.height = ''; return; }
      const full = slot.offsetHeight, least = full * 34 / 62;
      strip.style.height = Math.max(least, full - scrollY) + 'px';
    };
    addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(fit); } }, { passive: true });
    addEventListener('resize', fit); wide.addEventListener('change', fit); fit();
  }

  // lightbox
  const lb = document.querySelector('.lightbox');
  if (lb) {
    const frame = lb.querySelector('.frame'), closeBtn = lb.querySelector('button');
    let last = null;
    const close = () => { lb.classList.remove('open'); frame.querySelector('.pic').innerHTML = ''; document.body.style.overflow = ''; last && last.focus(); };
    document.querySelectorAll('button.shot').forEach(b => b.addEventListener('click', () => {
      last = b;
      const m = b.querySelector('.phones, img, video').cloneNode(true);
      m.removeAttribute('loading'); m.removeAttribute('data-autoplay');
      const pic = frame.querySelector('.pic'), aside = frame.querySelector('.note-panel'), note = b.querySelector('.note');
      pic.innerHTML = ''; pic.appendChild(m);
      aside.innerHTML = note ? note.innerHTML : '';
      lb.classList.toggle('has-note', !!note);
      lb.querySelector('.bar span').textContent = note ? lb.getAttribute('aria-label') : (m.getAttribute('alt') || m.getAttribute('aria-label') || '');
      if (m.tagName === 'VIDEO' && !matchMedia('(prefers-reduced-motion: reduce)').matches) m.play().catch(() => {});
      lb.classList.add('open'); document.body.style.overflow = 'hidden'; closeBtn.focus();
    }));
    closeBtn.addEventListener('click', close);
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && lb.classList.contains('open')) close(); });
  }
})();
</script>"""


import hashlib as _h, pathlib as _p
# changes whenever styles.css changes, so phones never pair new pages with an old cached stylesheet
CSS_VER = _h.md5(_p.Path(__file__).with_name("assets").joinpath("styles.css").read_bytes()).hexdigest()[:8]

GALLERY_ARROW = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6" fill="none" stroke="currentColor" '
                 'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
GALLERY_NAV = (f'<button class="g-btn prev" type="button" aria-label="Previous image" disabled>{GALLERY_ARROW}</button>'
               f'<button class="g-btn next" type="button" aria-label="Next image">{GALLERY_ARROW}</button>')


# Adam's mark (from images/logo.svg), drawn in the ink colour
LOGO = ('<svg class="logo" viewBox="0 0 122.48 59.52" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" '
        'stroke-linejoin="round" stroke-width="7"><polyline points=".5 43.04 118.98 43.04 118.98 30.62 3.5 30.62 3.5 18.48 121.98 18.48"/>'
        '<line x1="121.98" y1="56.02" x2="89.28" y2="56.02"/><line x1="77.59" y1="3.5" x2="44.89" y2="3.5"/>'
        '<line x1="33.2" y1="56.02" x2=".5" y2="56.02"/><polyline points="106.63 56.02 61.24 3.5 15.85 56.02"/></g></svg>')

# SVG lens used by the header's liquid-glass backdrop
GLASS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <filter id="glass" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
    <feTurbulence type="fractalNoise" baseFrequency="0.006 0.035" numOctaves="2" seed="7" result="noise"/>
    <feGaussianBlur in="noise" stdDeviation="2" result="soft"/>
    <feDisplacementMap in="SourceGraphic" in2="soft" scale="14" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
</svg>"""


def page(title, body, prefix="", view=None, sparkle=False):
    attr = (f' data-view="{view}"' if view else "") + (" data-sparkle" if sparkle else "")
    return f"{head(title, prefix)}\n<body{attr}>\n{GLASS}\n{body}\n{footer()}\n{SCRIPT}\n</body>\n</html>\n"


GRID_MAX = 10  # 4 across the bottom, 4 above, 2 on top; the List view shows everything


def tiles(projects, prefix="", cols=4, stair=False):
    """stair=True: 4 tiles on the bottom row, 3 above, 2 on top, stepped up to the right."""
    out = []
    limit = 9 if stair else GRID_MAX
    for i, p in enumerate(projects[:limit]):
        inner = (f'<img src="{prefix}{p["images"][0]}" alt="" loading="lazy">' if p["images"]
                 else f'<span class="empty">{escape(p["title"])}</span>')
        out.append(f'<li style="--i:{i}"><a href="{prefix}work/{p["slug"]}.html">{inner}'
                   f'<span class="cap">{escape(p["title"])}<span>{escape(p["type"])}</span></span></a></li>')
    cls = "tiles tiles-stair" if stair else "tiles"
    return f'<ul class="{cls}" style="--cols:{4 if stair else cols}">{"".join(out)}</ul>'


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
        out.append(f'<a class="brick" href="{prefix}work/{p["slug"]}.html"><span class="pic">{pic}</span>'
                   f'<h3>{escape(p["title"])}</h3><p>{escape(p["type"])}</p></a>')
    return f'<div class="masonry switchable">{"".join(out)}</div>'


# ---------------------------------------------------------------- pages

def build_home():
    # the name with a 4-3-2 staircase of square tiles; no lists below
    # square tiles made for the home page: (project, image). Bottom row first, then middle, then top.
    picks = [("hawkers-brunch", "brunch"), ("disney-dark-mode", "disney-v2"), ("red-6-ar", "red-6-helmet"), ("hawkers-apparel", "apparel"),
             ("environmental-design", "branding"), ("other-works", "hail-mary"), ("ucf", "ucf"),
             ("hawkers", "hawkers-fox-mask"), ("hawkers", "year-of-the-pig")]
    files = {"brunch": "hawkers-brunch", "apparel": "hawkers-apparel", "branding": "hawkers-branding"}
    featured = [dict(ALL[slug], images=[f"images/home/{files.get(img, img)}.webp"]) for slug, img in picks if slug in ALL]
    first, last = C.NAME.split(" ", 1)
    body = f"""{header("index.html")}
<main>
  <section class="stage stage-home">
    <div>
      <p class="lede">{escape(C.INTRO)}</p>
      <h1 class="word long">{escape(first)}<br>{escape(last)}</h1>
    </div>
    {tiles(featured, stair=True)}
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



# the three boxes on the Brand page: (title, subtitle, link, cover image)
BRAND_BOXES = [  # (title, subtitle, link, cover, crop position)
    (c["title"], c["type"], f'work/{c["slug"]}.html',
     c.get("box_cover") or c.get("cover") or c["images"][0], c.get("crop", "center"))
    for c in C.CLIENTS
]


def rail(items, prefix=""):
    """Tall boxes to the right of the big word; scrolls sideways when there are more than fit."""
    out = []
    for t, sub, href, img, *pos in items:
        style = f' style="object-position:{pos[0]}"' if pos else ""
        pic = f'<img src="{prefix}{img}" alt=""{style} loading="lazy">' if img else '<span class="box-empty">Add a cover image</span>'
        out.append(f'<li><a class="box" href="{prefix}{href}">{pic}'
                   f'<span class="box-text"><strong>{escape(t)}</strong><span>{escape(sub)}</span></span></a></li>')
    arrow = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6" fill="none" stroke="currentColor" '
             'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    nav = ('<div class="rail-nav">'
           f'<button class="rail-btn prev" type="button" aria-label="Scroll projects left" disabled>{arrow}</button>'
           f'<button class="rail-btn next" type="button" aria-label="Scroll projects right">{arrow}</button></div>')
    return f'<div class="rail-wrap">{nav}<ul class="rail" tabindex="0" aria-label="Projects">{"".join(out)}</ul></div>'


def build_rail_page(label, pg, intro, items, h1=None):
    body = f"""{header(pg)}
<main>
  <section class="stage stage-rail">
    <div>
      <p class="lede">{escape(intro)}</p>
      <h1 class="word word-rail">{h1 or escape(label).replace(" ", "<br>")}</h1>
    </div>
    {rail(items)}
  </section>
</main>"""
    return page(label, body)


def build_brand(key, label, pg, projects, intro):
    return build_rail_page(label, pg, intro, BRAND_BOXES, h1="Design +<br>Branding").replace(
        'class="word word-rail"', 'class="word word-rail word-name"')


def build_ux(key, label, pg, projects, intro):
    items = [(p["title"], " · ".join(x for x in [p.get("client"), p.get("year")] if x) or p["type"],
              f'work/{p["slug"]}.html', p.get("box_cover") or (p["images"][0] if p["images"] else "")) for p in projects]
    return build_rail_page(label, pg, intro, items)


def build_project(p):
    pre = "../"
    if p in C.CLIENTS:
        projs = C.CLIENTS
    elif p in SELECTED:
        projs = SELECTED
    else:
        projs = next(s[3] for s in SECTIONS if s[0] == p["section"])
    i = projs.index(p)
    prev, nxt = projs[i - 1], projs[(i + 1) % len(projs)]

    # every image for the project sits in the strip at the top
    titles = {PIECES[s]["images"][0]: PIECES[s]["title"] for _, slugs in p.get("groups", []) for s in slugs}
    strip = [(src, titles.get(src, p["title"]), p.get("videos")) for src in p["images"]]

    def body_html(txt):
        """Paragraphs separated by blank lines; lines starting with "- " become a list."""
        out = ""
        for block in txt.split("\n\n"):
            lines = block.split("\n")
            if all(l.startswith("= ") and "|" in l for l in lines):
                # "= 3.1M | Media impressions" lines become big-number cards
                cards = "".join(f'<div class="stat stat-big"><span class="v">{escape(a.strip())}</span><span class="k">{escape(b.strip())}</span></div>'
                                for a, b in (l[2:].split("|", 1) for l in lines))
                out += f'<div class="stats stat-row">{cards}</div>'
            elif all(l.startswith("- ") for l in lines):
                out += "<ul>" + "".join(f"<li>{escape(l[2:])}</li>" for l in lines) + "</ul>"
            else:
                out += f"<p>{escape(block)}</p>"
        return out

    # the write-up shown beside an image when it's opened full screen
    notes = {src: tuple(n) for src, n in p.get("notes", {}).items()}
    for _, slugs in p.get("groups", []):
        for s in slugs:
            piece = PIECES[s]
            notes.setdefault(piece["images"][0], (piece["title"], piece.get("description") or piece["type"]))
    # any image without its own write-up shows the project's
    fallback = (p["title"], p.get("description") or p.get("summary") or p["type"])

    def note_html(src):
        title, txt = notes.get(src, fallback)
        return f'<span class="note" hidden><strong>{escape(title)}</strong>{body_html(txt)}</span>'

    shots = "".join(
        f'<button class="shot" type="button" aria-label="View {escape(notes.get(src, (alt,))[0])} larger">'
        f'{media(src, alt, vids, pre)}{note_html(src)}</button>'
        for src, alt, vids in strip
    ) or '<div class="empty">Add images for this project</div>'
    next_panel = (f'<a class="next-panel" href="{nxt["slug"]}.html">'
                  f'<div><strong>Next: {escape(nxt["title"])}</strong><span>{escape(nxt["type"])}</span>'
                  f'<svg class="arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15m-6-6 6 6-6 6" fill="none" '
                  f'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div></a>')

    if p["section"] != "ux":
        # graphic design pages always show all four facts; filler fills any gaps for now
        p = dict(p)
        hk = "hawkers" in p["slug"] or "Hawkers" in (p.get("client") or "") or IN_CLIENT.get(p["slug"], {}).get("slug", "").startswith("hawkers")
        ucf = "ucf" in p["slug"] or "Central Florida" in (p.get("client") or "") or IN_CLIENT.get(p["slug"], {}).get("slug") == "ucf"
        p["client"] = p.get("client") or ("Hawkers Asian Street Food" if hk else "University of Central Florida" if ucf else "Personal project")
        p["date"] = p.get("date") or p.get("year") or ("2018–2022" if hk else "2015–2018" if ucf else "2020")
        p["role"] = p.get("role") or ("Creative direction and design" if hk else "Graphic design" if ucf else "Illustration and design")
        p["result"] = p.get("result") or "Result coming soon"

    # the four facts, each in its own card: value up top, small mono label beneath
    def stat(label, value):
        return f'<div class="stat"><span class="v">{value}</span><span class="k">{label}</span></div>'
    left = ""
    if p.get("client"):
        client = escape(p["client"])
        if p.get("client_url"):
            client = f'<a class="ext" href="{p["client_url"]}" target="_blank" rel="noopener">{client}</a>'
        left += stat("Designed for", client)
    if p.get("date") or p.get("year"):
        left += stat("Date", escape(p.get("date") or p["year"]))
    if p.get("role"):
        left += stat("Role", escape(p["role"]))
    if p.get("result"):
        left += stat("Result", escape(p["result"]))
    eyebrow = f'<p class="eyebrow">{escape(p.get("type") or ("Product design" if p["section"] == "ux" else "Design + Branding"))}</p>'

    text = p.get("description") or p.get("summary") or ""
    desc = f"<p>{escape(text)}</p>" if text else '<p class="prompt">Add a short description of this project.</p>'

    facts = story = groups = ""
    if p.get("story"):
        sections = list(p["story"])
    elif p["section"] == "ux":
        sections = [(n, p.get("sections", {}).get(n, "") or None, pr) for n, pr in C.CASE_STUDY_PROMPTS.items()]
    elif p.get("groups") or p.get("gallery"):
        sections = [(n, p.get("sections", {}).get(n, "") or None, pr) for n, pr in C.BRAND_PROMPTS.items()]
    else:
        sections = []
    secs = ""
    for sec in sections:
        name, txt = sec[0], sec[1]
        inner = body_html(txt) if txt else f'<p class="prompt">{escape(sec[2])}</p>'
        secs += f'<section><h2>{escape(name)}</h2><div class="body">{inner}</div></section>'
    if secs:
        story = f'<div class="story work-story">{secs}</div>'

    year = (escape(p["year"]) + "<br>") if p.get("year") else ""
    pager = f"""<nav class="pager" aria-label="More projects">
    <a href="{prev["slug"]}.html"><strong>{escape(prev["title"])}</strong><span>Previous project</span></a>
    <a class="next" href="{nxt["slug"]}.html"><strong>{escape(nxt["title"])}</strong><span>Next project</span></a>
  </nav>"""
    lightbox = f"""<div class="lightbox" role="dialog" aria-modal="true" aria-label="{escape(p["title"])}">
  <div class="bar"><span>{escape(p["title"])}</span><button type="button">Close</button></div>
  <div class="frame"><div class="pic"></div><aside class="note-panel"></aside></div>
</div>"""

    if p["section"] == "ux":
        # product design: images on the left, the write-up for each on the right
        def shot(src, alt, vids):
            label = escape(notes.get(src, (alt,))[0])
            # very tall images (full-page captures) keep their full height; the rest fit the screen
            try:
                from PIL import Image
                w, h = Image.open(ROOT / src).size
                long = h / w > 2.2
            except Exception:
                long = False
            ph = p.get("phones")
            if ph and src == ph["src"]:
                # light and dark screens in phone frames, scrolling together, tab bars pinned (pure HTML/CSS, transparent)
                def phone(name, scr, tabs, cls, status, top):
                    return (f'<figure class="phone"><figcaption>{name}</figcaption><div class="screen-wrap"><div class="screen">'
                            f'<img class="scroll" src="{pre}{scr}" alt="">'
                            f'<img class="tabs {cls}" src="{pre}{tabs}" alt=""><span class="status-bg"></span><img class="status st-top" src="{pre}{top}" alt=""><img class="status st-scrolled" src="{pre}{status}" alt=""><span class="island"></span><span class="home-ind"></span>'
                            f'</div></div></figure>')
                inner = (f'<div class="phones" role="img" aria-label="Trip home screen in light and dark mode, scrolling side by side">'
                         f'{phone("Light", ph["light"], ph["tabs_light"], "tl", ph["status_light"], ph["status_light"])}{phone("Dark", ph["dark"], ph["tabs_dark"], "td", ph["status_dark"], ph["status_dark"])}</div>')
                return (f'<button class="shot phones-shot" type="button" aria-label="View {label} larger">{inner}{note_html(src)}</button>')
            return (f'<button class="shot{" long" if long else ""}" type="button" aria-label="View {label} larger">'
                    f'{media(src, alt, vids, pre)}{note_html(src)}</button>')
        rows = ""
        if strip:
            src, alt, vids = strip[0]
            rows += f"""<section class="cs-row cs-intro">
    <div class="cs-media">{shot(src, alt, vids)}</div>
    <div class="cs-text">
      <div class="cs-head">{eyebrow}<h1>{escape(p["title"])}</h1><div class="lead">{desc}</div></div>
      <div class="cs-meta stats">{left}</div>
      {story}
    </div>
  </section>"""
        for src, alt, vids in strip[1:]:
            title, txt = notes.get(src, fallback)
            rows += f"""<section class="cs-row">
    <div class="cs-media">{shot(src, alt, vids)}</div>
    <div class="cs-text"><h2>{escape(title)}</h2><div class="body">{body_html(txt)}</div></div>
  </section>"""
        body = f"""{project_header(p, pre)}
<main class="cs">
  {rows}
  {pager}
</main>
{lightbox}"""
        return page(p["title"], body, prefix=pre, sparkle=p.get("client", "").startswith("The Walt Disney") or p.get("slug", "").startswith("disney"))

    body = f"""{project_header(p, pre)}
<main>
  <div class="gallery-slot"><div class="gallery-frame"><div class="gallery">{shots}{next_panel}</div>{GALLERY_NAV}</div></div>
  <div class="info info-stack">
    <div class="cs-head">{eyebrow}<h1>{escape(p["title"])}</h1><div class="lead">{desc}</div></div>
    <div class="cs-meta stats">{left}</div>
  </div>
  {story}
  {groups}
  <nav class="pager" aria-label="More projects">
    <a href="{prev["slug"]}.html"><strong>{escape(prev["title"])}</strong><span>Previous project</span></a>
    <a class="next" href="{nxt["slug"]}.html"><strong>{escape(nxt["title"])}</strong><span>Next project</span></a>
  </nav>
</main>
<div class="lightbox" role="dialog" aria-modal="true" aria-label="{escape(p["title"])}">
  <div class="bar"><span>{escape(p["title"])}</span><button type="button">Close</button></div>
  <div class="frame"><div class="pic"></div><aside class="note-panel"></aside></div>
</div>"""
    return page(p["title"], body, prefix=pre, sparkle=p.get("client", "").startswith("The Walt Disney") or p.get("slug", "").startswith("disney"))


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
    hl = "".join(f"<li><span>{escape(h)}</span></li>" for h in C.HIGHLIGHTS)
    contact = [f'<a href="{C.LINKEDIN}">LinkedIn</a>', f'<a href="{C.DRIBBBLE}">Dribbble</a>']
    if C.EMAIL:
        contact.insert(0, f'<a href="mailto:{C.EMAIL}">{escape(C.EMAIL)}</a>')
    if C.RESUME:
        contact.append(f'<a href="{C.RESUME}">Résumé (PDF)</a>')
    body = f"""{header("about.html")}
<main>
  <section class="stage stage-about">
    <div>
      <p class="lede">{escape(C.TITLE)}<br>{escape(C.LOCATION)}</p>
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
        files[s[2]] = {"brand": build_brand, "ux": build_ux}.get(s[0], build_index)(*s)
    for p in ALL.values():
        files[f"work/{p['slug']}.html"] = build_project(p)
    # old addresses keep working
    def redirect(to):
        return f'<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url={to}"><link rel="canonical" href="{to}"><a href="{to}">Moved here</a>'
    files["illustration.html"] = redirect("brand.html")
    files["other-work.html"] = redirect("work/other-works.html")
    files["graphic-design.html"] = redirect("brand.html")
    for slug, c in IN_CLIENT.items():
        files[f"work/{slug}.html"] = redirect(f"{c['slug']}.html")
    for name, html in files.items():
        (ROOT / name).write_text(html, encoding="utf-8")
    print(f"Built {len(files)} pages")


if __name__ == "__main__":
    main()
