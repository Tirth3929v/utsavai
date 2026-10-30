"""Itinerary management, ritual calculations, and markdown export engine for UtsavAI."""

from typing import List, Dict, Any
import json

class ItineraryEngine:
    """Manages multi-day ritual schedules, custom ceremonies, and export formatting."""

    @classmethod
    def export_markdown(
        cls,
        event_name: str,
        tradition: str,
        start_date: str,
        duration: int,
        schedule: List[Dict[str, Any]]
    ) -> str:
        """Generate a structured, printable Markdown document."""
        md_lines = [
            f"# 🪔 {event_name} – Auspicious Master Itinerary",
            f"**Culture / Sub-Tradition:** {tradition}  ",
            f"**Commencement Date:** {start_date}  ",
            f"**Event Duration:** {duration} Days  ",
            "\n---\n"
        ]

        days = sorted(list(set(item.get("day", 1) for item in schedule)))

        for d in days:
            md_lines.append(f"## 🌅 Day {d} Schedule\n")
            day_rituals = [r for r in schedule if r.get("day", 1) == d]

            for idx, r in enumerate(day_rituals, 1):
                md_lines.append(f"### {idx}. {r.get('ritual', 'Ceremony')}")
                md_lines.append(f"- **⏰ Auspicious Timing:** {r.get('time', 'TBD')}")
                md_lines.append(f"- **📖 Sacred Significance:** {r.get('significance', 'N/A')}")
                md_lines.append(f"- **👗 Dress Code & Palette:** {r.get('dress_code', 'Traditional Festive')}")
                md_lines.append(f"- **📌 Operational & Setup Notes:** {r.get('notes', 'Coordinate with priest and audio crew')}")
                md_lines.append("")

            md_lines.append("---\n")

        md_lines.append("Generated with **UtsavAI – The Cultural & Multi-Scale Event Architect**")
        return "\n".join(md_lines)

    @classmethod
    def calculate_stats(cls, schedule: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Compute key summary stats from schedule."""
        days = list(set(item.get("day", 1) for item in schedule))
        return {
            "total_rituals": len(schedule),
            "days_count": len(days),
            "morning_rituals": len([r for r in schedule if "AM" in r.get("time", "")]),
            "evening_rituals": len([r for r in schedule if "PM" in r.get("time", "") and ("06:" in r.get("time", "") or "07:" in r.get("time", "") or "08:" in r.get("time", "") or "09:" in r.get("time", ""))])
        }
