#!/usr/bin/env python3
"""Generate RaptorFam KE nganya detail pages with a shared, self-contained template."""
import os

OUT = "/home/claude/raptorfam"

with open(os.path.join(OUT, "styles.css")) as f:
    BASE_CSS = f.read()

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&'
         'family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">')

# Proven-working tuko.co.ke CDN images (hotlink-friendly)
IMG = lambda h: f"https://cdn.tuko.co.ke/images/1200x675/{h}.jpeg?v=1"
POOL = {
    "mood1": IMG("d561d67a16870189"),
    "mood2": IMG("1381611c866493fa"),
    "mood3": IMG("42bea0778bcc24f8"),
    "money": IMG("26b9da2442fd2c9e"),
    "matrix": IMG("1166019093a00952"),
    "baba": IMG("2a1e36efef4914f3"),
    "raptor": IMG("8f89fab43ca445cc"),
}

DETAIL_CSS = """
/* DETAIL PAGE */
.detail-hero {
  position: relative; min-height: 88vh; display: flex; align-items: flex-end;
  background-size: cover; background-position: center;
}
.detail-hero::after {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(to top, rgba(10,10,10,1) 0%, rgba(10,10,10,0.4) 45%, rgba(255,92,0,0.18) 100%);
}
.detail-hero-inner { position: relative; z-index: 2; padding: 0 4rem 4rem; max-width: 900px; }
.back-link {
  position: absolute; top: 6.5rem; left: 4rem; z-index: 3;
  font-size: 0.8rem; letter-spacing: 2px; text-transform: uppercase;
  text-decoration: none; color: var(--white); opacity: 0.8;
}
.back-link:hover { color: var(--orange); opacity: 1; }
.detail-badge {
  background: var(--orange); color: #fff; font-size: 0.7rem; letter-spacing: 2px;
  padding: 0.3rem 0.9rem; text-transform: uppercase; font-weight: 700;
  display: inline-block; margin-bottom: 1rem;
}
.detail-name {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(4.5rem, 12vw, 10rem); line-height: 0.85; letter-spacing: 4px;
  text-shadow: 0 0 80px rgba(255,92,0,0.4);
}
.detail-name span { color: var(--orange); }
.detail-tag { font-size: 1.1rem; opacity: 0.8; margin: 1rem 0 2rem; line-height: 1.6; max-width: 600px; }
.detail-hero-btns { display: flex; gap: 1rem; flex-wrap: wrap; }

/* spec strip */
.spec-strip {
  background: var(--orange); display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1px;
}
.spec { background: var(--orange); padding: 1.6rem 1rem; text-align: center; }
.spec-val { font-family: 'Bebas Neue', sans-serif; font-size: 2rem; letter-spacing: 1px; color: #fff; line-height: 1; }
.spec-key { font-size: 0.68rem; letter-spacing: 2px; text-transform: uppercase; color: rgba(255,255,255,0.85); margin-top: 0.4rem; }

/* story */
.story-inner { display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; align-items: center; }
@media (max-width: 900px) { .story-inner { grid-template-columns: 1fr; gap: 2.5rem; } }
.story-text p { font-size: 1rem; line-height: 1.9; opacity: 0.82; margin-bottom: 1.4rem; }
.story-img { position: relative; border-radius: 4px; overflow: hidden; aspect-ratio: 4/5; }
.story-img img { width: 100%; height: 100%; object-fit: cover; }
.story-img::before { content: ''; position: absolute; inset: -1px; border: 2px solid var(--orange); z-index: 2; pointer-events: none; opacity: 0.3; }

/* feature chips */
.feat-list { list-style: none; display: flex; flex-direction: column; gap: 1.1rem; margin-top: 1rem; }
.feat { display: flex; gap: 1rem; align-items: flex-start; }
.feat-ic { font-size: 1.3rem; flex-shrink: 0; }
.feat-tx { font-size: 0.92rem; line-height: 1.6; opacity: 0.85; }
.feat-tx strong { display: block; color: var(--white); }

/* gallery */
.dg-grid {
  display: grid; grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 200px; gap: 2px;
}
@media (max-width: 768px) { .dg-grid { grid-template-columns: repeat(2, 1fr); } }
.dg-item { overflow: hidden; position: relative; }
.dg-item img { width: 100%; height: 100%; object-fit: cover; filter: saturate(0.85); transition: transform 0.6s, filter 0.3s; }
.dg-item:hover img { transform: scale(1.06); filter: saturate(1.2); }
.dg-item.wide { grid-column: span 2; }
.dg-item.tall { grid-row: span 2; }
@media (max-width: 768px) { .dg-item.wide, .dg-item.tall { grid-column: auto; grid-row: auto; } }

/* other rides */
.other-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px,1fr)); gap: 2px; }
.other-card { position: relative; aspect-ratio: 4/3; overflow: hidden; text-decoration: none; }
.other-card img { width: 100%; height: 100%; object-fit: cover; filter: brightness(0.7); transition: transform 0.5s, filter 0.3s; }
.other-card:hover img { transform: scale(1.06); filter: brightness(1); }
.other-card-name {
  position: absolute; left: 0; right: 0; bottom: 0; padding: 1rem;
  font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; letter-spacing: 2px;
  background: linear-gradient(to top, rgba(0,0,0,0.9), transparent);
}
.cta-band { background: var(--mid); text-align: center; }
.cta-band h2 { font-family: 'Syne', sans-serif; font-size: clamp(2rem,4vw,3.2rem); margin-bottom: 1.5rem; }
.cta-band h2 em { font-style: normal; color: var(--orange); }
footer.mini { background: var(--dark); border-top: 1px solid rgba(255,92,0,0.2); padding: 2.5rem 4rem; text-align: center; }
footer.mini .fb { font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; letter-spacing: 4px; color: var(--orange); }
footer.mini p { opacity: 0.5; font-size: 0.82rem; margin-top: 0.6rem; }
@media (max-width: 900px) { .detail-hero-inner { padding: 0 1.5rem 2.5rem; } .back-link { left: 1.5rem; } }
"""

