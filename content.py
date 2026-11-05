"""
All the words and pictures on the site live here.

Edit this file, then run `python3 build.py` to rebuild the pages.
- Images go in /images. List them in "images"; the first one is the cover.
- "videos" maps an image to a looping video that plays in its place.
- Empty fields ("") are simply left off the page.
"""

NAME = "Adam Smajstrla"
TITLE = "Creative Director & Product Design"
LOCATION = "Central Florida"
LINKEDIN = "https://www.linkedin.com/in/adam-smajstrla/"
DRIBBBLE = "https://dribbble.com/smaj"
EMAIL = "adamsmajstrla@gmail.com"      # add an email to show it on the site
RESUME = ""     # e.g. "files/adam-smajstrla-resume.pdf"
PORTRAIT = "images/adam-smajstrla.webp"

# Color palette trial. "vista" loads assets/palette-vista.css ("burgundy" the older trial);
# set to "" for the original black-and-white colors.
PALETTE = "vista"

INTRO = "Merging data, graphic design and creative storytelling to enhance the user experience."

ABOUT = [
    "I'm a visual problem solver: a creative director and product designer in Central Florida, currently a senior product designer at The Walt Disney Company.",
    "For 15 years I've designed across theme parks, hospitality, higher education, insurance and tech, from Disney's design systems to an award-winning restaurant brand at Hawkers.",
    "I pair intuition with research and data, and I give teams the structure to ship great work without losing a brand's personality.",
]
HIGHLIGHTS = [
    "Built the Hawkers website in house, saving about $50K in agency fees, and grew its traffic 500% over three years",
    "Produced the Hawkers 40-page brand guidelines, menus, packaging, interiors and murals",
    "Created new design systems for Asbestos.com that lifted many key search terms to the first or second Google result",
    "Designed and launched Red 6's website from concept to launch",
]
# (company, role, years, shown before "Show more")
EXPERIENCE = [
    ("The Walt Disney Company", "Senior Product Designer (contract)", "2026–now", True),
    ("The Palm Medspa + Wellness", "Director of Brand & Operations (consultant)", "2025–2026", True),
    ("The Walt Disney Company", "Product Designer, design systems", "2024–2025", True),
    ("Launch That (Asbestos.com)", "Senior Product Designer", "2023–2024", True),
    ("Red 6", "Senior Graphic and Web Designer", "2023", True),
    ("Hawkers Asian Street Food", "Creative Director", "2018–2022", True),
    ("University of Central Florida", "Graphic Designer", "2015–2018", True),
    ("American Integrity Insurance", "Graphic Design and Marketing", "2013–2015", False),
    ("Tower Hill Insurance Group", "Graphic Designer", "2012–2013", False),
    ("Reynolds and Reynolds", "Graphic Designer", "2011–2012", False),
]
# (award, project, year) — American Advertising Federation unless noted
AWARDS = [
    ("Central Florida Art Director of the Year", "American Advertising Federation", "2022"),
    ("Gold ADDY", "Gan Bei takeout bag", "2022"),
    ("Silver ADDY", "Hawkers brunch menu", "2022"),
    ("Silver ADDY", "Dumplings and Dragons mural", "2022"),
    ("Silver ADDY", "Hawkers 10th birthday campaign", "2022"),
    ("Best of Show, Out of Home", "Gan Bei mural", "2021"),
    ("Best Breadth of Work", "Hawkers Asian Street Food", "2021"),
    ("Gold ADDY", "Gan Bei mural", "2021"),
    ("Gold ADDY", "Hawkers noodle tiger shirt", "2021"),
    ("District Silver ADDY", "Gan Bei takeout bag", "2021"),
    ("Gold Circle of Excellence", "CASE", "2018"),
    ("5 Awards of Excellence", "UCDA", ""),
    ("40+ ADDY awards in total", "Hawkers, UCF and more", "2015–2022"),
]
AWARDS_NOTE = "ADDY: American Advertising Federation. CASE: Council for Advancement and Support of Education. UCDA: University and College Designers Association."
# (what, where, years)
EDUCATION = [
    ("MBA", "University of Central Florida", "2020"),
    ("BFA, Graphic Design", "University of Central Florida", "2011"),
    ("AIGA Mentor", "University of Central Florida", "2019–2023"),
]
MENTORSHIP = [
    "Led and developed an in-house team of designers, photographers and videographers at Hawkers, supporting 13 restaurants",
    "Hired and trained the team at The Palm Medspa + Wellness while building its brand and operations",
    "Contributed to Disney's shared design system, writing the patterns and guidelines other designers build from",
    "Directed campus photoshoots and collaborated with a 20-person creative team at UCF",
]

# Prompts shown on a case study until its section is written.
CASE_STUDY_PROMPTS = {
    "The problem": "What was broken or missing, for whom, and why it mattered to the business.",
    "Research": "What you learned and how: interviews, analytics, audits, competitive review.",
    "Process": "Key flows, wireframes and iterations. Show one decision you changed your mind on.",
    "The solution": "The final design and the reasoning behind its most important choices.",
    "Outcome": "Results with numbers where you have them, and what you'd do next.",
}

