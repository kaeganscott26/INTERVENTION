#!/usr/bin/env python3
"""
Add/refresh Obsidian graph links at the bottom of every INTERVENTION chapter.

Why this exists:
- Obsidian graph view does not recognize [{Chapter 01}] as a note link.
- Obsidian graph view DOES recognize [[Chapter 01]] style wikilinks.
- This script adds a stable Ripple Links block to each chapter so the repo graph
  can visually express the theory: order, echo, artifact, return current.

Run from the repo root:

    python3 scripts/add_obsidian_ripple_links.py

Then commit the updated chapter files:

    git add "INTERVENTION ARG" scripts/add_obsidian_ripple_links.py
    git commit -m "docs: connect chapters for Obsidian graph"
    git push origin main
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_DIR = ROOT / "INTERVENTION ARG"

START = "<!-- RIPPLE_LINKS_START -->"
END = "<!-- RIPPLE_LINKS_END -->"

CORE_LINKS = [
    "[[ORDER]]",
    "[[HOW_TO_PLAY]]",
    "[[THEORY_LAYER]]",
    "[[GEOMETRY_AS_CONSEQUENCE]]",
]

SAFETY_LINKS = [
    "[[MENTAL_HEALTH_DISCLAIMER]]",
    "[[BOUNDARIES]]",
]

# These are intentionally meaning-based, not random. The previous/next links
# create the ordered expansion. The echoes/artifacts create the sideways
# interference pattern. Chapter 17 returns to Chapter 01 to create re-entry,
# not a flat loop.
LINK_MAP = {
    "Prologue.md": {
        "prev": "[[README]]",
        "next": "[[Chapter 01]]",
        "echoes": ["[[ARTIFACT_017_CURATOR'S_LAYER]]", "[[THEORY_LAYER]]"],
        "role": "doorway before the first room",
    },
    "Chapter 01.md": {
        "prev": "[[Prologue]]",
        "next": "[[Chapter 02]]",
        "echoes": ["[[ARTIFACT_017_CURATOR'S_LAYER]]", "[[ARTIFACT_020_THE SPLIT LAYER]]"],
        "role": "first ripple / adoption / origin architecture",
    },
    "Chapter 02.md": {
        "prev": "[[Chapter 01]]",
        "next": "[[Chapter 03]]",
        "echoes": ["[[ARTIFACT_021_THE_IGNORED_LAYER]]", "[[MENTAL_HEALTH_DISCLAIMER]]"],
        "role": "trigger / gap between impulse and action",
    },
    "Chapter 03.md": {
        "prev": "[[Chapter 02]]",
        "next": "[[Chapter 04]]",
        "echoes": ["[[THEORY_LAYER]]", "[[ARTIFACT_020_THE SPLIT LAYER]]"],
        "role": "room architecture / behavior made sensible by environment",
    },
    "Chapter 04.md": {
        "prev": "[[Chapter 03]]",
        "next": "[[Chapter 05]]",
        "echoes": ["[[ARTIFACT_017_CURATOR'S_LAYER]]", "[[ARTIFACT_020_THE SPLIT LAYER]]"],
        "role": "missed intervention / hidden fork",
    },
    "Chapter 05.md": {
        "prev": "[[Chapter 04]]",
        "next": "[[Chapter 06]]",
        "echoes": ["[[COMMUNITY_RIPPLES]]", "[[THEORY_LAYER]]"],
        "role": "shared reality / social rendering layer",
    },
    "Chapter 06.md": {
        "prev": "[[Chapter 05]]",
        "next": "[[Chapter 07]]",
        "echoes": ["[[ARTIFACT_021_THE_IGNORED_LAYER]]", "[[MENTAL_HEALTH_DISCLAIMER]]", "[[BOUNDARIES]]"],
        "role": "false world / danger of mistaking pattern for command",
    },
    "Chapter 07.md": {
        "prev": "[[Chapter 06]]",
        "next": "[[Chapter 08]]",
        "echoes": ["[[chapter_07_read_aloud_failure]]", "[[THEORY_LAYER]]"],
        "role": "observer / broadcast / perception as public architecture",
    },
    "Chapter 08.md": {
        "prev": "[[Chapter 07]]",
        "next": "[[Chapter 09]]",
        "echoes": ["[[ARTIFACT_017_CURATOR'S_LAYER]]", "[[ARTIFACT_020_THE SPLIT LAYER]]"],
        "role": "0826 / fatherhood / signal aimed at love",
    },
    "Chapter 09.md": {
        "prev": "[[Chapter 08]]",
        "next": "[[Chapter 10]]",
        "echoes": ["[[ARTIFACT_020_THE SPLIT LAYER]]", "[[COMMUNITY_RIPPLES]]"],
        "role": "kitchen / work pressure / rooms changing people",
    },
    "Chapter 10.md": {
        "prev": "[[Chapter 09]]",
        "next": "[[Chapter 11]]",
        "echoes": ["[[ARTIFACT_017_CURATOR'S_LAYER]]", "[[GEOMETRY_AS_CONSEQUENCE]]"],
        "role": "signal / music / uploaded consequence",
    },
    "Chapter 11.md": {
        "prev": "[[Chapter 10]]",
        "next": "[[Chapter 12]]",
        "echoes": ["[[ARTIFACT_020_THE SPLIT LAYER]]", "[[THEORY_LAYER]]"],
        "role": "loop / repeated pattern / intervention before repetition",
    },
    "Chapter 12.md": {
        "prev": "[[Chapter 11]]",
        "next": "[[Chapter 13]]",
        "echoes": ["[[GEOMETRY_AS_CONSEQUENCE]]", "[[ARTIFACT_017_CURATOR'S_LAYER]]"],
        "role": "door / threshold / choice as passage",
    },
    "Chapter 13.md": {
        "prev": "[[Chapter 12]]",
        "next": "[[Chapter 14]]",
        "echoes": ["[[COMMUNITY_RIPPLES]]", "[[CHANGELOG]]"],
        "role": "echo / phrase becoming public signal",
    },
    "Chapter 14.md": {
        "prev": "[[Chapter 13]]",
        "next": "[[Chapter 15]]",
        "echoes": ["[[GEOMETRY_AS_CONSEQUENCE]]", "[[THEORY_LAYER]]", "[[CHANGELOG]]"],
        "role": "cosmic room / expansion / first ripple scaled outward",
    },
    "Chapter 15.md": {
        "prev": "[[Chapter 14]]",
        "next": "[[Chapter 16]]",
        "echoes": ["[[GEOMETRY_AS_CONSEQUENCE]]", "[[ARTIFACT_021_THE_IGNORED_LAYER]]"],
        "role": "boulder / weight / consequence made visible",
    },
    "Chapter 16.md": {
        "prev": "[[Chapter 15]]",
        "next": "[[Chapter 17]]",
        "echoes": ["[[ARTIFACT_017_CURATOR'S_LAYER]]", "[[ARTIFACT_021_THE_IGNORED_LAYER]]"],
        "role": "morning after the signal / the thing under the thing",
    },
    "Chapter 17.md": {
        "prev": "[[Chapter 16]]",
        "next": "[[Chapter 01]]",
        "echoes": ["[[README]]", "[[ARTIFACT_017_CURATOR'S_LAYER]]", "[[ARTIFACT_020_THE SPLIT LAYER]]", "[[GEOMETRY_AS_CONSEQUENCE]]"],
        "role": "return current / Teodor / re-entry through origin",
    },
}


def format_links(filename: str, data: dict[str, object]) -> str:
    echoes = data.get("echoes", [])
    if not isinstance(echoes, list):
        echoes = []

    lines = [
        "",
        "---",
        START,
        "",
        "## 🌀 Ripple Links",
        "",
        f"- **Room function:** {data['role']}",
        f"- **Previous room:** {data['prev']}",
        f"- **Next room:** {data['next']}",
        f"- **Canon path:** {' · '.join(CORE_LINKS)}",
        f"- **Safety frame:** {' · '.join(SAFETY_LINKS)}",
    ]

    if echoes:
        lines.append(f"- **Echo / artifact links:** {' · '.join(echoes)}")

    if filename == "Chapter 17.md":
        lines.append("- **Return current:** [[Chapter 17]] → [[Chapter 01]] → [[README]]")

    lines += [
        "",
        "> A loop repeats. A torus circulates. This link block is part of the graph becoming the theory.",
        "",
        END,
        "",
    ]
    return "\n".join(lines)


def replace_or_append(content: str, block: str) -> str:
    if START in content and END in content:
        before = content.split(START, 1)[0].rstrip()
        after = content.split(END, 1)[1].lstrip()
        return f"{before}\n{block}{after}"
    return content.rstrip() + "\n" + block


def main() -> None:
    changed = []
    for filename, data in LINK_MAP.items():
        path = CHAPTER_DIR / filename
        if not path.exists():
            print(f"SKIP missing: {path}")
            continue
        original = path.read_text(encoding="utf-8")
        block = format_links(filename, data)
        updated = replace_or_append(original, block)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed.append(filename)

    if changed:
        print("Updated Ripple Links in:")
        for name in changed:
            print(f"- {name}")
    else:
        print("No chapter link blocks changed.")


if __name__ == "__main__":
    main()