NAV = """<nav>
  <a href="index.html" class="nav-logo">RAPTORFAM</a>
  <ul class="nav-links">
    <li><a href="index.html#fleet">Fleet</a></li>
    <li><a href="index.html#book">Book a Ride</a></li>
    <li><a href="index.html#culture">Culture</a></li>
    <li><a href="index.html#gallery">Gallery</a></li>
    <li><a href="index.html#contact">Contact</a></li>
  </ul>
  <a href="index.html#book" class="nav-cta">Book Now</a>
</nav>"""

SCRIPT = """<script>
const reveals = document.querySelectorAll('.reveal');
const ob = new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible');});},{threshold:0.1});
reveals.forEach(el=>ob.observe(el));
</script>"""

# ---- Per-nganya data ----
NGANYAS = {
    "mood": {
        "file": "mood.html",
        "name": "MOOD",
        "badge": "Flagship Nganya \u2605",
        "hero": POOL["mood1"],
        "tag": "Kenya's first solar-powered matatu. A KSh 14M disco on wheels that shut down Nairobi CBD on launch night.",
        "specs": [("KSh 14M","Build Cost"),("26","Bucket Seats"),("Solar","Powered PSV"),("Embakasi","Route"),("2025","Unveiled")],
        "story": [
            "When Mood rolled into the Kenyatta International Convention Centre on launch night in July 2025, Nairobi's CBD turned into a concert. Hundreds of young Kenyans thronged the streets for the unveiling \u2014 prayers, a symbolic anointing, live performances and a DJ set that ran deep into the night.",
            "Mood broke new ground as one of the first PSVs in Kenya to run solar power, keeping its screens and sound alive even through power cuts. It packs custom bucket seats with cup holders and USB charging ports, full air-conditioning, a push-to-start ignition, and a professional DJ console mounted right next to the driver.",
            "This is the crown jewel of the RaptorFam fleet \u2014 a moving theatre that proves matatu culture is one of Kenya's boldest creative exports.",
        ],
        "features": [
            ("\u2600\ufe0f","Solar Powered","Roof-mounted solar panels keep the screens and sound running through any outage."),
            ("\ud83c\udfa7","DJ Console","A professional DJ mixer fixed in the cockpit \u2014 a mobile party spot on wheels."),
            ("\ud83d\udecb\ufe0f","26 Bucket Seats","Each with cup holder, USB charging port and full air-conditioning."),
            ("\ud83d\udd11","Push-to-Start","Modern ignition and an NTSA-approved custom number plate."),
        ],
        "gallery": ["mood1","mood2","mood3","raptor","matrix","baba"],
    },
    "moneyfest": {
        "file": "moneyfest.html",
        "name": "MONEY<span>FEST</span>",
        "plain": "MONEYFEST",
        "badge": "Premium Ride",
        "hero": POOL["money"],
        "tag": "Statement graffiti, statement presence. A big-budget build born to make moves on the Embakasi run.",
        "specs": [("KSh 20M","Build Cost"),("Graffiti","Full Wrap"),("Pro","Sound Rig"),("Embakasi","Route"),("Premium","Interior")],
        "story": [
            "MoneyFest is exactly what the name promises \u2014 a celebration of hustle, art and unapologetic flex. Wrapped end-to-end in bold graffiti from Kenya's top street artists, every panel is a billboard for Nairobi's youth movement.",
            "Inside, premium interiors and a heavy sound rig turn the daily commute into an event. When MoneyFest pulls up, the whole block knows.",
            "It's one of the most photographed nganyas in the fleet \u2014 a favourite for brand activations, shoots and anyone who wants their arrival to be the main event.",
        ],
        "features": [
            ("\ud83c\udfa8","Full Graffiti Wrap","Murals across every panel by Nairobi's finest street artists."),
            ("\ud83c\udfb5","Heavy Sound Rig","Booming audio setup tuned to make an entrance."),
            ("\ud83d\udca1","Ambient Lighting","Interior LED strips and party lighting for the full vibe."),
            ("\ud83d\udcf8","Shoot-Ready","A go-to backdrop for music videos and brand activations."),
        ],
        "gallery": ["money","mood1","matrix","baba","raptor","mood3"],
    },
    "matrix": {
        "file": "matrix.html",
        "name": "MATRIX",
        "badge": "Fan Favorite",
        "hero": POOL["matrix"],
        "tag": "Inspired by the blockbuster. Digital screens, futuristic lighting and an KSh 8.7M build \u2014 Embakasi's finest.",
        "specs": [("KSh 8.7M","Build Cost"),("Digital","Screen Walls"),("Neon","Lighting"),("Embakasi","Route"),("Tech","Theme")],
        "story": [
            "Matrix takes its cue from the cult sci-fi blockbuster \u2014 think cascading code, neon greens and a futuristic build that feels like stepping into another dimension.",
            "Digital screens line the interior, ambient lighting shifts with the music, and the whole rig is engineered for maximum vibe. At KSh 8.7M, it's one of the sharpest tech-themed nganyas on the road.",
            "A genuine fan favourite, Matrix turns heads on the Embakasi route every single day.",
        ],
        "features": [
            ("\ud83d\udda5\ufe0f","Digital Screen Walls","Interior screens running visuals synced to the music."),
            ("\ud83d\udd06","Neon Lighting","Futuristic green-and-blue ambient lighting throughout."),
            ("\ud83c\udfae","Tech-Inspired Build","A sci-fi concept executed down to the smallest detail."),
            ("\ud83d\udd0a","Crisp Sound","Clean, punchy audio matched to the digital aesthetic."),
        ],
        "gallery": ["matrix","mood2","money","raptor","baba","mood1"],
    },
    "babayaga": {
        "file": "babayaga.html",
        "name": "BABA<span>YAGA</span>",
        "plain": "BABA YAGA",
        "badge": "Crew of the Year \ud83c\udfc6",
        "hero": POOL["baba"],
        "tag": "Ongata Rongai's most fierce matatu \u2014 and winner of Crew of the Year at the Nganya Awards 2025.",
        "specs": [("\ud83c\udfc6","Crew of the Year"),("Rongai","Route"),("Fierce","Design"),("2025","Award Winner"),("Iconic","Road Presence")],
        "story": [
            "Baba Yaga earned its name \u2014 fierce, unforgettable and impossible to ignore. Plying the Ongata Rongai route, it's become a symbol of just how far the craft of nganya building has come.",
            "In 2025 the crew took home Crew of the Year at the Nganya Awards, a recognition of the artistry, sound engineering and showmanship behind the build.",
            "Bold artwork, commanding presence and a crew that lives the culture \u2014 Baba Yaga is a fan favourite for events that need real road impact.",
        ],
        "features": [
            ("\ud83c\udfc6","Award-Winning Crew","Crew of the Year, Nganya Awards 2025."),
            ("\ud83c\udfa8","Fierce Artwork","Aggressive, unforgettable graffiti and detailing."),
            ("\ud83d\udd0a","Big Sound","A sound system built to dominate the road."),
            ("\ud83d\udd25","Road Presence","One of the most commanding nganyas in the city."),
        ],
        "gallery": ["baba","mood1","matrix","money","raptor","mood2"],
    },
    "raptor": {
        "file": "raptor.html",
        "name": "RAPTOR",
        "badge": "The OG \u2014 Back on Roads",
        "hero": POOL["raptor"],
        "tag": "Where it all started. Named after the F-22 Raptor fighter jet \u2014 fully revamped and back on the roads in 2026.",
        "specs": [("F-22","Namesake"),("2026","Comeback"),("The OG","Original Build"),("Revamped","Full Rebuild"),("Legend","Status")],
        "story": [
            "Raptor is where the whole story begins \u2014 the original build that gave the family its name, inspired by the F-22 Raptor fighter jet. Speed, edge and aggression baked into every line.",
            "After a major rebuild, the legend is back on the roads in 2026, fully revamped and sharper than ever. It carries the history of the entire movement on its panels.",
            "For the day-ones, Raptor isn't just a matatu \u2014 it's the namesake, the OG, the reason RaptorFam exists.",
        ],
        "features": [
            ("\u2708\ufe0f","Fighter-Jet DNA","Named and styled after the F-22 Raptor."),
            ("\ud83d\udd27","Full Rebuild","Revamped from the ground up for its 2026 return."),
            ("\ud83c\udfa8","Original Artwork","The build that started Nairobi's RaptorFam legend."),
            ("\ud83d\udc51","OG Status","The namesake of the whole family."),
        ],
        "gallery": ["raptor","mood1","matrix","money","baba","mood3"],
    },
}