UX = [{'slug': 'disney-dark-mode',
  'title': 'Disney Parks – Dark Mode',
  'type': 'Product design and design systems',
  'client': 'The Walt Disney Company',
  'year': '2026',
  'date': '2026',
  'role': 'Senior Product Designer',
  'result_label': 'Components themed',
  'result': '60+',
  'summary': "Exploring a dark theme for Disney's parks app, built into the Vista design system so every "
             'screen and component can switch with its tokens.',
  'box_cover': 'images/disney/dark-mode-box-v2.webp',
  'images': ['images/disney/dark-mode-phones-v2.webp',
             'images/disney/dark-mode-components.webp',
             'images/disney/dark-mode-backgrounds.webp',
             'images/disney/dark-mode-checklist.png',
             'images/disney/dark-mode-alerts.png'],
  'story': [('The problem',
             'Guests use the parks app all day, often where a bright white screen gets in the way: at '
             'nighttime shows, in dark ride queues and late in the day on a low battery. The app had no '
             'dark theme.'),
            ('Why dark mode',
             '- Saves battery\n'
             '- Easier viewing at night\n'
             '- Less glare in dark rides and indoor queues'),
            ('The approach',
             'I built dark mode into the Vista design system so every component switches with tokens. Each '
             'component was reviewed side by side in light and dark, then the theme was tested on real '
             'parks app screens.'),
            ('Roadblocks',
             '- One "inverse" token was doing two jobs. I split it so text on brand colors stays white while '
             'true inverse surfaces flip in dark mode.\n'
             '- Brand colors could only get so light before white text lost contrast. I set a lightness limit so '
             'every brand fill still passes.\n'
             '- Toasts, disabled states, map pins and menus fell short on contrast in dark mode. Each was tuned '
             'until it read clearly.')],
  'notes': {'images/disney/dark-mode-components.webp': ['Every component, in both themes',
                                                      'Dark mode had to work on every single component, not '
                                                      'just whole screens. We ran each one through both themes '
                                                      'side by side: calendars, date pickers, dropdowns, '
                                                      'buttons, search, toggles, checkboxes and segmented '
                                                      'controls. For each, we checked that it still read '
                                                      'clearly, kept its contrast and behaved the same way, so '
                                                      'a selected date or an active toggle is just as obvious '
                                                      'at night as it is in daylight.'],
            'images/disney/dark-mode-backgrounds.webp': ['Finding the right background',
                                                      'A straight dark theme gets very dark, very fast, and '
                                                      'loses the lightness and brightness people expect from '
                                                      'Disney. To bring the whimsy and magic back, we tried a '
                                                      'range of backgrounds on the same Trip Plans screen, '
                                                      'from flat navy to soft gradients with hints of blue and '
                                                      'purple. The gradients kept the screen easy on the eyes '
                                                      'at night while still feeling like a Disney sky.'],
            'images/disney/dark-mode-checklist.png': ['Trip checklist',
                                                       'A dense, task-heavy screen. In dark mode, cards '
                                                       'separate from the background with lighter surfaces '
                                                       'instead of shadows, which disappear on dark '
                                                       'backgrounds.'],
            'images/disney/dark-mode-alerts.png': ['Alert components',
                                                   'Toasts and badges, light against dark. Status colors '
                                                   'become deep tinted fills, so success, warning, error and '
                                                   'info stay easy to tell apart without glowing in a dark '
                                                   'room, and every badge style keeps its meaning in both '
                                                   'themes.'],
            'images/disney/dark-mode-phones-v2.webp': ['Light and dark, side by side',
                                                    'The trip home screen in both themes, scrolling together '
                                                    'with the tab bar pinned, so you can compare how '
                                                    'surfaces, cards, type and brand colors carry over from '
                                                    'light to dark.']},
  'videos': {},
  'phones': {'src': 'images/disney/dark-mode-phones-v2.webp',
             'light': 'images/disney/screen-light.webp',
             'dark': 'images/disney/screen-dark.webp',
             'tabs_light': 'images/disney/tabs-light.webp',
             'tabs_dark': 'images/disney/tabs-dark.webp',
             'status_light': 'images/disney/status-dark-text.webp',
             'status_dark': 'images/disney/status-light-text.webp'}},
 {'slug': 'asbestos-com',
  'title': 'Asbestos.com homepage',
  'type': 'UX and web design',
  'client': 'Asbestos.com',
  'client_url': 'https://www.asbestos.com/',
  'year': '2024',
  'date': 'February 2024',
  'role': 'UX and web design',
  'result': 'Creating frictionless conversions',
  'summary': 'A homepage redesign to build trust, simplify navigation and use real imagery so visitors can '
             'picture themselves using the service.',
  'story': [('The problem',
             'Asbestos.com is a deep, knowledge-based resource, similar to WebMD or Wikipedia. For most of '
             'its audience, people 65 and older, the sheer amount of information can be overwhelming, and '
             'the site struggled to guide visitors to the content they needed.'),
            ('The solution',
             '- Clear trust signals near the top to build confidence quickly.\n'
             "- A more visible call to action for the free guide, the site's highest-converting element.\n"
             '- Entry points for patients, caregivers and medical professionals, so each group finds '
             'relevant content fast.\n'
             "- Better search, for information that doesn't live in the top navigation.")],
  'images': ['images/site/hero3.webp',
             'images/site/Before-and-After.webp',
             'images/site/on-screen-asbestos.webp',
             'images/site/homepage-3.webp',
             'images/site/nav-comp.webp',
             'images/site/homepage-2.webp',
             'images/site/homepage-6.webp',
             'images/site/video-5.webp',
             'images/site/full-homepage.webp'],
  'videos': {'images/site/homepage-3.webp': 'images/site/homepage-3.mp4',
             'images/site/nav-comp.webp': 'images/site/nav-comp.mp4',
             'images/site/video-5.webp': 'images/site/video-5.mp4'},
  'notes': {'images/site/Before-and-After.webp': ['Before and after',
                                                  'The old layout on the left, the new design on the right.\n'
                                                  '\n'
                                                  '- Blue reserved for calls to action.\n'
                                                  '- Custom video content in place of stock imagery.\n'
                                                  '- New components to guide visitors, below.'],
            'images/site/nav-comp.webp': ['New navigation component',
                                          '- More emphasis on search.\n'
                                          '- Most-visited pages grouped by audience.\n'
                                          '- Friendlier, more engaging heading copy.'],
            'images/site/homepage-2.webp': ['New comparison component',
                                            'Many visitors find a doctor or lawyer on Asbestos.com and '
                                            'contact them directly. The comparison tool shows the benefits '
                                            "of working with the site's patient advocates instead, which led "
                                            'to more case signings.'],
            'images/site/homepage-6.webp': ['Mobile mockups', 'The redesigned homepage on mobile.'],
            'images/site/video-5.webp': ['Mobile functionality',
                                         'The existing site was static, so I added motion to make the mobile '
                                         'experience more dynamic and engaging.'],
            'images/site/full-homepage.webp': ['Full page', 'The complete redesigned homepage.']}},
 {'slug': 'asbestos-com-back-page',
  'title': 'Asbestos.com back pages',
  'box_cover': 'images/site/asbestos-back-pages-box.webp',
  'type': 'UX and web design',
  'client': 'Asbestos.com',
  'client_url': 'https://www.asbestos.com/',
  'year': '2024',
  'date': 'July 2024',
  'role': 'UX and web design',
  'result': 'Conversions up 17%, Google ranking up 2 points on average',
  'summary': 'A new article template that puts more of the most important content above the fold without '
             'hurting design or readability.',
  'story': [('The problem',
             "- The layout couldn't fit all the content stakeholders wanted higher on the page.\n"
             "- Videos took up a lot of space and weren't getting much engagement.\n"
             "- The primary call to action wasn't as prominent as it could be.\n"
             '- The page felt flat and hard to read.'),
            ('The solution',
             '- More legible typography.\n'
             '- Stronger separation between the hero and the rest of the page.\n'
             '- A smaller video, with trust signals and authorship moved up.\n'
             '- A sticky side navigation that shows more content without distracting readers.\n'
             '- Higher contrast on the table of contents for easier navigation.')],
  'images': ['images/site/template-featured.webp',
             'images/site/before-after-ux-test.webp',
             'images/site/Full-template.webp',
             'images/site/before-and-after-1.webp',
             'images/site/Typography-Update-New-remix-1.webp',
             'images/site/mobile.webp',
             'images/site/pull-quote.webp'],
  'videos': {'images/site/Full-template.webp': 'images/site/Full-template.mp4',
             'images/site/Typography-Update-New-remix-1.webp': 'images/site/Typography-Update-New-remix-1.mp4'},
  'notes': {'images/site/before-after-ux-test.webp': ['Before and after',
                                                      'The old layout on the left, the new design on the '
                                                      'right.\n'
                                                      '\n'
                                                      '- Videos had a low click-through rate, so shrinking '
                                                      'them made the primary call to action more visible.\n'
                                                      '- A new dark header and a more visible fact-checked '
                                                      'box build trust.\n'
                                                      '- Related articles moved from the bottom of the page '
                                                      'to the sidebar.\n'
                                                      "- A table of contents bar that's easier to see."],
            'images/site/Full-template.webp': ['Sidebar',
                                               'The original template used a single column. A sticky side '
                                               'navigation fits more content above the fold, moves '
                                               'recommended reading higher, and keeps the call to action '
                                               'visible while reading. It also fixed an issue where the call '
                                               'to action overlapped text on some screen sizes.'],
            'images/site/before-and-after-1.webp': ['Profile pages',
                                                    'The old profile layout was cluttered and short on white '
                                                    'space. The new template moves key content above the '
                                                    'fold and uses collapsible sections to cut visual '
                                                    'noise.'],
            'images/site/Typography-Update-New-remix-1.webp': ['Sticky navigation',
                                                               'On the old template, readers had to scroll '
                                                               'back to the top to reach the main '
                                                               'navigation. The new navigation reappears as '
                                                               'you scroll up, and the updated table of '
                                                               'contents no longer gets lost '
                                                               'white-on-white.'],
            'images/site/mobile.webp': ['Mobile mockups', 'The new template on mobile.'],
            'images/site/pull-quote.webp': ['New pull quote style',
                                            'A more distinct pull quote style for highlighting key '
                                            'statements.']}},
 {'slug': 'red-6-ar',
  'title': 'Red 6 AR website',
  'type': 'Web design',
  'client': 'Red 6',
  'client_url': 'https://www.red6ar.com/',
  'year': '2023',
  'date': 'January 2023',
  'role': 'Web design and development',
  'result': '',
  'summary': 'A minimal, modern website for an augmented reality company that builds hardware and software '
             'for fighter pilot training.',
  'story': [('The problem',
             'Red 6 needed a minimal, modern website that would act as a visual gateway into its work. The '
             'challenge was to deliver a seamless experience while showcasing striking imagery of its '
             'technology.'),
            ('The solution',
             'I worked with Red 6 to build a site that pairs a sleek look with straightforward navigation. '
             "It reflects the company's forward-thinking culture and tells a clear story about its augmented "
             'reality products, turning complex technology into something visually striking and easy to '
             'follow.')],
  'images': ['images/site/Untitled-1.webp',
             'images/site/original-ae1aba409bcef10cc8902e2d34af971f.webp',
             'images/site/original-a848813faa7e65c0ed97d736165d2ad2.webp',
             'images/site/ATARS-Red-6.webp'],
  'videos': {'images/site/original-a848813faa7e65c0ed97d736165d2ad2.webp': 'images/site/original-a848813faa7e65c0ed97d736165d2ad2.mp4'},
  'notes': {'images/site/original-ae1aba409bcef10cc8902e2d34af971f.webp': ['Layout',
                                                                           'Dark colors, impactful imagery '
                                                                           'and video, and clear calls to '
                                                                           'action guided the design, from '
                                                                           'the homepage through the full '
                                                                           'product pages.'],
            'images/site/original-a848813faa7e65c0ed97d736165d2ad2.webp': ['Homepage',
                                                                           'The homepage hero, with video '
                                                                           'front and center.'],
            'images/site/ATARS-Red-6.webp': ['Full product page',
                                             'The ATARS product page from top to bottom.']}}]

