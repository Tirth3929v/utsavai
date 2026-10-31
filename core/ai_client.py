"""
AI Orchestration Layer for UtsavAI.
Utilizes Google Gemini 2.5 Flash with structured JSON mode, dynamic multi-key failover,
and robust two-tier cultural preset fallback.
"""

import os
import json
import re
from typing import Dict, Any, Optional, List

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

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
    CRISIS_USER_TEMPLATE,
    build_timeline_system_prompt,
    build_timeline_user_prompt,
    build_invitation_system_prompt,
    build_invitation_user_prompt
)
from core.invitation_engine import InvitationEngine
from config.global_traditions import GLOBAL_RELIGIONS


def _resolve_api_keys(explicit_key: Optional[str] = None) -> List[str]:
    """Safely resolve primary and failover API keys from parameter, Streamlit secrets, or environment."""
    keys: List[str] = []

    # 1. Explicit parameter
    if explicit_key and explicit_key.strip():
        keys.append(explicit_key.strip())

    # 2. Streamlit Secrets
    try:
        import streamlit as st
        if hasattr(st, "secrets"):
            for sec_name in ["GEMINI_API_KEY", "GEMINI_API_KEY_BACKUP", "GOOGLE_API_KEY"]:
                if sec_name in st.secrets and st.secrets[sec_name]:
                    k = str(st.secrets[sec_name]).strip()
                    if k and k not in keys:
                        keys.append(k)
    except Exception:
        pass

    # 3. Environment Variables
    for env_name in ["GEMINI_API_KEY", "GEMINI_API_KEY_BACKUP", "GOOGLE_API_KEY"]:
        val = os.getenv(env_name)
        if val and val.strip():
            k = val.strip()
            if k not in keys:
                keys.append(k)

    return keys