GALLERY_CLASSES = ["wide tall", "", "", "wide", "tall", ""]

def other_rides(current):
    cards = ""
    for key, d in NGANYAS.items():
        if key == current:
            continue
        nm = d.get("plain", d["name"])
        cards += f'''      <a href="{d['file']}" class="other-card">
        <img src="{d['hero']}" alt="{nm}" loading="lazy">
        <div class="other-card-name">{nm}</div>
      </a>\n'''
    return cards

def build_detail(key, d):
    plain = d.get("plain", d["name"])
    specs = "".join(
        f'<div class="spec"><div class="spec-val">{v}</div><div class="spec-key">{k}</div></div>'
        for v, k in d["specs"])
    feats = "".join(
        f'<li class="feat"><span class="feat-ic">{ic}</span><div class="feat-tx"><strong>{t}</strong>{desc}</div></li>'
        for ic, t, desc in d["features"])
    gal = ""
    for i, imgkey in enumerate(d["gallery"]):
        cls = GALLERY_CLASSES[i % len(GALLERY_CLASSES)]
        gal += f'<div class="dg-item {cls}"><img src="{POOL[imgkey]}" alt="{plain}" loading="lazy"></div>'
    story = "".join(f"<p>{p}</p>" for p in d["story"])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{plain} \u2014 RaptorFam KE</title>
{FONTS}
<style>
{BASE_CSS}
{DETAIL_CSS}
</style>
</head>
<body>
{NAV}

