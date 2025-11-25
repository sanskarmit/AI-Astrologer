from __future__ import annotations
from dataclasses import dataclass
from datetime import date, time, datetime
from dateutil.relativedelta import relativedelta
from typing import Dict, Any
import hashlib

@dataclass
class InputData:
    name: str
    birth_date: date
    birth_time: time
    birth_place: str

    def validate(self) -> None:
        if not self.name:
            raise ValueError("Name is required")
        if not isinstance(self.birth_date, date):
            raise ValueError("Birth date is invalid")
        if not isinstance(self.birth_time, time):
            raise ValueError("Birth time is invalid")
        if not self.birth_place:
            raise ValueError("Birth place is required")

ZODIAC_DATES = [
    (119, "Capricorn"),   # Dec 22 – Jan 19
    (218, "Aquarius"),    # Jan 20 – Feb 18
    (320, "Pisces"),      # Feb 19 – Mar 20
    (419, "Aries"),       # Mar 21 – Apr 19
    (520, "Taurus"),      # Apr 20 – May 20
    (620, "Gemini"),      # May 21 – Jun 20
    (722, "Cancer"),      # Jun 21 – Jul 22
    (822, "Leo"),         # Jul 23 – Aug 22
    (922, "Virgo"),       # Aug 23 – Sep 22
    (1022, "Libra"),      # Sep 23 – Oct 22
    (1121, "Scorpio"),    # Oct 23 – Nov 21
    (1221, "Sagittarius"),# Nov 22 – Dec 21
    (1231, "Capricorn"),  # Dec 22 – Dec 31
]

ELEMENTS = {
    "Aries": "Fire",
    "Leo": "Fire",
    "Sagittarius": "Fire",
    "Taurus": "Earth",
    "Virgo": "Earth",
    "Capricorn": "Earth",
    "Gemini": "Air",
    "Libra": "Air",
    "Aquarius": "Air",
    "Cancer": "Water",
    "Scorpio": "Water",
    "Pisces": "Water",
}

TIME_TRAITS = [
    (5, "early riser clarity"),
    (11, "forenoon momentum"),
    (16, "afternoon adaptability"),
    (20, "evening reflection"),
    (24, "night-owl intuition"),
]

SIGN_TRAITS = {
    "Aries": "bold, pioneering energy",
    "Taurus": "steady, grounded presence",
    "Gemini": "curious, communicative spark",
    "Cancer": "intuitive, nurturing vibe",
    "Leo": "radiant, expressive leadership",
    "Virgo": "practical, detail-oriented focus",
    "Libra": "harmonizing, diplomatic balance",
    "Scorpio": "deep, transformative magnetism",
    "Sagittarius": "adventurous, truth-seeking spirit",
    "Capricorn": "ambitious, disciplined drive",
    "Aquarius": "visionary, original perspective",
    "Pisces": "creative, empathetic flow",
}

ADVICE_BUCKETS = {
    "Fire": [
        "Channel your momentum into one clear goal this week.",
        "Take a small risk that excites you—start, then iterate.",
    ],
    "Earth": [
        "Build a simple routine; consistency will compound.",
        "Tackle one practical task that reduces friction in your life.",
    ],
    "Air": [
        "Write your thoughts—clarity comes from articulation.",
        "Have a meaningful conversation that stretches your thinking.",
    ],
    "Water": [
        "Trust your intuition; journal a gut feeling and act on it.",
        "Protect your energy—set one gentle boundary today.",
    ],
}


def zodiac_sign(d: date) -> str:
    mmdd = d.month * 100 + d.day
    for cutoff, sign in ZODIAC_DATES:
        if mmdd <= cutoff:
            return sign
    return "Capricorn"


def life_path_number(d: date) -> int:
    s = sum(int(c) for c in d.strftime("%Y%m%d"))
    while s > 9 and s not in (11, 22, 33):
        s = sum(int(c) for c in str(s))
    return s


def time_trait(t: time) -> str:
    hr = t.hour
    for cutoff, trait in TIME_TRAITS:
        if hr < cutoff:
            return trait
    return TIME_TRAITS[-1][1]


