"""
Jake V. Alipin | Autobiography & Portfolio
CSIT 349 · Applied AI · BSIT-4 · Section G01
Theme: Cyberpunk / Edgerunners (neon yellow · cyan · magenta on night-black)

Run with:  streamlit run app.py
"""

from datetime import date, datetime
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# ──────────────────────────────────────────────────────────────────────────────
# 1. PAGE CONFIG  (must be the first Streamlit call)
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Jake V. Alipin | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"About": "Autobiography & Portfolio built with Streamlit · CSIT 349 · BSIT-4 · G01"},
)

# ──────────────────────────────────────────────────────────────────────────────
# 2. CONTENT
# ──────────────────────────────────────────────────────────────────────────────
PROFILE = {
    "name": "Jake V. Alipin",
    "course": "BSIT-4",
    "program": "BS Information Technology",
    "year": "4th Year",
    "section": "G01",
    "class_label": "CSIT 349 · Section G01",
    "school": "Cebu Institute of Technology – University",
    "school_short": "CIT-U",
    "location": "Pinamungajan, Cebu, Philippines",
    "headline": "IT student by day, visual creator always: part developer, part artist, part editor.",
    "email": "jakealipinv@gmail.com",
    "github": "https://github.com/jiku202",
    "portfolio_site": "https://github.com/jiku202/portfolio-site",
    "bio": [
        "I'm **Jake V. Alipin**, a fourth-year BSIT student at Cebu Institute of Technology – "
        "University, originally from Pinamungajan, Cebu. At my core, I'm a creator. I'm really "
        "into art, and nothing beats the feeling of making something from nothing, whether it's "
        "a video edit cut to the beat of a favorite song, a graphic design built layer by layer, "
        "or a photograph that holds on to a quiet moment.",
        "Music keeps my creative gears turning and table tennis keeps me sharp, "
        "quick on my feet and out of my own head. I'm a shy and spiritual person by nature, so "
        "I usually let my work do the talking. Nature, anime and manga (One Piece forever) "
        "fill in the rest of my inspiration.",
        "Studying information technology gave me a way to bring both sides together: "
        "building things on a screen that look good *and* work well. I'm always chasing the "
        "next idea, and I'm excited to keep growing as a developer with a designer's eye.",
    ],
    "fun_facts": [
        "🙏 A spiritual person at heart",
        "🤫 Very shy, but warms up fast with the right people",
        "🌿 Loves nature and quiet places",
        "🎨 Art is basically my second language",
        "🏓 Table tennis is my go-to sport",
        "🎬 Video editing: I can lose hours in a timeline",
        "🏴‍☠️ Favorite anime: One Piece",
        "📖 Manga reader, always one more chapter",
        "🥚 Eggs. Any style. Any time.",
    ],
}

# (year, title, story, emoji)
TIMELINE = [
    (2016, "Junior High School begins", "Started Basic Education, a time when my love for art, music and exploring new things started to take shape.", "🌱"),
    (2021, "Senior High: ICT Strand", "Chose the ICT strand and got my first real taste of computers, design and building things on a screen.", "💻"),
    (2023, "Enrolled at CIT-U", "Began my BSIT journey at Cebu Institute of Technology – University, balancing code with my creative side.", "🎓"),
    (2026, "Fourth year · Applied AI", "Now in my final stretch, exploring how to build and deploy smart, well-designed apps.", "🚀"),
]

EDUCATION = pd.DataFrame(
    [
        ("Cebu Institute of Technology – University", "BS Information Technology", "2023 – Present", "4th year · Section G01"),
        ("Senior High School", "ICT Strand", "2021 – 2023", "Information & Communications Technology track"),
        ("Junior High School", "Basic Education", "2016 – 2021", "Foundation years"),
    ],
    columns=["School", "Program", "Years", "Notes"],
)

INTERESTS = ["Music", "Video Editing", "Graphic Design", "Table Tennis", "Photography",
             "Art", "Anime & Manga", "Nature"]

# (skill, category, level 0-100, years)  ← self-assessed, adjust to your own numbers
SKILLS = pd.DataFrame(
    [
        ("Video Editing", "Creative", 80, 4),
        ("Graphic Design", "Creative", 80, 4),
        ("Photography", "Creative", 70, 4),
        ("Python", "Programming", 65, 2),
        ("Streamlit", "Programming", 55, 1),
        ("HTML / CSS", "Web", 70, 3),
        ("JavaScript", "Web", 55, 2),
        ("SQL", "Data", 60, 2),
        ("Git & GitHub", "Tools", 65, 2),
        ("Creativity", "Soft skills", 90, 6),
        ("Teamwork", "Soft skills", 75, 4),
    ],
    columns=["Skill", "Category", "Level", "Years"],
)