# ---------------------------------------------------------------------------
# Brand section. Client pages group pieces (by slug from PIECES) under
# headings; selected work is everything shown as its own page.
# ---------------------------------------------------------------------------
BRAND_PROMPTS = {
    "The brief": "What the client needed and the problem the brand had to solve.",
    "My role": "What you owned: creative direction, illustration, design, production partners.",
    "The system": "How the pieces work together: mascot, type, color, voice, and where it shows up.",
}

CLIENTS = [{'slug': 'hawkers-brunch',
  'title': 'Hawkers brunch',
  'type': 'Brand campaign, menu and art direction',
  'client': 'Hawkers Asian Street Food',
  'year': '2022',
  'description': 'An original brunch brand for Hawkers, built from scratch and launched in six weeks. It reached over 6 million people and returned five times what it cost.',
  'cover': 'images/work/hawkers-brunch-cover.webp',
  'box_cover': 'images/work/hawkers-brunch-box.webp',
  'story': [('The idea',
             'Hawkers wanted more people through the door on weekend mornings. Instead of just adding a brunch menu, '
             'we gave brunch its own name, look and personality: a small brand that lives inside the bigger one.'),
            ('My role',
             'I came up with the concept and led it from first sketch to launch: the name and look, the menu, '
             'the photoshoot and everything people saw online.'),
            ('What we made',
             '- Printed brunch menus\n'
             '- Brunch pages on the Hawkers website\n'
             '- Augmented reality filters for Instagram\n'
             '- An interactive quiz to find your brunch order\n'
             '- Spotify playlists to set the mood\n'
             '- Email campaigns to bring guests in'),
            ('The results',
             'In just six weeks, the launch reached millions and paid for itself many times over.\n'
             '\n'
             '= 3.1M | Media impressions\n'
             '= 2.9M | Social impressions\n'
             '= 500% | Return on investment\n'
             '= 6 | Weeks from launch')],
  'groups': [],
  'gallery': ['images/site/brunch-social-grid.webp',
              'images/site/brunch-photo-hibiscus.webp',
              'images/site/brunch-menu.webp',
              'images/site/brunch-photo-butterfly.webp',
              'images/site/brunch-poster-basic.webp',
              'images/site/brunch-photo-pancakes.webp',
              'images/site/brunch-poster-rbf.webp',
              'images/site/brunch-photo-biscuits.webp',
              'images/site/brunch-poster-level-up.webp',
              'images/site/brunch-photo-mimosas.webp',
              'images/site/brunch-poster-dtb.webp',
              'images/site/brunch-photo-margarita.webp',
              'images/site/brunch-emails.webp'],
  'notes': {'images/site/brunch-social-grid.webp': ['Social campaign',
                                                    'A grid of social posts for the Brunch Better launch: '
                                                    'duotone halftone photography, oversized condensed type '
                                                    'and a tight palette of navy, yellow, lavender, green '
                                                    'and orange.'],
            'images/site/brunch-menu.webp': ['Brunch menu',
                                             'The brunch menu, front and back. Each dish gets its own color '
                                             'block and photo, with the Brunch Better cover carrying the '
                                             "campaign's halftone hands and outlined type."],
            'images/site/brunch-poster-basic.webp': ['No More Basic Brunches',
                                                     'A neighborhood poster from the campaign. Posters drove '
                                                     "sign-ups for email updates ahead of each city's "
                                                     'launch.'],
            'images/site/brunch-poster-rbf.webp': ['No More RBF',
                                                   'Resting brunch face, duh. A poster for bottomless '
                                                   'mimosas.'],
            'images/site/brunch-poster-level-up.webp': ['Level up. Squad up. Brunch up.',
                                                        'A campaign poster built around the halftone '
                                                        'hand-and-chopsticks motif.'],
            'images/site/brunch-poster-dtb.webp': ['DTB? Us too.',
                                                   'Down to brunch. A campaign poster pointing to '
                                                   'BrunchBetter.com.'],
            'images/site/brunch-emails.webp': ['Launch emails',
                                               'Emails announcing brunch by city, offering a free brunch to '
                                               'poster sign-ups, and sharing the launch date breakdown.'],
            'images/site/brunch-photo-hibiscus.webp': ['Hibiscus cooler',
                                                       'From the brunch photoshoot: each drink and dish shot '
                                                       'on a single bright color, styled with one playful '
                                                       'prop.'],
            'images/site/brunch-photo-butterfly.webp': ['Butterfly pea cocktail',
                                                        'From the brunch photoshoot.'],
            'images/site/brunch-photo-pancakes.webp': ['Pandan pancakes', 'From the brunch photoshoot.'],
            'images/site/brunch-photo-biscuits.webp': ['Korean fried chicken biscuits',
                                                       'From the brunch photoshoot.'],
            'images/site/brunch-photo-mimosas.webp': ['Bottomless mimosas', 'From the brunch photoshoot.'],
            'images/site/brunch-photo-margarita.webp': ['Brunch margarita', 'From the brunch photoshoot.']},
  'date': '2022',
  'result': '500% ROI in 6 weeks'},
 {'slug': 'hawkers',
  'title': 'Hawkers branding',
  'type': 'Brand identity and creative direction',
  'client': 'Hawkers Asian Street Food',
  'year': '2018–2022',
  'description': 'A brand system for a fast-growing Asian street food restaurant group, built to feel as '
                 'loud, warm and hand-made as the food, and to scale from 4 to 15 locations across the '
                 'country.',
  'sections': {'The brief': 'Hawkers started as a single Orlando restaurant serving the dishes its founders '
                            'grew up with at street stalls across Asia. As the group expanded, the brand had '
                            'to travel to new cities without losing the energy of the original: every '
                            'location needed to feel local and lived-in, not like a chain.\n'
                            '\n'
                            'The challenge was to build one system flexible enough for menus, packaging, '
                            'apparel, signage and full-wall murals, while giving each new restaurant its own '
                            'personality.',
               'My role': 'I joined as senior art director and later became creative director, leading an '
                          'in-house team of designers, photographers and videographers.\n'
                          '\n'
                          'I owned the brand end to end: the 40-page brand guidelines, the menu suite, '
                          'takeout packaging, uniforms and merch, neon signage and seasonal campaigns. I '
                          'also traveled to new locations to design and paint the murals myself.',
               'The system': 'The tiger mascot is the anchor. It shows up as a full illustration on murals '
                             'and Lunar New Year pieces, simplified on packaging, and as a single-line mark '
                             'on pins and caps. Around it sits a tight palette of tiger orange, deep green '
                             'and cream, a bold sans for headlines and hand lettering for moments that need '
                             'personality.\n'
                             '\n'
                             'Every year the zodiac animal becomes a new campaign, which keeps the brand '
                             'fresh while reinforcing the tiger. The work earned Central Florida Art '
                             'Director of the Year and a string of ADDY awards.'},
  'groups': [('Identity and mascot', ['japanese-hero-mask-lockup', 'lapel-pins']),
             ('Lunar New Year and anniversaries',
              ['happy-new-year-2020-year-of-the-rat', 'year-of-the-ox', 'luck-cat-anniversary-pin']),
             ('Menus and packaging',
              ['hawkers-takeout-bag',
               'hawkers-to-go-cup',
               'hawkers-beverage-coasters',
               'foo-dog-drink-coaster',
               'daruma-lucky-cat-drink-coaster']),
             ('Illustration',
              ['street-of-asia',
               'streets-of-asia',
               'asian-food-illustrations',
               'kabuki-mask',
               'fu-lion-playing-with-noodles',
               'happy-mother-s-day-nesting-dolls',
               'nom-com-movie-night',
               'cute-lucky-cat',
               'cocktails'])],
  'cover': 'images/site/hawkers-menu-suite.webp',
  'box_cover': 'images/site/hawkers-brandbook-box.webp',
  'gallery': ['images/site/hawkers-menu-suite.webp',
              'images/site/year-of-the-pig-2019.webp',
              'images/site/hawkers-doordash-send-noods.webp',
              'images/site/hawkers-brand-book.webp',
              'images/site/hawkers-business-cards.webp'],
  'notes': {'images/site/year-of-the-pig-2019.webp': ['Year of the Pig',
                                                      'Lunar New Year 2019 artwork: a hand-drawn pig riding '
                                                      'swirling clouds, finished with halftone texture in '
                                                      'red and gold.'],
            'images/site/hawkers-doordash-send-noods.webp': ['Send Noods Plz.',
                                                             'A Hawkers + DoorDash delivery campaign, built '
                                                             'around an illustrated plate of noodles and a '
                                                             'cheeky headline.'],
            'images/site/hawkers-brand-book.webp': ['Brand book',
                                                    'The cover of the Hawkers brand book, second edition: '
                                                    "Food. Service. Vibe. The guide covers the brand's "
                                                    'voice, photography, type, color and how they come '
                                                    'together across every location.'],
            'images/site/hawkers-business-cards.webp': ['Business cards',
                                                        'Business cards with a collage back built from the '
                                                        "brand's poster style, mascots and street-food "
                                                        'photography.'],
            'images/site/hawkers-menu-suite.webp': ['Menu suite',
                                                    'The full menu system: small plates, noodles and rice '
                                                    "with a hand-drawn map of the dishes' origins, craft "
                                                    'cocktails and saké, and happy hour inserts. Each menu '
                                                    'uses the same bold red and green type, halftone '
                                                    'photography and playful callouts.']}},
 {'slug': 'hawkers-apparel',
  'title': 'Hawkers apparel',
  'type': 'Apparel and merch design',
  'client': 'Hawkers Asian Street Food',
  'year': '2021',
  'date': '2018–2022',
  'role': 'Brand identity',
  'result': 'ADDY Award winner',
  'description': 'Shirts, masks, uniforms and merch designed for Hawkers Asian Street Food, from Lunar New '
                 'Year drops to charity collaborations.',
  'cover': 'images/site/Hawkers-Apparel.webp',
  'box_cover': 'images/site/hawkers-spice-shirt-photo.webp',
  'crop': '34% center',
  'gallery': ['images/site/Other-Illos.webp',
              'images/site/hawkers_14456072.webp',
              'images/site/Certified-Trainer-Shirt-Mockup-scaled.webp',
              'images/site/certified-trainer-artwork.webp',
              'images/site/certified-trainer-process.webp',
              'images/site/Dribbble-Mockup-2.webp',
              'images/site/Hawkers-Apparel.webp',
              'images/site/02-Mask-Mockup-Perspective-View2.webp',
              'images/site/Commissary-Uniform-Grid-Mock-up-01.webp',
              'images/site/b34ffe5b35e4c396d4f7445bf05cc38c.webp',
              'images/site/hawkers_80851540.webp',
              'images/site/Geisha.webp'],
  'story': [],
  'groups': [('More apparel', ['hawkers-tiger-trucker-cap', 'i-wanna-wok-hat-design'])],
  'notes': {'images/site/Other-Illos.webp': ['Year of the Tiger',
                                             'A Lunar New Year 2022 shirt. All proceeds went to Asian '
                                             'Americans Advancing Justice (AAJC).'],
            'images/site/Certified-Trainer-Shirt-Mockup-scaled.webp': ['Certified trainer shirt',
                                                                       'A shirt for Hawkers certified '
                                                                       'trainers.'],
            'images/site/Dribbble-Mockup-2.webp': ['Certified trainer shirt',
                                                   'The character artwork for the certified trainer shirt.'],
            'images/site/Hawkers-Apparel.webp': ['Certified trainer shirt',
                                                 'The shirt in use at a Hawkers restaurant.'],
            'images/site/02-Mask-Mockup-Perspective-View2.webp': ['Panda COVID mask',
                                                                  'A branded face mask for staff and '
                                                                  'guests.'],
            'images/site/Commissary-Uniform-Grid-Mock-up-01.webp': ["Feelin' saucy",
                                                                    'Merch and uniforms built around the '
                                                                    'Hawkers voice.'],
            'images/site/b34ffe5b35e4c396d4f7445bf05cc38c.webp': ['Noodle tiger',
                                                                  'Made for the Orlando Merch Store to raise '
                                                                  'money for charity and local businesses.'],
            'images/site/hawkers_80851540.webp': ['Spice shirt',
                                                  'Part of the Hawkers spice campaign, hand-dyed in '
                                                  'turmeric.'],
            'images/site/hawkers_14456072.webp': ['Seasoned perfectly',
                                                  'Another piece from the spice campaign.'],
            'images/site/Geisha.webp': ['Hawkers + DoorDash',
                                        'A T-shirt designed in partnership with DoorDash.'],
            'images/site/certified-trainer-artwork.webp': ['Certified trainer artwork',
                                                           'The full illustration for the Hawkers certified '
                                                           'trainer shirt: a masked trainer carrying a bowl '
                                                           'of dumplings, with one narrowly escaping the '
                                                           'chopsticks.'],
            'images/site/certified-trainer-process.webp': ['Certified trainer, in progress',
                                                           'A screen recording of the illustration coming '
                                                           'together in Illustrator, from line art to the '
                                                           'finished color piece.']},
  'videos': {'images/site/certified-trainer-process.webp': 'images/site/certified-trainer-process.mp4'}},
 {'slug': 'ucf',
  'title': 'UCF branding',
  'type': 'Editorial, admissions and print design',
  'client': 'University of Central Florida',
  'year': '2015–2018',
  'description': 'Three years of environmental graphics, admissions publications, Pegasus magazine editorial '
                 'and campus spirit work for the University of Central Florida.',
  'sections': {'The brief': '', 'My role': '', 'The system': ''},
  'groups': [('Admissions',
              ['ucf-viewbook',
               'ucf-viewbook-full-magazine',
               'ucf-big-is-editorial-spread',
               'ucf-book-cover-idea',
               'ucf-downtown-campus-spread',
               'be-a-part-of-something-big',
               'this-is-big-ucf-landing-page',
               'ucf-campaign-website-impact']),
             ('Pegasus magazine',
              ['all-the-buzz-honey-bee-editorial',
               'hand-drawn-flower-illustration',
               'drive-on-editorial-racing-story',
               'ucf-student-debt-infographic',
               'ucf-global-distribution-infographic',
               'pegasus-the-space-issue',
               'citronaut-spread-for-ucf-alumni-magazine',
               'space-shuttle-discovery',
               'international-space-station',
               'ucf-old-mascot-the-citronaut']),
             ('Spirit and merch',
              ['ucf-knights-sticker',
               'pegasus-sticker',
               'ucf-knights-lapel-pin-concept',
               'knightro-poster-charge-on',
               'laser-cut-wood-press-poster',
               'ucf-student-id-concept'])],
  'cover': 'images/work/ucf-cover.webp',
  'box_cover': 'images/site/ucf-pegasus-covers.webp',
  'crop': '52% center'},
 {'slug': 'environmental-design',
  'title': 'Environmental design',
  'type': 'Murals, neon, wall wraps and signage',
  'client': 'Hawkers Asian Street Food and UCF',
  'year': '2015–2022',
  'date': '2015–2022',
  'role': 'Environmental design and art direction',
  'result': 'Best of Show, Out of Home ADDY',
  'description': 'Spaces people walk into: hand-painted murals and custom neon for Hawkers restaurants, and '
                 'large-format wall wraps, vehicle wraps and billboards for UCF.',
  'cover': 'images/site/hawkers-neon-interior.webp',
  'box_cover': 'images/site/hawkers-neon-interior.webp',
  'crop': '37.9% center',
  'gallery': ['images/site/hawkers-interior-masks.webp',
              'images/site/gan-bei-neon-wall.webp',
              'images/site/gan-bei-garden-mural-photo.webp'],
  'notes': {'images/site/hawkers-interior-masks.webp': ['Restaurant interior',
                                                        'A Hawkers dining room: hand-painted mask mural, '
                                                        "custom neon and the brand's colors carried through "
                                                        'the space.'],
            'images/site/gan-bei-neon-wall.webp': ['Gan Bei neon wall',
                                                   'The bar at Gan Bei, layered with poster collage and '
                                                   'custom neon signs, including the Gan Bei bicycle mark.'],
            'images/site/gan-bei-garden-mural-photo.webp': ['Gan Bei Garden mural',
                                                            'The finished Gan Bei Garden mural, painted on '
                                                            'site, a busy street scene of diners, shops and '
                                                            'lanterns.'],
            'images/site/hawkers-neon-interior.webp': ['Hawkers neon interior',
                                                       'Neon, signage and poster collage layered through a '
                                                       'Hawkers dining room.']},
  'sections': {'The brief': '', 'My role': '', 'The system': ''},
  'groups': [('Hawkers murals', ['gan-bei-garden-mural', 'dumplings-and-dragons-mural', 'custom-neons']),
             ('Hawkers neon signs',
              ['spicy-smile-neon-sign',
               'nice-buns-neon',
               'neon-cocktails',
               'drink-like-a-fish-neon-sign',
               'asian-neon-masks',
               'nom-neon',
               'lucky-cat-stamp-neon',
               'the-great-wave-neon']),
             ('UCF wall wraps and outdoor',
              ['ucf-mba-downtown-wall-wrap',
               'ucf-champions-wall-wrap',
               'ucf-wall-wrap',
               'ucf-wall-wrap-mural',
               'big-dreams-orlando-airport-wallwrap',
               'orlando-downtown-wall-wrap',
               'ucf-marketing-wall-wrap',
               'bus-wrap',
               'ucf-vs-auburn-chick-fil-a-peach-bowl-billboard'])]},
 {'slug': 'other-works',
  'title': 'Other works',
  'type': 'Illustration and identity',
  'client': '',
  'year': '',
  'description': 'Patches, logos and illustration for clients and personal projects outside of Hawkers and '
                 'UCF.',
  'cover': 'images/work/project-hail-mary-patch.webp',
  'box_cover': 'images/work/other-works-box.webp',
  'sections': {'The brief': '', 'My role': '', 'The system': ''},
  'groups': [('Selected pieces',
              ['project-hail-mary-patch', 'ghost-chicken', 'main-street-bridge', 'hutch-studio-logo'])]}]

