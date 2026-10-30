"""AI Orchestration Layer for UtsavAI utilizing Google Gemini with fallback logic."""

import os
import json
from typing import Dict, Any, Optional

try:
    from google import genai
    from google.genai import types
    GENAI_V2_AVAILABLE = True
except ImportError:
    GENAI_V2_AVAILABLE = False

try:
    import google.generativeai as legacy_genai
    GENAI_V1_AVAILABLE = True
except ImportError:
    GENAI_V1_AVAILABLE = False


class UtsavAIEngine:
    """Handles LLM prompts for cultural timelines, budget intelligence, and copy generation."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.client = None
        self._init_client()

    def _init_client(self):
        """Initialize the Gemini client if key is present."""
        if not self.api_key:
            return

        if GENAI_V2_AVAILABLE:
            try:
                self.client = genai.Client(api_key=self.api_key)
                return
            except Exception:
                pass

        if GENAI_V1_AVAILABLE:
            try:
                legacy_genai.configure(api_key=self.api_key)
                self.client = "legacy"
            except Exception:
                pass

    def is_configured(self) -> bool:
        return self.client is not None

    def generate_custom_itinerary(
        self,
        event_type: str,
        tradition: str,
        days: int,
        guest_count: int,
        dietary: str,
        venue_type: str,
        notes: str = ""
    ) -> Dict[str, Any]:
        """Generate an AI-powered custom day-by-day ritual timeline."""
        if not self.is_configured():
            return {"source": "preset", "message": "Using calibrated cultural knowledge-base."}

        prompt = f"""
You are the world's leading Cultural Event Architect & Muhurat Specialist for large-scale Indian & fusion celebrations.
Generate a structured, authentic {days}-day itinerary for:
- Event: {event_type}
- Tradition/Culture: {tradition}
- Expected Guests: {guest_count}
- Dietary Style: {dietary}
- Venue Type: {venue_type}
- Special Notes: {notes}

Ensure every ritual includes:
1. Day number and precise auspicious timing range (e.g., '09:15 AM - 11:30 AM')
2. Ritual Name & Sacred Significance
3. Recommended Dress Code Theme & Color Palette
4. Logistical & Audio/Pooja Setup Notes

Format your output STRICTLY as a valid JSON object matching this schema:
{{
  "overview": "Short 2-sentence vision statement for this celebration",
  "schedule": [
    {{
      "day": 1,
      "time": "09:30 AM - 11:30 AM",
      "ritual": "Ceremony Name",
      "significance": "Deep cultural purpose",
      "dress_code": "Attire suggestions and palette",
      "notes": "Key samagri or coordination instructions"
    }}
  ]
}}
Do NOT wrap in markdown backticks other than valid json text.
"""
        try:
            if GENAI_V2_AVAILABLE and isinstance(self.client, genai.Client):
                response = self.client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        temperature=0.4,
                        response_mime_type="application/json"
                    )
                )
                text = response.text
            elif GENAI_V1_AVAILABLE:
                model = legacy_genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(
                    prompt,
                    generation_config={"response_mime_type": "application/json", "temperature": 0.4}
                )
                text = response.text
            else:
                return {"source": "preset"}

            # Parse JSON
            cleaned = text.strip()
            if cleaned.startswith("```json"):
                cleaned = cleaned[7:-3].strip()
            elif cleaned.startswith("```"):
                cleaned = cleaned[3:-3].strip()
            data = json.loads(cleaned)
            data["source"] = "gemini"
            return data
        except Exception as e:
            return {"source": "preset", "error": str(e)}

    def analyze_budget_insights(
        self,
        total_budget: float,
        allocations: Dict[str, Any],
        currency: str,
        guest_count: int,
        tradition: str
    ) -> str:
        """Provide intelligent financial and negotiation insights."""
        if not self.is_configured():
            cost_per_guest = total_budget / guest_count if guest_count > 0 else 0
            return (
                f"💡 **Financial Advisory Insights:**\n"
                f"- **Per Guest Investment:** {currency}{cost_per_guest:,.0f} across {guest_count} attendees.\n"
                f"- **Catering & Hospitality:** In {tradition} celebrations, catering satisfaction correlates directly with event sentiment. Ensure live counters are prioritized.\n"
                f"- **Vendor Contracting Tip:** Retain 10–15% buffer liquidity for unseasonal weather protection or extra guest plates on Day 2."
            )

        prompt = f"""
Act as a veteran event financial comptroller for high-end celebrations.
Analyze this budget breakdown:
- Total Budget: {currency}{total_budget:,.2f}
- Guest Count: {guest_count} (Cost/head: {currency}{total_budget/guest_count:,.0f})
- Tradition: {tradition}
- Category Breakdown: {json.dumps({k: v['amount'] for k, v in allocations.items()})}

Provide 3 crisp, high-impact financial optimization bullet points (Vendor negotiation hacks, high-ROI areas, and risk areas to watch).
Return clean markdown format with bold headers and emoji markers.
"""
        try:
            if GENAI_V2_AVAILABLE and isinstance(self.client, genai.Client):
                response = self.client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )
                return response.text
            elif GENAI_V1_AVAILABLE:
                model = legacy_genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt)
                return response.text
        except Exception:
            pass

        return "💡 Allocation aligned with regional benchmarks. Verify live food counter minimum guarantees before signing catering agreements."