# link=None → shows "link coming soon"
PROJECTS = [
    {
        "title": "Streamlit Autobiography App",
        "emoji": "⚡",
        "role": "Designer & developer",
        "tools": ["Python", "Streamlit", "Pandas"],
        "year": 2026,
        "type": "Web app",
        "summary": "This very site: an interactive autobiography and portfolio with a cyberpunk, Edgerunners-inspired look.",
        "details": "Built for CSIT 349. Combines data tables, charts, forms, session state and custom CSS to turn a Python script into a neon-lit personal site.",
        "outcome": "A fully interactive portfolio made with Streamlit components and a custom theme",
        "link": "https://github.com/jiku202",
    },
    {
        "title": "Personal Portfolio Website",
        "emoji": "🌐",
        "role": "Designer & front-end developer",
        "tools": ["HTML / CSS", "JavaScript", "Git & GitHub"],
        "year": 2025,
        "type": "Website",
        "summary": "A hand-coded personal website to showcase my creative work and practice front-end fundamentals.",
        "details": "Focused on layout, typography and responsiveness, and on keeping the code organized in a Git repository.",
        "outcome": "A live repository that taught me version control and responsive design",
        "link": "https://github.com/jiku202/streamlit-portfolio",
    },
    {
        "title": "Motion Reel: Video Edits",
        "emoji": "🎬",
        "role": "Video editor",
        "tools": ["Video Editing", "Color Grading", "Sound Design"],
        "year": 2025,
        "type": "Video",
        "summary": "A collection of music-driven edits that experiment with pacing, transitions and color.",
        "details": "Each edit starts with a song and a mood, then builds visuals around the beat using cuts, effects and grading.",
        "outcome": "Sharper sense of rhythm, pacing and storytelling through motion",
        "link": None,
    },
    {
        "title": "Neon Poster & Graphic Series",
        "emoji": "🎨",
        "role": "Graphic designer",
        "tools": ["Graphic Design", "Typography", "Layout"],
        "year": 2024,
        "type": "Design",
        "summary": "A series of posters and graphics inspired by anime, music and city nightscapes.",
        "details": "Explored bold type, contrast and color palettes, and how composition guides the viewer's eye.",
        "outcome": "A growing visual style and a stronger eye for composition",
        "link": None,
    },
    {
        "title": "Nature & Street Photo Journal",
        "emoji": "📷",
        "role": "Photographer & editor",
        "tools": ["Photography", "Photo Editing", "Color Grading"],
        "year": 2024,
        "type": "Photo",
        "summary": "A photo series capturing quiet nature scenes and everyday moments around Cebu.",
        "details": "Shot on location and edited for mood and tone, pairing my love of nature with my editing skills.",
        "outcome": "Learned to find stories in small, quiet details",
        "link": None,
    },
]

ACCENTS = {  # name: (hex, rgb)
    "Yellow": ("#FCEE0A", "252,238,10"),
    "Cyan": ("#00F0FF", "0,240,255"),
    "Magenta": ("#FF2A6D", "255,42,109"),
}

# ──────────────────────────────────────────────────────────────────────────────
# 3. STATE
# ──────────────────────────────────────────────────────────────────────────────
st.session_state.setdefault("waves", 0)
st.session_state.setdefault("messages", [])
st.session_state.setdefault("uploaded_photo", None)
st.session_state.setdefault("accent", "Yellow")

ACCENT_HEX, ACCENT_RGB = ACCENTS[st.session_state["accent"]]

# ──────────────────────────────────────────────────────────────────────────────
# 4. STYLE: Cyberpunk Edgerunners
# ──────────────────────────────────────────────────────────────────────────────
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Rajdhani:wght@400;500;600;700&display=swap');

:root {
  --accent: __HEX__; --accent-rgb: __RGB__;
  --cyan: #00F0FF; --pink: #FF2A6D; --panel: #12121F;
}