def build_profile(data: InputData) -> Dict[str, Any]:
    data.validate()
    sign = zodiac_sign(data.birth_date)
    element = ELEMENTS[sign]
    lp = life_path_number(data.birth_date)
    ttrait = time_trait(data.birth_time)
    # A reproducible seed from name+date
    seed_str = f"{data.name.lower()}-{data.birth_date.isoformat()}"
    seed = int(hashlib.sha256(seed_str.encode()).hexdigest(), 16) % (10**8)
    age_years = relativedelta(date.today(), data.birth_date).years
    return {
        "name": data.name,
        "birth_place": data.birth_place,
        "sign": sign,
        "element": element,
        "life_path": lp,
        "time_trait": ttrait,
        "seed": seed,
        "age_years": max(0, age_years),
    }


def generate_reading(profile: Dict[str, Any]) -> str:
    sign = profile["sign"]
    element = profile["element"]
    lp = profile["life_path"]
    ttrait = profile["time_trait"]

    trait = SIGN_TRAITS.get(sign, "balanced energy")
    advice_list = ADVICE_BUCKETS[element]
    choice_idx = profile["seed"] % len(advice_list)
    advice = advice_list[choice_idx]

    lp_blurbs = {
        1: "leadership and fresh starts",
        2: "partnership and cooperation",
        3: "creativity and communication",
        4: "stability and systems",
        5: "change and exploration",
        6: "care and responsibility",
        7: "reflection and depth",
        8: "ambition and impact",
        9: "service and completion",
        11: "intuition and insight",
        22: "vision and building",
        33: "service through creativity",
    }
    lp_note = lp_blurbs.get(lp, "growth")

    lines = [
        f"• Sun sign: {sign} ({element} element) — {trait}.",
        f"• Life path {lp}: a theme of {lp_note}.",
        f"• Your natural rhythm leans toward {ttrait}.",
        "\nFocus for you:",
        f"→ {advice}",
    ]
    return "\n".join(lines)


def answer_question(question: str, profile: Dict[str, Any]) -> str:
    q = question.strip().lower()
    sign = profile["sign"]
    element = profile["element"]
    lp = profile["life_path"]

    # simplistic intent buckets
    if any(w in q for w in ["career", "job", "work", "promotion"]):
        tip = {
            "Fire": "act boldly on one opportunity; follow up within 48 hours",
            "Earth": "map a 2-week plan and ship one concrete deliverable",
            "Air": "pitch your ideas to a mentor; refine with feedback",
            "Water": "trust rapport—nurture a key relationship this week",
        }[element]
        return (
            f"Career insight for a {sign}: prioritize momentum over perfection.\n"
            f"Practical nudge: {tip}."
        )

    if any(w in q for w in ["love", "relationship", "partner", "marriage", "dating"]):
        tip = {
            "Fire": "plan a playful micro-adventure",
            "Earth": "express care through a reliable act",
            "Air": "share a thoughtful conversation starter",
            "Water": "create a cozy space to open up",
        }[element]
        return (
            f"Matters of the heart for a {sign}: lead with presence and honesty.\n"
            f"Gentle guidance: {tip}."
        )

    if any(w in q for w in ["health", "stress", "energy", "sleep", "wellbeing"]):
        tip = {
            "Fire": "10-minute high-energy movement",
            "Earth": "consistent bedtime and hydration",
            "Air": "mind dump to clear mental loops",
            "Water": "slow breath and soothing music",
        }[element]
        return (
            f"Wellbeing for a {sign}: listen to your body's signals.\n"
            f"Today’s anchor: {tip}."
        )

    # fallback
    generic = {
        "Fire": "Take one inspired step and observe the result.",
        "Earth": "Simplify one thing; consistency will open doors.",
        "Air": "Ask a better question; clarity invites direction.",
        "Water": "Honor your feelings; softness can be strong.",
    }[element]
    return (
        f"For a {sign}, the path clears as you act with intention.\n"
        f"Guidance: {generic}"
    )