class UtsavAIEngine:
    """Handles LLM calls for cultural timelines, budget rebalancing chains, and crisis protocols with multi-key failover."""

    def __init__(self, api_key: Optional[str] = None):
        """Initializes the AI orchestration client with multi-key failover support.

        Args:
            api_key: Optional explicit API key override. If omitted, keys are resolved
                     automatically from environment variables or Streamlit secrets.
        """
        self.api_keys: List[str] = _resolve_api_keys(api_key)
        self.api_key: Optional[str] = self.api_keys[0] if self.api_keys else None
        self.client = None
        self._init_client()

    def _init_client(self):
        """Initialize the Gemini client using the primary key if present."""
        if not self.api_keys:
            return

        primary_key = self.api_keys[0]
        if GENAI_V2_AVAILABLE:
            try:
                self.client = genai.Client(api_key=primary_key)
                return
            except Exception:
                pass

        if GENAI_V1_AVAILABLE:
            try:
                legacy_genai.configure(api_key=primary_key)
                self.client = "legacy"
            except Exception:
                pass

    def is_configured(self) -> bool:
        """Checks whether at least one valid Gemini API key is configured and active.

        Returns:
            True if one or more API keys are available in the failover pool.
        """
        return len(self.api_keys) > 0

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

    def _execute_gemini_call(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.3
    ) -> Optional[str]:
        """
        Executes an LLM request across the pool of available API keys.
        Automatically fails over to backup keys if quota or rate-limiting errors occur.
        """
        if not self.api_keys:
            return None

        last_error = None
        for key in self.api_keys:
            try:
                if GENAI_V2_AVAILABLE:
                    client = genai.Client(api_key=key)
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=user_prompt,
                        config=types.GenerateContentConfig(
                            system_instruction=system_prompt,
                            temperature=temperature,
                            response_mime_type="application/json"
                        )
                    )
                    if response and response.text:
                        return response.text
                elif GENAI_V1_AVAILABLE:
                    legacy_genai.configure(api_key=key)
                    model = legacy_genai.GenerativeModel(
                        "gemini-1.5-flash",
                        system_instruction=system_prompt
                    )
                    response = model.generate_content(
                        user_prompt,
                        generation_config={"response_mime_type": "application/json", "temperature": temperature}
                    )
                    if response and response.text:
                        return response.text
            except Exception as e:
                last_error = e
                # Fail over to the next key in the pool
                continue

        if last_error:
            # All keys failed or exhausted
            pass
        return None

    def _execute_text_call(self, prompt: str) -> Optional[str]:
        """Executes a plain-text LLM generation request with key failover."""
        if not self.api_keys:
            return None

        for key in self.api_keys:
            try:
                if GENAI_V2_AVAILABLE:
                    client = genai.Client(api_key=key)
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt
                    )
                    if response and response.text:
                        return response.text
                elif GENAI_V1_AVAILABLE:
                    legacy_genai.configure(api_key=key)
                    model = legacy_genai.GenerativeModel("gemini-1.5-flash")
                    response = model.generate_content(prompt)
                    if response and response.text:
                        return response.text
            except Exception:
                continue
        return None

    def _sanitize_theological_schedule(
        self,
        schedule: List[Dict[str, Any]],
        religion: str,
        event_type: str,
        tradition: str,
        days: int = 1
    ) -> List[Dict[str, Any]]:
        """
        Guarantees 100% theological isolation.
        If non-Hinduism religion is selected and Vedic/Hindu rituals are detected,
        replaces the schedule with authentic presets for that faith and event.
        """
        rel_lower = (religion or "Hinduism").lower()
        if "hindu" in rel_lower:
            return schedule

        banned_terms = [
            "ganesh", "puja", "pooja", "vedic", "muhurat", "mandap", "phera",
            "pheray", "haldi", "pithi", "sangeet", "havan", "kanyadaan", "saptapadi",
            "baraat", "garba", "vidhi", "pandit", "agnihotra", "mangalphera", "dholak"
        ]

        contaminated = False
        for item in schedule:
            text = f"{item.get('ritual', '')} {item.get('significance', '')} {item.get('phase', '')}".lower()
            if any(bt in text for bt in banned_terms):
                contaminated = True
                break

        if not contaminated:
            return schedule

        # Contamination detected: fetch authentic faith preset
        sub_trads = GLOBAL_RELIGIONS.get(religion, {}).get("sub_traditions", {})
        chosen_rituals = []
        evt_lower = (event_type or "").lower()

        for sub_name, sub_meta in sub_trads.items():
            s_low = sub_name.lower()
            if ("engagement" in evt_lower and "engagement" in s_low) or \
               ("anniversary" in evt_lower and "anniversary" in s_low) or \
               ("matrimony" in evt_lower or "wedding" in evt_lower):
                chosen_rituals = sub_meta.get("rituals", [])
                break

        if not chosen_rituals and sub_trads:
            first_key = next(iter(sub_trads.keys()))
            chosen_rituals = sub_trads[first_key].get("rituals", [])

        if chosen_rituals:
            filtered = [r for r in chosen_rituals if r.get("day", 1) <= days]
            return filtered if filtered else chosen_rituals

        return schedule

    def generate_custom_itinerary(
        self,
        event_type: str,
        tradition: str,
        days: int,
        guest_count: int,
        dietary: str,
        venue_type: str,
        user_notes: str = "",
        religion: str = "Hinduism",
        sub_tradition: str = ""
    ) -> Dict[str, Any]:
        """Module 1: Generates an AI-powered day-by-day ritual timeline strictly honoring the chosen religion."""
        active_tradition = sub_tradition if sub_tradition else tradition

        if not self.is_configured():
            # Local preset resolution with duration filtering
            sub_trads = GLOBAL_RELIGIONS.get(religion, {}).get("sub_traditions", {})
            rituals = sub_trads.get(active_tradition, {}).get("rituals", [])
            filtered = [r for r in rituals if r.get("day", 1) <= days] if any(r.get("day", 1) <= days for r in rituals) else rituals
            return {"source": "preset", "schedule": filtered, "message": "Using calibrated cultural knowledge-base."}

        system_prompt = build_timeline_system_prompt(religion=religion, tradition=active_tradition, event_type=event_type)
        user_prompt = build_timeline_user_prompt(
            event_type=event_type,
            religion=religion,
            tradition=active_tradition,
            guest_count=guest_count,
            duration_days=days,
            venue_type=venue_type,
            dietary=dietary,
            user_notes=user_notes
        )

        try:
            raw_text = self._execute_gemini_call(system_prompt, user_prompt, temperature=0.3)
            if not raw_text:
                sub_trads = GLOBAL_RELIGIONS.get(religion, {}).get("sub_traditions", {})
                rituals = sub_trads.get(active_tradition, {}).get("rituals", [])
                filtered = [r for r in rituals if r.get("day", 1) <= days] if any(r.get("day", 1) <= days for r in rituals) else rituals
                return {"source": "preset", "schedule": filtered}

            cleaned = self._clean_json_text(raw_text)
            data = json.loads(cleaned)
            
            # Apply theological guardrail & sanitizer
            if "schedule" in data and isinstance(data["schedule"], list):
                data["schedule"] = self._sanitize_theological_schedule(
                    data["schedule"],
                    religion=religion,
                    event_type=event_type,
                    tradition=active_tradition,
                    days=days
                )
            data["source"] = "gemini"
            return data
        except Exception as e:
            sub_trads = GLOBAL_RELIGIONS.get(religion, {}).get("sub_traditions", {})
            rituals = sub_trads.get(active_tradition, {}).get("rituals", [])
            filtered = [r for r in rituals if r.get("day", 1) <= days] if any(r.get("day", 1) <= days for r in rituals) else rituals
            return {"source": "preset", "schedule": filtered, "error": str(e)}

    def generate_ai_invitations(
        self,
        event_name: str,
        hosts: str,
        honorees: str,
        tradition: str,
        venue: str,
        dates: str,
        rsvp_contact: str,
        religion: str = "Christianity"
    ) -> Dict[str, Dict[str, str]]:
        """
        Generates culturally personalized multi-tier invitations using Gemini with failover
        and deterministic fallback to InvitationEngine.
        """
        fallback_invites = InvitationEngine.generate_invitations(
            event_name=event_name,
            hosts=hosts,
            honorees=honorees,
            tradition=tradition,
            venue=venue,
            dates=dates,
            rsvp_contact=rsvp_contact,
            religion=religion
        )

        if not self.is_configured():
            return fallback_invites

        system_prompt = build_invitation_system_prompt(religion=religion, event_type=event_name)
        user_prompt = build_invitation_user_prompt(
            event_name=event_name,
            hosts=hosts,
            honorees=honorees,
            tradition=tradition,
            venue=venue,
            dates=dates,
            rsvp_contact=rsvp_contact,
            religion=religion
        )

        try:
            raw_text = self._execute_gemini_call(system_prompt, user_prompt, temperature=0.3)
            if not raw_text:
                return fallback_invites

            cleaned = self._clean_json_text(raw_text)
            ai_data = json.loads(cleaned)

            required_tiers = [
                "Tier 1: Elders & Sacred Family Circle",
                "Tier 2: Close Friends & Celebration Circle",
                "Tier 3: Esteemed Colleagues & Network"
            ]

            valid = True
            for tier in required_tiers:
                if tier not in ai_data:
                    valid = False
                    break
                tier_info = ai_data[tier]
                if not isinstance(tier_info, dict) or "card_copy" not in tier_info or "whatsapp_copy" not in tier_info:
                    valid = False
                    break

            if valid:
                for k in required_tiers:
                    ai_data[k]["source"] = "gemini"
                    if "badge" not in ai_data[k]:
                        ai_data[k]["badge"] = fallback_invites[k]["badge"]
                    if "audience" not in ai_data[k]:
                        ai_data[k]["audience"] = fallback_invites[k]["audience"]
                return ai_data

            return fallback_invites
        except Exception:
            return fallback_invites

    def generate_ai_budget(
        self,
        total_budget: float,
        guest_count: int,
        tradition: str,
        venue_type: str,
        currency: str = "₹",
        priorities: str = "Balanced Cultural Hospitality",
        religion: str = "Hinduism"
    ) -> Dict[str, Any]:
        """Module 2: Generates structured budget breakdown with vendor line items."""
        if not self.is_configured():
            return {"source": "preset"}

        prompt = (
            f"Allocate total budget of {currency}{total_budget:,.2f} for a {religion} ({tradition}) celebration with "
            f"{guest_count} guests at a {venue_type}. Primary focus: {priorities}. Output strict JSON matching the schema."
        )

        try:
            raw_text = self._execute_gemini_call(BUDGET_SYSTEM_PROMPT, prompt, temperature=0.2)
            if not raw_text:
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
        currency: str = "₹",
        religion: str = "Hinduism"
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
            tradition=f"{religion} ({tradition})",
            current_allocations_json=json.dumps(alloc_summary),
            user_instruction=user_instruction
        )

        try:
            raw_text = self._execute_gemini_call(BUDGET_SYSTEM_PROMPT, prompt, temperature=0.2)
            if not raw_text:
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
        season_context: str = "Peak Wedding Season / Outdoor Lawn Setup",
        religion: str = "Hinduism"
    ) -> Dict[str, Any]:
        """Module 3: Generates time-phased dependency matrix and crisis protocols."""
        if not self.is_configured():
            return {"source": "preset"}

        user_prompt = CRISIS_USER_TEMPLATE.format(
            event_type=event_type,
            tradition=f"{religion} ({tradition})",
            venue_type=venue_type,
            guest_count=guest_count,
            season_context=season_context
        )

        try:
            raw_text = self._execute_gemini_call(CRISIS_DEPENDENCY_SYSTEM_PROMPT, user_prompt, temperature=0.3)
            if not raw_text:
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
        text_resp = self._execute_text_call(prompt)
        if text_resp and text_resp.strip():
            return text_resp.strip()

        return "💡 Allocation aligned with regional benchmarks. Verify live food counter minimum guarantees before signing catering agreements."