/* background: night city glow + scanlines */
.stApp {
  background:
    radial-gradient(900px 500px at 90% -5%, rgba(255,42,109,.20), transparent 60%),
    radial-gradient(900px 520px at -5% 8%, rgba(0,240,255,.15), transparent 60%),
    linear-gradient(rgba(255,255,255,.018) 1px, transparent 1px) 0 0 / 100% 44px,
    #0A0A12;
  font-family: 'Rajdhani', sans-serif;
  font-size: 1.08rem;
}
.stApp::before {
  content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 9999;
  background: repeating-linear-gradient(to bottom, rgba(255,255,255,.03) 0, rgba(255,255,255,.03) 1px, transparent 1px, transparent 3px);
}
header[data-testid="stHeader"] { background: transparent; }

/* type */
h1, h2, h3, h4 { font-family: 'Orbitron', sans-serif !important; letter-spacing: .05em; text-transform: uppercase; }
h2 { border-left: 4px solid var(--accent); padding-left: .7rem; font-size: 1.6rem !important; }
h3 { color: var(--cyan); font-size: 1.15rem !important; }
.stMarkdown p, .stMarkdown li { line-height: 1.65; }
label, [data-testid="stWidgetLabel"] p { font-weight: 600; letter-spacing: .04em; }

/* hero */
.hud { font-family: 'Orbitron'; font-size: .78rem; letter-spacing: .25em; color: var(--cyan); margin-bottom: .4rem; }
.hud::before { content: "▌"; color: var(--pink); margin-right: .5rem; animation: blink 1.2s steps(2) infinite; }
.hero-title {
  font-family: 'Orbitron'; font-weight: 900; text-transform: uppercase; line-height: 1.05;
  font-size: clamp(2.1rem, 5.2vw, 3.9rem); color: #fff; margin-bottom: .5rem;
  text-shadow: 2px 0 var(--pink), -2px 0 var(--cyan);
  animation: glitch 4s infinite;
}
.hero-sub { font-size: 1.25rem; color: #c9c9dd; margin-bottom: 1rem; max-width: 46rem; }
.hero-sub b { color: var(--accent); }
@keyframes blink { 50% { opacity: 0; } }
@keyframes glitch {
  0%, 91%, 100% { transform: none; text-shadow: 2px 0 var(--pink), -2px 0 var(--cyan); }
  92% { transform: translate(-4px, 1px); text-shadow: 5px 0 var(--pink), -5px 0 var(--cyan); }
  94% { transform: translate(4px, -1px); text-shadow: -5px 0 var(--pink), 5px 0 var(--cyan); }
  96% { transform: translate(-2px, 0); text-shadow: 3px 0 var(--cyan), -3px 0 var(--pink); }
}

/* pills */
.pill {
  display: inline-block; padding: .18rem .85rem; margin: 0 .4rem .4rem 0;
  border: 1px solid var(--accent); color: var(--accent); background: rgba(var(--accent-rgb), .07);
  font-weight: 700; font-size: .85rem; letter-spacing: .1em; text-transform: uppercase;
  clip-path: polygon(8px 0, 100% 0, 100% calc(100% - 8px), calc(100% - 8px) 100%, 0 100%, 0 8px);
}

/* photo */
[data-testid="stImage"] img {
  border: 2px solid var(--accent); border-radius: 2px;
  box-shadow: 0 0 0 5px rgba(var(--accent-rgb), .12), -10px 10px 0 var(--pink), 0 0 30px rgba(0,240,255,.35);
}
[data-testid="stSidebar"] [data-testid="stImage"] img { box-shadow: 0 0 18px rgba(0,240,255,.4); }

/* metrics */
[data-testid="stMetric"] {
  background: linear-gradient(135deg, #15152a, #0d0d19);
  border: 1px solid rgba(var(--accent-rgb), .35); border-left: 4px solid var(--accent);
  padding: .8rem 1rem; box-shadow: 0 0 18px rgba(var(--accent-rgb), .08);
}
[data-testid="stMetricValue"] { font-family: 'Orbitron'; color: var(--accent); }
[data-testid="stMetricLabel"] p { text-transform: uppercase; letter-spacing: .12em; font-size: .8rem; }

/* cards (bordered containers are keyed "card-*") */
[class*="st-key-card"] {
  background: linear-gradient(160deg, rgba(20,20,40,.92), rgba(10,10,20,.92));
  border: 1px solid rgba(0,240,255,.35) !important;
  border-left: 4px solid var(--pink) !important;
  border-radius: 2px !important;
  box-shadow: 0 0 22px rgba(0,240,255,.07);
}

/* tabs */
button[data-baseweb="tab"] { font-family: 'Orbitron'; font-size: .85rem; letter-spacing: .14em; text-transform: uppercase; }
button[data-baseweb="tab"][aria-selected="true"] { color: var(--accent); }
[data-baseweb="tab-highlight"] { background-color: var(--accent) !important; box-shadow: 0 0 10px var(--accent); }

/* buttons */
.stButton button, .stDownloadButton button, .stFormSubmitButton button, .stLinkButton a {
  font-family: 'Orbitron'; font-size: .78rem; letter-spacing: .14em; text-transform: uppercase;
  background: transparent; color: var(--accent); border: 1px solid var(--accent); border-radius: 0;
  clip-path: polygon(10px 0, 100% 0, 100% calc(100% - 10px), calc(100% - 10px) 100%, 0 100%, 0 10px);
  transition: all .15s ease;
}
.stButton button:hover, .stDownloadButton button:hover, .stFormSubmitButton button:hover, .stLinkButton a:hover {
  background: var(--accent); color: #0A0A12; box-shadow: 0 0 16px rgba(var(--accent-rgb), .6);
}
.stFormSubmitButton button[kind="primary"], .stButton button[kind="primary"] { background: var(--accent); color: #0A0A12; }

/* inputs, tags, expanders */
span[data-baseweb="tag"] { background: rgba(255,42,109,.22) !important; border: 1px solid var(--pink); color: #fff !important; }
[data-testid="stExpander"] { border: 1px solid rgba(0,240,255,.3); border-radius: 2px; background: rgba(18,18,31,.7); }
[data-testid="stExpander"] summary { font-weight: 700; letter-spacing: .04em; }
[data-testid="stAlert"] { border-radius: 2px; }

/* sidebar */
section[data-testid="stSidebar"] { background: #0b0b17; border-right: 1px solid rgba(var(--accent-rgb), .45); }
section[data-testid="stSidebar"] h2 { font-size: 1.1rem !important; }

hr { border-color: rgba(var(--accent-rgb), .25) !important; }
.footer { text-align: center; color: #8a8aa8; font-size: .9rem; letter-spacing: .15em; text-transform: uppercase; padding: 1.5rem 0 .5rem; }
.footer b { color: var(--accent); }
</style>
"""
st.markdown(CSS.replace("__HEX__", ACCENT_HEX).replace("__RGB__", ACCENT_RGB), unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# 5. HELPERS
# ──────────────────────────────────────────────────────────────────────────────
@st.cache_data
def make_avatar(initials: str, size: int = 600) -> Image.Image:
    """Fallback stand-in photo used only if assets/photo.png is missing."""
    img = Image.new("RGB", (size, size), (18, 18, 40))
    d = ImageDraw.Draw(img)
    for i in range(0, size, 24):
        d.line([(i, 0), (i, size)], fill=(40, 20, 70))
        d.line([(0, i), (size, i)], fill=(40, 20, 70))
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", size // 3)
    except OSError:
        font = ImageFont.load_default()
    w, h = d.textbbox((0, 0), initials, font=font)[2:]
    d.text(((size - w) / 2, (size - h) / 2), initials, fill=(252, 238, 10), font=font)
    return img


def get_photo():
    """Priority: uploaded photo (this session) > assets/photo.* > generated stand-in."""
    if st.session_state.get("uploaded_photo") is not None:
        return Image.open(st.session_state["uploaded_photo"])
    for name in ("photo.png", "photo.jpg", "photo.jpeg"):
        p = Path(__file__).parent / "assets" / name
        if p.exists():
            return Image.open(p)
    return make_avatar("".join(w[0] for w in PROFILE["name"].split()[:2]).upper())


def build_resume_text() -> str:
    lines = [
        PROFILE["name"].upper(),
        f'{PROFILE["program"]} ({PROFILE["course"]}) · {PROFILE["school"]} · Section {PROFILE["section"]}',
        f'{PROFILE["email"]} · {PROFILE["github"]}',
        f'{PROFILE["location"]}',
        "",
        "ABOUT",
        *PROFILE["bio"],
        "",
        "EDUCATION",
        *[f"- {r.Program}, {r.School} ({r.Years})" for r in EDUCATION.itertuples()],
        "",
        "SKILLS",
        *[f"- {r.Skill}: {r.Level}/100 ({r.Years} yrs)" for r in SKILLS.itertuples()],
        "",
        "PROJECTS",
        *[f'- {p["title"]} ({p["year"]}) | {p["role"]} | {", ".join(p["tools"])} | {p["outcome"]}' for p in PROJECTS],
        "",
        "INTERESTS",
        ", ".join(INTERESTS),
    ]
    return "\n".join(lines).replace("**", "").replace("*", "")


def pills(items):
    return "".join(f'<span class="pill">{t}</span>' for t in items)


# ──────────────────────────────────────────────────────────────────────────────
# 6. SIDEBAR
# ──────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image(get_photo(), width="stretch")
    st.header(PROFILE["name"])
    st.caption(f'🎓 {PROFILE["course"]} · {PROFILE["school_short"]}')
    st.caption(f'🏷️ {PROFILE["class_label"]}')
    st.caption(f'📍 {PROFILE["location"]}')

    st.divider()
    st.subheader("⚙️ Interface")
    st.selectbox("HUD color", list(ACCENTS), key="accent", help="Changes the neon accent color of the site.")
    show_fun = st.checkbox("Show fun facts", value=True)
    detail_level = st.radio("Project detail", ["Compact", "Detailed"], index=1, horizontal=True,
                            help="Compact hides the long project descriptions.")

    if st.button("👋 Ping Jake", width="stretch"):
        st.session_state.waves += 1
        st.toast(f"Connection established! (ping #{st.session_state.waves})", icon="⚡")
    if st.session_state.waves:
        st.caption(f"Pings sent this session: {st.session_state.waves}")

    with st.expander("🖼️ Try a different photo"):
        up = st.file_uploader("Upload a photo", type=["png", "jpg", "jpeg"])
        if up is not None:
            st.session_state.uploaded_photo = up
        st.caption("Preview only. The permanent photo is assets/photo.png.")

    st.divider()
    st.link_button("GitHub", PROFILE["github"], width="stretch")
    st.link_button("Portfolio repo", PROFILE["portfolio_site"], width="stretch")

# ──────────────────────────────────────────────────────────────────────────────
# 7. HERO
# ──────────────────────────────────────────────────────────────────────────────
hero_l, hero_r = st.columns([1, 2], gap="large", vertical_alignment="center")
with hero_l:
    st.image(get_photo(), width="stretch")
with hero_r:
    st.markdown(f'<div class="hud">SYSTEM ONLINE // {PROFILE["school_short"]} · {PROFILE["course"]} · {PROFILE["section"]}</div>',
                unsafe_allow_html=True)
    st.markdown(f'<div class="hero-title">{PROFILE["name"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="hero-sub">{PROFILE["headline"]}</div>', unsafe_allow_html=True)
    st.markdown(pills([PROFILE["program"], PROFILE["year"], f'Section {PROFILE["section"]}', PROFILE["school_short"]]),
                unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Projects", len(PROJECTS))
    m2.metric("Skills tracked", len(SKILLS))
    m3.metric("Avg. skill", f"{SKILLS['Level'].mean():.0f}/100",
              delta=f"{SKILLS['Level'].max() - SKILLS['Level'].mean():.0f} to top skill")
    m4.metric("Year level", "4th")

st.divider()

# ──────────────────────────────────────────────────────────────────────────────
# 8. TABS
# ──────────────────────────────────────────────────────────────────────────────
tab_about, tab_story, tab_skills, tab_projects, tab_contact = st.tabs(
    ["About", "Autobiography", "Skills", "Projects", "Contact"]
)

# ───────── ABOUT ─────────
with tab_about:
    st.header("About me")
    c1, c2 = st.columns([3, 2], gap="large")
    with c1:
        for para in PROFILE["bio"]:
            st.write(para)
        st.subheader("What I'm into")
        chosen = st.multiselect("Pick the interests we share:", INTERESTS, default=INTERESTS[:3])
        if chosen:
            st.success(f"We both like **{', '.join(chosen)}**. Let's talk!")
        else:
            st.info("Select a few interests to see what we have in common.")
    with c2:
        with st.container(border=True, key="card-facts"):
            st.subheader("Quick facts")
            st.markdown(
                f"""
                - **Name:** {PROFILE['name']}
                - **Course:** {PROFILE['program']} ({PROFILE['course']})
                - **Section:** {PROFILE['section']}
                - **School:** {PROFILE['school']}
                - **From:** {PROFILE['location']}
                """
            )
        if show_fun:
            with st.container(border=True, key="card-fun"):
                st.subheader("Fun facts")
                for fact in PROFILE["fun_facts"]:
                    st.write(fact)

# ───────── AUTOBIOGRAPHY ─────────
with tab_story:
    st.header("My story")
    st.caption("From a curious kid in Pinamungajan to a BSIT senior at CIT-U.")

    left, right = st.columns([2, 3], gap="large")
    with left:
        st.subheader("🎓 Education")
        st.dataframe(EDUCATION, hide_index=True, width="stretch")
        st.subheader("🌟 Milestones")
        years = [t[0] for t in TIMELINE]
        picked = st.select_slider("Slide through the years", options=years, value=years[-1])
    with right:
        year, title, story, emoji = next(t for t in TIMELINE if t[0] == picked)
        with st.container(border=True, key="card-milestone"):
            st.markdown(f"### {emoji} {year}: {title}")
            st.write(story)
            idx = years.index(picked)
            st.progress((idx + 1) / len(years), text=f"Milestone {idx + 1} of {len(years)}")

    st.subheader("🧭 Full timeline")
    for year, title, story, emoji in TIMELINE:
        with st.expander(f"{emoji}  {year} · {title}"):
            st.write(story)

    st.subheader("💭 In my own words")
    st.markdown(
        "> I'm quiet, so I express myself through what I make: edits, designs, photos and "
        "now code. Every project is a way of saying something I might not say out loud. "
        "I want to keep building things that are useful *and* beautiful."
    )

# ───────── SKILLS ─────────
with tab_skills:
    st.header("Skills")
    st.caption("Self-assessed on a 0–100 scale.")

    f1, f2, f3 = st.columns([2, 2, 1.4])
    with f1:
        all_cats = sorted(SKILLS["Category"].unique())
        cats = st.multiselect("Categories", all_cats, default=all_cats)
    with f2:
        min_level = st.slider("Minimum level", 0, 100, 50, step=5)
    with f3:
        chart_type = st.selectbox("Chart", ["Bar", "Area", "Line"])

    view = SKILLS[SKILLS["Category"].isin(cats) & (SKILLS["Level"] >= min_level)]
    if view.empty:
        st.warning("No skills match those filters. Try lowering the minimum level.")
    else:
        t_chart, t_table, t_cat = st.tabs(["Chart", "Table", "By category"])
        with t_chart:
            chart_fn = {"Bar": st.bar_chart, "Area": st.area_chart, "Line": st.line_chart}[chart_type]
            chart_fn(view.set_index("Skill")[["Level"]], color=ACCENT_HEX)
        with t_table:
            st.dataframe(
                view.sort_values("Level", ascending=False),
                hide_index=True,
                width="stretch",
                column_config={
                    "Level": st.column_config.ProgressColumn("Level", min_value=0, max_value=100, format="%d"),
                    "Years": st.column_config.NumberColumn("Years", format="%d yr"),
                },
            )
        with t_cat:
            avg = view.groupby("Category")["Level"].mean().round(0).sort_values(ascending=False)
            st.bar_chart(avg, horizontal=True, color="#00F0FF")
            top = view.loc[view["Level"].idxmax()]
            st.metric("Strongest skill in view", top["Skill"], f'{top["Level"]}/100')

    st.subheader("Upgrading next")
    st.markdown("- **Deep learning** with PyTorch\n- **Motion graphics** and advanced color grading\n- **Cloud deployment** (Docker, Streamlit Cloud)")

# ───────── PROJECTS ─────────
with tab_projects:
    st.header("Projects")
    all_tools = sorted({t for p in PROJECTS for t in p["tools"]})
    p1, p2 = st.columns([3, 1])
    with p1:
        tool_filter = st.multiselect("Filter by tool", all_tools, placeholder="All tools")
    with p2:
        sort_by = st.selectbox("Sort by", ["Newest first", "Oldest first", "Title A–Z"])

    shown = [p for p in PROJECTS if not tool_filter or set(tool_filter) & set(p["tools"])]
    shown.sort(key=lambda p: (p["title"] if sort_by == "Title A–Z" else p["year"]),
               reverse=(sort_by == "Newest first"))

    st.caption(f"Showing {len(shown)} of {len(PROJECTS)} projects")
    for i, p in enumerate(shown):
        with st.container(border=True, key=f"card-project-{i}"):
            a, b = st.columns([3, 1], gap="large", vertical_alignment="center")
            with a:
                st.subheader(f'{p["emoji"]} {p["title"]}')
                st.markdown(f'**Role:** {p["role"]} &nbsp;·&nbsp; **Year:** {p["year"]}')
                st.write(p["summary"])
                st.markdown(pills(p["tools"]), unsafe_allow_html=True)
                if detail_level == "Detailed":
                    st.write(p["details"])
                st.success(f'**Outcome:** {p["outcome"]}')
            with b:
                st.metric("Type", p["type"])
                if p["link"]:
                    st.link_button("View project ↗", p["link"], width="stretch")
                else:
                    st.caption("🔒 Link coming soon")
    if not shown:
        st.info("No projects use those tools. Clear the filter to see everything.")

    with st.expander("📈 Creative output by month (demo data)"):
        rng = np.random.default_rng(349)
        activity = pd.DataFrame(
            rng.integers(2, 20, size=(12, 3)),
            columns=["Edits", "Designs", "Photos"],
            index=pd.date_range("2025-01-01", periods=12, freq="MS").strftime("%b"),
        )
        st.line_chart(activity, color=["#FCEE0A", "#00F0FF", "#FF2A6D"])
        st.caption("Sample numbers for illustration. Swap in your real counts.")

# ───────── CONTACT ─────────
with tab_contact:
    st.header("Open a channel")
    form_col, side_col = st.columns([3, 2], gap="large")

    with form_col:
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your name", placeholder="Juan Dela Cruz")
            email = st.text_input("Email", placeholder="you@example.com")
            topic = st.selectbox("Topic", ["Feedback on this site", "Project collaboration",
                                           "Internship / job opportunity", "Just saying hi"])
            rating = st.slider("Rate this portfolio", 1, 5, 4)
            when = st.date_input("Best date to reply", value=date.today())
            message = st.text_area("Message", height=140, placeholder="Drop your message here…")
            subscribe = st.checkbox("Send me a copy of my message")
            sent = st.form_submit_button("Transmit message", type="primary", width="stretch")

        if sent:
            if not name.strip() or "@" not in email or not message.strip():
                st.error("Transmission failed: please fill in your name, a valid email, and a message.")
            else:
                st.session_state.messages.append(
                    {"Time": datetime.now().strftime("%Y-%m-%d %H:%M"), "Name": name, "Email": email,
                     "Topic": topic, "Rating": rating, "Reply by": str(when), "Message": message}
                )
                st.success(f"Transmission received, {name}! Your message about **{topic.lower()}** is in. "
                           f"{'A copy is on its way. ' if subscribe else ''}I'll reply by {when:%b %d}.")
                st.balloons()

    with side_col:
        with st.container(border=True, key="card-contact"):
            st.subheader("Direct line")
            st.write(f"📧 {PROFILE['email']}")
            st.write(f"📍 {PROFILE['location']}")
            st.write(f"🏷️ {PROFILE['class_label']}")
            st.link_button("GitHub profile", PROFILE["github"], width="stretch")
            st.link_button("Portfolio repo", PROFILE["portfolio_site"], width="stretch")
        st.download_button(
            "Download résumé (.txt)",
            data=build_resume_text(),
            file_name="Jake_V_Alipin_resume.txt",
            mime="text/plain",
            width="stretch",
        )
        if st.session_state.messages:
            msgs = pd.DataFrame(st.session_state.messages)
            st.metric("Messages this session", len(msgs), delta=f"avg rating {msgs['Rating'].mean():.1f}★")
            with st.expander("📬 View submitted messages"):
                st.dataframe(msgs, hide_index=True, width="stretch")
            st.download_button("Download messages (.csv)", msgs.to_csv(index=False),
                               "messages.csv", "text/csv", width="stretch")

# ──────────────────────────────────────────────────────────────────────────────
# 9. FOOTER
# ──────────────────────────────────────────────────────────────────────────────
st.markdown(
    f'<div class="footer">// <b>{PROFILE["name"]}</b> · {PROFILE["course"]} · Section {PROFILE["section"]} · '
    f'{PROFILE["school_short"]} · Built with Streamlit · {date.today().year}</div>',
    unsafe_allow_html=True,
)