# Pieces covered by a client page in another form, kept off Other work
HIDDEN = ['hawkers-noodle-tiger-shirt', 'hero-trainer-shirt']

# Every individual piece. Pieces used in a client page above don't get their own page.
PIECES = [{'slug': 'project-hail-mary-patch',
  'title': 'Project Hail Mary patch',
  'type': 'Patch',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/project-hail-mary-patch.webp']},
 {'slug': 'gan-bei-garden-mural',
  'title': 'Gan Bei garden mural',
  'type': 'Mural',
  'client': 'Gan Bei',
  'year': '',
  'description': '',
  'images': ['images/work/gan-bei-garden-mural.webp']},
 {'slug': 'japanese-hero-mask-lockup',
  'title': 'Japanese hero mask lockup',
  'type': 'Lettering',
  'client': '',
  'year': '',
  'description': 'A kabuki mask and kanji lettering, designed for the front of the Certified Trainer T-shirt.',
  'images': ['images/work/japanese-hero-mask-lockup.webp']},
 {'slug': 'hero-trainer-shirt',
  'title': 'Hero trainer shirt',
  'type': 'Apparel',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/hero-trainer-shirt.webp']},
 {'slug': 'dumplings-and-dragons-mural',
  'title': 'Dumplings and Dragons mural',
  'type': 'Mural',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/dumplings-and-dragons-mural.webp']},
 {'slug': 'year-of-the-ox',
  'title': 'Year of the Ox',
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': 'A Happy Lunar New Year card for 2021, given to guests to keep or send as a postcard.',
  'images': ['images/work/year-of-the-ox.webp']},
 {'slug': 'kabuki-mask',
  'title': 'Kabuki mask',
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/kabuki-mask.webp']},
 {'slug': 'happy-mother-s-day-nesting-dolls',
  'title': "Mother's Day nesting dolls",
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': "An illustration created for Hawkers' Mother's Day social media graphics.",
  'images': ['images/work/happy-mother-s-day-nesting-dolls.webp'],
  'videos': {'images/work/happy-mother-s-day-nesting-dolls.webp': 'images/work/happy-mother-s-day-nesting-dolls.mp4'}},
 {'slug': 'cute-lucky-cat',
  'title': 'Lucky cat',
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/cute-lucky-cat.webp']},
 {'slug': 'hawkers-noodle-tiger-shirt',
  'title': 'Hawkers noodle tiger shirt',
  'type': 'Apparel',
  'client': 'Hawkers',
  'year': '',
  'description': '',
  'images': ['images/work/hawkers-noodle-tiger-shirt.webp']},
 {'slug': 'nom-com-movie-night',
  'title': 'Nom Com movie night',
  'type': 'Illustration',
  'client': 'Nom Com',
  'year': '',
  'description': 'An animated illustration for the social media graphics promoting a Hawkers movie night event.',
  'images': ['images/work/nom-com-movie-night.webp'],
  'videos': {'images/work/nom-com-movie-night.webp': 'images/work/nom-com-movie-night.mp4'}},
 {'slug': 'happy-new-year-2020-year-of-the-rat',
  'title': 'Year of the Rat',
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': 'A custom money envelope, made for Lunar New Year 2020 and handed out to guests.',
  'images': ['images/work/happy-new-year-2020-year-of-the-rat.webp']},
 {'slug': 'streets-of-asia',
  'title': 'Streets of Asia',
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': 'The original hand-drawn illustration created for the menus.',
  'images': ['images/work/streets-of-asia.webp']},
 {'slug': 'asian-food-illustrations',
  'title': 'Asian food illustrations',
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': 'Hand-drawn illustrations of dishes from the menu, used in an early version of the dining menu.',
  'images': ['images/work/asian-food-illustrations.webp']},
 {'slug': 'street-of-asia',
  'title': 'Street of Asia',
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': 'An unused illustration created for the menus.',
  'images': ['images/work/street-of-asia.webp']},
 {'slug': 'main-street-bridge',
  'title': 'Main Street Bridge',
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/main-street-bridge.webp']},
 {'slug': 'fu-lion-playing-with-noodles',
  'title': 'Fu lion with noodles',
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': 'A hand-drawn foo dog playing with a ball of yarn, planned as a mural for the corporate office.',
  'images': ['images/work/fu-lion-playing-with-noodles.webp']},
 {'slug': 'ucf-mba-downtown-wall-wrap',
  'title': 'UCF MBA downtown wall wrap',
  'type': 'Environmental graphics',
  'client': 'UCF',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-mba-downtown-wall-wrap.webp']},
 {'slug': 'hawkers-takeout-bag',
  'title': 'Hawkers takeout bag',
  'type': 'Packaging',
  'client': 'Hawkers',
  'year': '',
  'description': 'Hand-drawn illustrations for the Hawkers takeout bag, printed in three colors.',
  'images': ['images/work/hawkers-takeout-bag.webp']},
 {'slug': 'hawkers-beverage-coasters',
  'title': 'Hawkers beverage coasters',
  'type': 'Coaster',
  'client': 'Hawkers',
  'year': '',
  'description': "A series of four coasters, each representing a different part of Asia and tied to that region's heritage. Printed in three colors.",
  'images': ['images/work/hawkers-beverage-coasters.webp']},
 {'slug': 'spicy-smile-neon-sign',
  'title': 'Spicy Smile neon sign',
  'type': 'Neon sign',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/spicy-smile-neon-sign.webp']},
 {'slug': 'foo-dog-drink-coaster',
  'title': 'Foo dog drink coaster',
  'type': 'Coaster',
  'client': '',
  'year': '',
  'description': '“What foes around comes around”: drink coaster art featuring two foo dogs in a halftone pattern.',
  'images': ['images/work/foo-dog-drink-coaster.webp']},
 {'slug': 'nice-buns-neon',
  'title': 'Nice Buns neon',
  'type': 'Neon sign',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/nice-buns-neon.webp']},
 {'slug': 'daruma-lucky-cat-drink-coaster',
  'title': 'Daruma lucky cat coaster',
  'type': 'Coaster',
  'client': '',
  'year': '',
  'description': "“Who says wishes can't come true?” Drink coaster art designed as a working daruma doll: guests color in the eyes to make a wish.",
  'images': ['images/work/daruma-lucky-cat-drink-coaster.webp']},
 {'slug': 'asian-neon-masks',
  'title': 'Asian neon masks',
  'type': 'Neon sign',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/asian-neon-masks.webp']},
 {'slug': 'hutch-studio-logo',
  'title': 'Hutch Studio logo',
  'type': 'Logo',
  'client': 'Hutch Studio',
  'year': '',
  'description': '',
  'images': ['images/work/hutch-studio-logo.webp']},
 {'slug': 'luck-cat-anniversary-pin',
  'title': 'Lucky cat anniversary pin',
  'type': 'Enamel pin',
  'client': '',
  'year': '',
  'description': 'One of a set of five anniversary pins for staff; this one marks eight years. Every pin shares the same lucky cat, with more embellishment added as the years go on.',
  'images': ['images/work/luck-cat-anniversary-pin.webp']},
 {'slug': 'ghost-chicken',
  'title': 'Ghost Chicken logo',
  'type': 'Logo',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/ghost-chicken.webp']},
 {'slug': 'i-wanna-wok-hat-design',
  'title': 'I Wanna Wok hat',
  'type': 'Apparel',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/i-wanna-wok-hat-design.webp']},
 {'slug': 'cocktails',
  'title': 'Cocktail icons',
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/cocktails.webp']},
 {'slug': 'neon-cocktails',
  'title': 'Neon cocktails',
  'type': 'Neon sign',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/neon-cocktails.webp']},
 {'slug': 'drink-like-a-fish-neon-sign',
  'title': 'Drink Like a Fish neon sign',
  'type': 'Neon sign',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/drink-like-a-fish-neon-sign.webp']},
 {'slug': 'lapel-pins',
  'title': 'Lapel pins',
  'type': 'Enamel pin',
  'client': '',
  'year': '',
  'description': 'A set of enamel pins for the service staff. Each time someone completed training on a station in the restaurant, they earned a new pin.',
  'images': ['images/work/lapel-pins.webp']},
 {'slug': 'hawkers-to-go-cup',
  'title': 'Hawkers to-go cup',
  'type': 'Packaging',
  'client': 'Hawkers',
  'year': '',
  'description': 'A to-go cup designed to look like a street lamp post, bringing the Streets of Asia feel to every drink.',
  'images': ['images/work/hawkers-to-go-cup.webp']},
 {'slug': 'hawkers-tiger-trucker-cap',
  'title': 'Hawkers tiger trucker cap',
  'type': 'Apparel',
  'client': 'Hawkers',
  'year': '',
  'description': '',
  'images': ['images/work/hawkers-tiger-trucker-cap.webp']},
 {'slug': 'nom-neon',
  'title': 'Nom neon',
  'type': 'Neon sign',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/nom-neon.webp']},
 {'slug': 'lucky-cat-stamp-neon',
  'title': 'Lucky cat stamp neon',
  'type': 'Neon sign',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/lucky-cat-stamp-neon.webp']},
 {'slug': 'the-great-wave-neon',
  'title': 'The Great Wave neon',
  'type': 'Neon sign',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/the-great-wave-neon.webp']},
 {'slug': 'custom-neons',
  'title': 'Custom neons',
  'type': 'Neon sign',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/custom-neons.webp']},
 {'slug': 'ucf-champions-wall-wrap',
  'title': 'UCF Champions wall wrap',
  'type': 'Environmental graphics',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-champions-wall-wrap.webp']},
 {'slug': 'ucf-wall-wrap',
  'title': 'Millican Hall wall wrap',
  'type': 'Environmental graphics',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-wall-wrap.webp']},
 {'slug': 'ucf-wall-wrap-mural',
  'title': 'Millican Hall wall wrap install',
  'type': 'Environmental graphics',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-wall-wrap-mural.webp']},
 {'slug': 'big-dreams-orlando-airport-wallwrap',
  'title': 'Big Dreams airport wall wrap',
  'type': 'Environmental graphics',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/big-dreams-orlando-airport-wallwrap.webp']},
 {'slug': 'orlando-downtown-wall-wrap',
  'title': 'Orlando downtown wall wrap',
  'type': 'Environmental graphics',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/orlando-downtown-wall-wrap.webp']},
 {'slug': 'ucf-marketing-wall-wrap',
  'title': 'UCF Marketing wall wrap',
  'type': 'Environmental graphics',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-marketing-wall-wrap.webp']},
 {'slug': 'bus-wrap',
  'title': 'UCF Cares bus wrap',
  'type': 'Vehicle wrap',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/bus-wrap.webp']},
 {'slug': 'ucf-vs-auburn-chick-fil-a-peach-bowl-billboard',
  'title': 'Peach Bowl billboard',
  'type': 'Outdoor advertising',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-vs-auburn-chick-fil-a-peach-bowl-billboard.webp']},
 {'slug': 'ucf-viewbook',
  'title': 'This Is Big viewbook',
  'type': 'Admissions publication',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-viewbook.webp']},
 {'slug': 'ucf-viewbook-full-magazine',
  'title': 'This Is Big viewbook spreads',
  'type': 'Admissions publication',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-viewbook-full-magazine.webp']},
 {'slug': 'ucf-big-is-editorial-spread',
  'title': 'Big Is spread',
  'type': 'Admissions publication',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-big-is-editorial-spread.webp']},
 {'slug': 'ucf-book-cover-idea',
  'title': 'Viewbook cover concept',
  'type': 'Admissions publication',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-book-cover-idea.webp']},
 {'slug': 'ucf-downtown-campus-spread',
  'title': 'Downtown campus spread',
  'type': 'Admissions publication',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-downtown-campus-spread.webp']},
 {'slug': 'be-a-part-of-something-big',
  'title': 'Be a part of something big mailer',
  'type': 'Admissions mailer',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/be-a-part-of-something-big.webp']},
 {'slug': 'this-is-big-ucf-landing-page',
  'title': 'This Is Big landing page',
  'type': 'Web design',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/this-is-big-ucf-landing-page.webp']},
 {'slug': 'ucf-campaign-website-impact',
  'title': 'Impact campaign website',
  'type': 'Web design',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-campaign-website-impact.webp']},
 {'slug': 'all-the-buzz-honey-bee-editorial',
  'title': 'All the Buzz',
  'type': 'Pegasus magazine editorial',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/all-the-buzz-honey-bee-editorial.webp']},
 {'slug': 'hand-drawn-flower-illustration',
  'title': 'All the Buzz flower illustration',
  'type': 'Illustration',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/hand-drawn-flower-illustration.webp']},
 {'slug': 'drive-on-editorial-racing-story',
  'title': 'Drive On',
  'type': 'Pegasus magazine editorial',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/drive-on-editorial-racing-story.webp']},
 {'slug': 'ucf-student-debt-infographic',
  'title': 'Breaking Down Debt',
  'type': 'Editorial infographic',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-student-debt-infographic.webp']},
 {'slug': 'ucf-global-distribution-infographic',
  'title': 'Global Distribution',
  'type': 'Editorial infographic',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-global-distribution-infographic.webp']},
 {'slug': 'pegasus-the-space-issue',
  'title': 'One Small Step: the space issue',
  'type': 'Pegasus magazine editorial',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/pegasus-the-space-issue.webp']},
 {'slug': 'citronaut-spread-for-ucf-alumni-magazine',
  'title': 'Citronaut spread',
  'type': 'Pegasus magazine editorial',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/citronaut-spread-for-ucf-alumni-magazine.webp']},
 {'slug': 'space-shuttle-discovery',
  'title': 'Space Shuttle Discovery',
  'type': 'Illustration',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/space-shuttle-discovery.webp']},
 {'slug': 'international-space-station',
  'title': 'International Space Station',
  'type': 'Illustration',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/international-space-station.webp']},
 {'slug': 'ucf-old-mascot-the-citronaut',
  'title': 'The Citronaut',
  'type': 'Character illustration',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-old-mascot-the-citronaut.webp']},
 {'slug': 'ucf-knights-sticker',
  'title': 'Charge On sticker',
  'type': 'Sticker',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-knights-sticker.webp']},
 {'slug': 'pegasus-sticker',
  'title': 'Pegasus sticker',
  'type': 'Sticker',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/pegasus-sticker.webp']},
 {'slug': 'ucf-knights-lapel-pin-concept',
  'title': 'Knights lapel pin',
  'type': 'Enamel pin concept',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-knights-lapel-pin-concept.webp']},
 {'slug': 'knightro-poster-charge-on',
  'title': 'Charge On poster',
  'type': 'Poster',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/knightro-poster-charge-on.webp']},
 {'slug': 'laser-cut-wood-press-poster',
  'title': 'Charge On letterpress',
  'type': 'Letterpress print',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/laser-cut-wood-press-poster.webp']},
 {'slug': 'ucf-student-id-concept',
  'title': 'Student ID concept',
  'type': 'Identity design',
  'client': 'University of Central Florida',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-student-id-concept.webp']}]
