"""
AI Orchestration Layer for UtsavAI.
Utilizes Google Gemini with structured JSON mode and robust fallback architecture.
"""

import os
import json
import re
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

from core.prompts import (
    TIMELINE_SYSTEM_PROMPT,
    TIMELINE_USER_TEMPLATE,
    BUDGET_SYSTEM_PROMPT,
    BUDGET_REBALANCE_PROMPT,
    CRISIS_DEPENDENCY_SYSTEM_PROMPT,
    CRISIS_USER_TEMPLATE
)


def _resolve_api_key(explicit_key: Optional[str] = None) -> Optional[str]:
    """Safely resolve API key from parameter, Streamlit secrets, or environment variable."""
    if explicit_key and explicit_key.strip():
        return explicit_key.strip()
    try:
        import streamlit as st
        if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
            key = st.secrets["GEMINI_API_KEY"]
            if key and key.strip():
                return key.strip()
    except Exception:
        pass
    return os.getenv("GEMINI_API_KEY")


class UtsavAIEngine:
    """Handles LLM calls for cultural timelines, budget rebalancing chains, and crisis protocols."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = _resolve_api_key(api_key)
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

    def _clean_json_text(self, text: str) -> str:
        """Strip markdown fences, whitespace, and leading/trailing non-JSON chars."""
        cleaned = text.strip()
        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]
        elif cleaned.startswith("```"):
            cleaned = cleaned[3:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        return cleaned.strip()

    def generate_custom_itinerary(
        self,
        event_type: str,
        tradition: str,
        days: int,
        guest_count: int,
        dietary: str,
        venue_type: str,
        user_notes: str = ""
    ) -> Dict[str, Any]:
        """Module 1: Generates an AI-powered day-by-day ritual timeline."""
        if not self.is_configured():
            return {"source": "preset", "message": "Using calibrated cultural knowledge-base."}

        user_prompt = TIMELINE_USER_TEMPLATE.format(
            duration_days=days,
            event_type=event_type,
            tradition=tradition,
            guest_count=guest_count,
            venue_type=venue_type,
            dietary=dietary,
            user_notes=user_notes or "Adhere strictly to auspicious Vedic muhurat traditions."
        )

        try:
            if GENAI_V2_AVAILABLE and isinstance(self.client, genai.Client):
                response = self.client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=TIMELINE_SYSTEM_PROMPT,
                        temperature=0.3,
                        response_mime_type="application/json"
                    )
                )
                raw_text = response.text
            elif GENAI_V1_AVAILABLE:
                model = legacy_genai.GenerativeModel(
                    "gemini-1.5-flash",
                    system_instruction=TIMELINE_SYSTEM_PROMPT
                )
                response = model.generate_content(
                    user_prompt,
                    generation_config={"response_mime_type": "application/json", "temperature": 0.3}
                )
                raw_text = response.text
            else:
                return {"source": "preset"}

            cleaned = self._clean_json_text(raw_text)
            data = json.loads(cleaned)
            data["source"] = "gemini"
            return data
        except Exception as e:
            return {"source": "preset", "error": str(e)}

    def generate_ai_budget(
        self,
        total_budget: float,
        guest_count: int,
        tradition: str,
        venue_type: str,
        currency: str = "₹",
        priorities: str = "Balanced Cultural Hospitality"
    ) -> Dict[str, Any]:
        """Module 2: Generates structured budget breakdown with vendor line items."""
        if not self.is_configured():
            return {"source": "preset"}

        prompt = (
            f"Allocate total budget of {currency}{total_budget:,.2f} for a {tradition} celebration with "
            f"{guest_count} guests at a {venue_type}. Primary focus: {priorities}. Output strict JSON matching the schema."
        )

        try:
            if GENAI_V2_AVAILABLE and isinstance(self.client, genai.Client):
                response = self.client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=BUDGET_SYSTEM_PROMPT,
                        temperature=0.2,
                        response_mime_type="application/json"
                    )
                )
                raw_text = response.text
            elif GENAI_V1_AVAILABLE:
                model = legacy_genai.GenerativeModel(
                    "gemini-1.5-flash",
                    system_instruction=BUDGET_SYSTEM_PROMPT
                )
                response = model.generate_content(
                    prompt,
                    generation_config={"response_mime_type": "application/json", "temperature": 0.2}
                )
                raw_text = response.text
            else:
                return {"source": "preset"}

            cleaned = self._clean_json_text(raw_text)
            data = json.loads(cleaned)
            data["source"] = "gemini"
            return data
        except Exception as e:
            return {"source": "preset", "error": str(e)}

    def rebalance_ai_budget(
        self,
        total_budget: float,
        guest_count: int,
        tradition: str,
        current_allocations: Dict[str, Any],
        user_instruction: str,
        currency: str = "₹"
    ) -> Dict[str, Any]:
        """Module 2 Chain: Rebalances budget categories based on natural language overrides."""
        if not self.is_configured():
            return {"source": "preset"}

        alloc_summary = {
            k: {"amount": v["amount"], "locked": v.get("locked", False)}
            for k, v in current_allocations.items()
        }

        prompt = BUDGET_REBALANCE_PROMPT.format(
            currency=currency,
            total_budget=total_budget,
            guest_count=guest_count,
            tradition=tradition,
            current_allocations_json=json.dumps(alloc_summary),
            user_instruction=user_instruction
        )

        try:
            if GENAI_V2_AVAILABLE and isinstance(self.client, genai.Client):
                response = self.client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=BUDGET_SYSTEM_PROMPT,
                        temperature=0.2,
                        response_mime_type="application/json"
                    )
                )
                raw_text = response.text
            elif GENAI_V1_AVAILABLE:
                model = legacy_genai.GenerativeModel(
                    "gemini-1.5-flash",
                    system_instruction=BUDGET_SYSTEM_PROMPT
                )
                response = model.generate_content(
                    prompt,
                    generation_config={"response_mime_type": "application/json", "temperature": 0.2}
                )
                raw_text = response.text
            else:
                return {"source": "preset"}

            cleaned = self._clean_json_text(raw_text)
            data = json.loads(cleaned)
            data["source"] = "gemini"
            return data
        except Exception as e:
            return {"source": "preset", "error": str(e)}

    def generate_crisis_matrix(
        self,
        event_type: str,
        tradition: str,
        venue_type: str,
        guest_count: int,
        season_context: str = "Peak Wedding Season / Outdoor Lawn Setup"
    ) -> Dict[str, Any]:
        """Module 3: Generates time-phased dependency matrix and crisis protocols."""
        if not self.is_configured():
            return {"source": "preset"}

        user_prompt = CRISIS_USER_TEMPLATE.format(
            event_type=event_type,
            tradition=tradition,
            venue_type=venue_type,
            guest_count=guest_count,
            season_context=season_context
        )

        try:
            if GENAI_V2_AVAILABLE and isinstance(self.client, genai.Client):
                response = self.client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=CRISIS_DEPENDENCY_SYSTEM_PROMPT,
                        temperature=0.3,
                        response_mime_type="application/json"
                    )
                )
                raw_text = response.text
            elif GENAI_V1_AVAILABLE:
                model = legacy_genai.GenerativeModel(
                    "gemini-1.5-flash",
                    system_instruction=CRISIS_DEPENDENCY_SYSTEM_PROMPT
                )
                response = model.generate_content(
                    user_prompt,
                    generation_config={"response_mime_type": "application/json", "temperature": 0.3}
                )
                raw_text = response.text
            else:
                return {"source": "preset"}

            cleaned = self._clean_json_text(raw_text)
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
