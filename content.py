"""
All the words and pictures on the site live here.

Edit this file, then run `python3 build.py` to rebuild the pages.
- Images go in /images. List them in "images"; the first one is the cover.
- "videos" maps an image to a looping video that plays in its place.
- Empty fields ("") are simply left off the page.
"""

NAME = "Adam Smajstrla"
TITLE = "Creative Director & Product Design"
LOCATION = "Orlando, FL"
LINKEDIN = "https://www.linkedin.com/in/adam-smajstrla/"
DRIBBBLE = "https://dribbble.com/smaj"
EMAIL = ""      # add an email to show it on the site
RESUME = ""     # e.g. "files/adam-smajstrla-resume.pdf"
PORTRAIT = "images/adam-smajstrla.webp"

INTRO = "Merging data, graphic design and creative storytelling to enhance the user experience."

ABOUT = [
    "I'm a visual problem solver: a creative director and product designer in Orlando, currently a senior product designer at The Walt Disney Company.",
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

UX = [{'slug': 'asbestos-com',
  'title': 'Asbestos.com homepage refresh',
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
  'title': 'Asbestos.com back page template',
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
  'type': 'Menu, photography and art direction',
  'client': 'Hawkers Asian Street Food',
  'year': '',
  'description': '',
  'cover': 'images/work/hawkers-brunch-cover.webp',
  'box_cover': 'images/work/hawkers-brunch-box.webp',
  'sections': {'The brief': '', 'My role': '', 'The system': ''},
  'groups': [('Menu', ['hawkers-brunch-menu']), ('Photography', ['brunch-photoshoot'])]},
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
  'groups': [('Identity and mascot', ['hawkers-tiger', 'japanese-hero-mask-lockup', 'lapel-pins']),
             ('Lunar New Year and anniversaries',
              ['lunar-new-year-year-of-the-tiger',
               'happy-new-year-2020-year-of-the-rat',
               'year-of-the-ox',
               'luck-cat-anniversary-pin']),
             ('Menus and packaging',
              ['hawkers-takeout-bag',
               'hawkers-to-go-cup',
               'hawkers-beverage-coasters',
               'foo-dog-drink-coaster',
               'daruma-lucky-cat-drink-coaster']),
             ('Murals and signage', ['gan-bei-garden-mural', 'dumplings-and-dragons-mural', 'custom-neons'])],
  'cover': 'images/work/hawkers-tiger-cover.webp',
  'crop': 'right center'},
 {'slug': 'hawkers-apparel',
  'title': 'Hawkers apparel',
  'type': 'Apparel and merch design',
  'client': 'Hawkers Asian Street Food',
  'year': '2021',
  'date': 'October 2021',
  'role': 'Brand identity',
  'result': 'ADDY Award winner',
  'description': 'Shirts, masks, uniforms and merch designed for Hawkers Asian Street Food, from Lunar New '
                 'Year drops to charity collaborations.',
  'cover': 'images/site/Hawkers-Apparel.webp',
  'gallery': ['images/site/Other-Illos.webp',
              'images/site/Certified-Trainer-Shirt-Mockup-scaled.webp',
              'images/site/Dribbble-Mockup-2.webp',
              'images/site/Hawkers-Apparel.webp',
              'images/site/02-Mask-Mockup-Perspective-View2.webp',
              'images/site/Commissary-Uniform-Grid-Mock-up-01.webp',
              'images/site/b34ffe5b35e4c396d4f7445bf05cc38c.webp',
              'images/site/hawkers_80851540.webp',
              'images/site/hawkers_14456072.webp',
              'images/site/Geisha.webp'],
  'story': [],
  'groups': [('More apparel', ['hawkers-tiger-trucker-cap'])],
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
                                        'A T-shirt designed in partnership with DoorDash.']}},
 {'slug': 'ucf',
  'title': 'UCF branding',
  'type': 'Environmental and print design',
  'client': 'University of Central Florida',
  'year': '2015–2018',
  'description': '',
  'sections': {'The brief': '', 'My role': '', 'The system': ''},
  'groups': [('Environmental graphics', ['ucf-mba-downtown-wall-wrap'])],
  'cover': 'images/work/ucf-cover.webp',
  'box_cover': 'images/work/ucf-box.webp'}]

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
  'description': '',
  'images': ['images/work/japanese-hero-mask-lockup.webp']},
 {'slug': 'hero-trainer-shirt',
  'title': 'Hero trainer shirt',
  'type': 'Apparel',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/hero-trainer-shirt.webp']},
 {'slug': 'lunar-new-year-year-of-the-tiger',
  'title': 'Year of the Tiger',
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/lunar-new-year-year-of-the-tiger.webp']},
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
  'description': '',
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
  'description': '',
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
  'description': '',
  'images': ['images/work/nom-com-movie-night.webp'],
  'videos': {'images/work/nom-com-movie-night.webp': 'images/work/nom-com-movie-night.mp4'}},
 {'slug': 'happy-new-year-2020-year-of-the-rat',
  'title': 'Year of the Rat',
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/happy-new-year-2020-year-of-the-rat.webp']},
 {'slug': 'geisha-and-koi',
  'title': 'Geisha and koi',
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/geisha-and-koi.webp']},
 {'slug': 'streets-of-asia',
  'title': 'Streets of Asia',
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/streets-of-asia.webp']},
 {'slug': 'asian-food-illustrations',
  'title': 'Asian food illustrations',
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/asian-food-illustrations.webp']},
 {'slug': 'street-of-asia',
  'title': 'Street of Asia',
  'type': 'Illustration',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/street-of-asia.webp']},
 {'slug': 'hawkers-tiger',
  'title': 'Hawkers tiger',
  'type': 'Illustration',
  'client': 'Hawkers',
  'year': '',
  'description': '',
  'images': ['images/work/hawkers-tiger.webp']},
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
  'description': '',
  'images': ['images/work/fu-lion-playing-with-noodles.webp']},
 {'slug': 'ucf-mba-downtown-wall-wrap',
  'title': 'UCF MBA downtown wall wrap',
  'type': 'Environmental graphics',
  'client': 'UCF',
  'year': '',
  'description': '',
  'images': ['images/work/ucf-mba-downtown-wall-wrap.webp']},
 {'slug': 'hawkers-brunch-menu',
  'title': 'Hawkers brunch menu',
  'type': 'Menu',
  'client': 'Hawkers',
  'year': '',
  'description': '',
  'images': ['images/work/hawkers-brunch-menu.webp']},
 {'slug': 'hawkers-takeout-bag',
  'title': 'Hawkers takeout bag',
  'type': 'Packaging',
  'client': 'Hawkers',
  'year': '',
  'description': '',
  'images': ['images/work/hawkers-takeout-bag.webp']},
 {'slug': 'hawkers-beverage-coasters',
  'title': 'Hawkers beverage coasters',
  'type': 'Coaster',
  'client': 'Hawkers',
  'year': '',
  'description': '',
  'images': ['images/work/hawkers-beverage-coasters.webp']},
 {'slug': 'brunch-photoshoot',
  'title': 'Brunch photoshoot',
  'type': 'Art direction',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/brunch-photoshoot.webp']},
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
  'description': '',
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
  'description': '',
  'images': ['images/work/daruma-lucky-cat-drink-coaster.webp']},
 {'slug': 'asian-neon-masks',
  'title': 'Asian neon masks',
  'type': 'Neon sign',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/asian-neon-masks.webp']},
 {'slug': 'i-wanna-wok',
  'title': 'I Wanna Wok logo',
  'type': 'Logo',
  'client': '',
  'year': '',
  'description': '',
  'images': ['images/work/i-wanna-wok.webp']},
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
  'description': '',
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
  'description': '',
  'images': ['images/work/lapel-pins.webp']},
 {'slug': 'hawkers-to-go-cup',
  'title': 'Hawkers to-go cup',
  'type': 'Packaging',
  'client': 'Hawkers',
  'year': '',
  'description': '',
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
  'images': ['images/work/custom-neons.webp']}]