<header class="detail-hero" style="background-image:url('{d['hero']}')">
  <a href="index.html#fleet" class="back-link">\u2190 Back to Fleet</a>
  <div class="detail-hero-inner">
    <span class="detail-badge">{d['badge']}</span>
    <h1 class="detail-name">{d['name']}</h1>
    <p class="detail-tag">{d['tag']}</p>
    <div class="detail-hero-btns">
      <a href="index.html?nganya={plain}#book" class="btn-primary">Book {plain}</a>
      <a href="#gallery" class="btn-outline">See the Photos</a>
    </div>
  </div>
</header>

<div class="spec-strip">{specs}</div>

<section>
  <div class="story-inner">
    <div class="story-text">
      <p class="section-label reveal">The Story</p>
      <h2 class="section-title reveal" style="font-size:clamp(2rem,4vw,3rem);">INSIDE <em>{plain}</em></h2>
      {story}
      <ul class="feat-list reveal">{feats}</ul>
    </div>
    <div class="story-img reveal"><img src="{POOL[d['gallery'][1]]}" alt="{plain}"></div>
  </div>
</section>

<section id="gallery" style="padding-top:0;">
  <p class="section-label reveal">Gallery</p>
  <h2 class="section-title reveal">{plain}. <em>UP CLOSE.</em></h2>
  <div class="dg-grid">{gal}</div>
</section>

<section style="padding-bottom:0;">
  <p class="section-label reveal">More of the Family</p>
  <h2 class="section-title reveal">THE REST OF THE <em>FLEET</em></h2>
  <div class="other-grid">
{other_rides(key)}  </div>
</section>

<section class="cta-band">
  <h2>READY TO RIDE <em>{plain}?</em></h2>
  <p style="opacity:0.7; margin-bottom:2rem;">Call or WhatsApp <a href="tel:+254721200200" style="color:var(--orange);font-weight:700;">+254 721 200 200</a> \u2014 we confirm within 2 hours.</p>
  <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
    <a href="index.html?nganya={plain}#book" class="btn-primary">Book {plain}</a>
    <a href="https://wa.me/254721200200" target="_blank" class="btn-outline">\ud83d\udcac WhatsApp Us</a>
  </div>
</section>

<footer class="mini">
  <div class="fb">RAPTORFAM KE</div>
  <p>Nairobi's most iconic nganya family \u2022 +254 721 200 200 \u2022 @raptorfam_ke</p>
</footer>
{SCRIPT}
</body>
</html>"""
    html = html.encode("utf-16", "surrogatepass").decode("utf-16")
    path = os.path.join(OUT, d["file"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", d["file"])

for key, d in NGANYAS.items():
    build_detail(key, d)

print("done")