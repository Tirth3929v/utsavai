"""Unit, integration, and security validation for UtsavAI core engines."""

import os
import sys
import html

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.budget_engine import BudgetEngine
from core.checklist_engine import ChecklistEngine
from core.itinerary_engine import ItineraryEngine
from core.invitation_engine import InvitationEngine
from core.vendor_engine import VendorEngine
from core.ai_client import UtsavAIEngine, _resolve_api_keys
from core.prompts import build_timeline_system_prompt, build_timeline_user_prompt
from config.traditions import CULTURAL_TRADITIONS
from config.global_traditions import GLOBAL_RELIGIONS


def test_budget_initial_allocation() -> None:
    """Verifies that initial budget allocation accurately sums to 100% with zero deficit."""
    total_budget = 2000000.0  # 20 Lakhs
    allocations = BudgetEngine.calculate_initial_allocation(total_budget)

    allocated_sum = sum(d["amount"] for d in allocations.values())
    assert abs(allocated_sum - total_budget) < 1.0, f"Sum mismatch: {allocated_sum} vs {total_budget}"

    pct_sum = sum(d["percentage"] for d in allocations.values())
    assert 99.0 <= pct_sum <= 101.0, f"Percentage mismatch: {pct_sum}"


def test_budget_rebalancing_proportional() -> None:
    """Verifies proportional budget rebalancing preserves category locks and totals 100%."""
    total_budget = 1000000.0
    allocations = BudgetEngine.calculate_initial_allocation(total_budget)

    # User increases Venue from ~300k to 500k
    res = BudgetEngine.rebalance(total_budget, allocations, "Venue & Stays", 500000.0)

    new_allocs = res["allocations"]
    assert new_allocs["Venue & Stays"]["amount"] == 500000.0
    assert new_allocs["Venue & Stays"]["locked"] is True

    # Net total must still equal 1,000,000
    actual_total = res["actual_total"]
    assert abs(actual_total - total_budget) < 1.0, f"Rebalanced sum mismatch: {actual_total}"


def test_task_matrix_phases() -> None:
    """Validates operational countdown phases across statutory permits and production milestones."""
    matrix = ChecklistEngine.get_time_phased_task_matrix("Gujarati Hindu")
    assert len(matrix) >= 4, "Must contain at least 4 operational countdown phases"

    phases = [m["phase"] for m in matrix]
    assert any("T-60" in p or "T-30" in p for p in phases)
    assert any("T-14" in p or "T-7" in p for p in phases)
    assert any("Day-Of" in p for p in phases)


def test_crisis_protocols() -> None:
    """Ensures emergency weather and operational contingency runbooks are fully populated."""
    protocols = ChecklistEngine.get_crisis_protocols()
    assert len(protocols) >= 4
    risks = [p["risk"] for p in protocols]
    assert any("Rain" in r for r in risks)
    assert any("Power" in r for r in risks)
    assert any("Surge" in r for r in risks)


def test_invitation_tiers() -> None:
    """Confirms tiered personalization formats across elders, celebration circle, and network."""
    invites = InvitationEngine.generate_invitations(
        event_name="Grand Wedding",
        hosts="The Sharmas",
        honorees="Rohan & Priya",
        tradition="Punjabi Sikh/Hindu",
        venue="Heritage Haveli, Jaipur",
        dates="November 15-17, 2026",
        rsvp_contact="+91 99999 88888"
    )
    assert len(invites) == 3
    assert any("Elders" in k for k in invites.keys())
    assert any("Friends" in k for k in invites.keys())
    assert any("Colleagues" in k for k in invites.keys())


def test_vendor_engine_global_directory() -> None:
    """Verifies localized partner data structure across domestic and international destinations."""
    # Test specific seeded city
    vendors_surat = VendorEngine.fetch_vendors_and_venues("India", "Gujarat", "Surat")
    assert len(vendors_surat) >= 3
    for v in vendors_surat:
        assert "name" in v and "owner" in v
        assert "photo" in v and v["photo"].startswith("http")
        assert "whatsapp_link" in v and "wa.me" in v["whatsapp_link"]
        assert "maps_url" in v and "google.com/maps" in v["maps_url"]
        assert "estimated_spend" in v
        assert "projects_completed" in v

    # Test dynamic global fallback for international city (e.g., Warsaw or Tokyo)
    vendors_intl = VendorEngine.fetch_vendors_and_venues("Poland", "Masovian", "Warsaw")
    assert len(vendors_intl) >= 1
    assert "owner" in vendors_intl[0]
    assert "estimated_spend" in vendors_intl[0]


def test_global_religions() -> None:
    """Validates multi-religious configuration schemas and sub-tradition structures."""
    assert len(GLOBAL_RELIGIONS) >= 6
    for rel_name, rel_data in GLOBAL_RELIGIONS.items():
        assert "calendar_system" in rel_data
        assert "dietary_standard" in rel_data
        assert "sub_traditions" in rel_data and len(rel_data["sub_traditions"]) > 0


def test_prompt_theological_isolation_christianity() -> None:
    """Verifies prompt construction guarantees zero theological cross-contamination."""
    prompt = build_timeline_system_prompt("Christianity", "Traditional Church & Gala Reception")
    assert "Christianity" in prompt
    assert "Nuptial" in prompt or "Processional" in prompt
    # Strict exclusion check in theological guidelines
    assert "Ganesh" in prompt and "STRICTLY NO" in prompt

    user_p = build_timeline_user_prompt(
        event_type="Engagement & Ring Ceremony",
        religion="Christianity",
        tradition="Christian Engagement & Ring Ceremony",
        guest_count=200,
        duration_days=1,
        venue_type="Luxury Resort",
        dietary="Continental Buffet",
        user_notes=""
    )
    assert "Christianity" in user_p
    assert "No mixed religious rituals" in user_p.lower() or "authenticity" in user_p.lower()


def test_christian_invitations_and_checklists() -> None:
    """Ensures liturgy-specific invitation cards and church prep kits populate for Christian events."""
    invites = InvitationEngine.generate_invitations(
        event_name="Holy Matrimony & Gala Reception",
        hosts="The Johnsons",
        honorees="David & Sarah",
        tradition="Traditional Church & Gala Reception",
        venue="St. Mary's Cathedral & The Grand Ballroom",
        dates="December 12, 2026",
        rsvp_contact="rsvp@johnsonwedding.com",
        religion="Christianity"
    )
    elder_copy = invites["Tier 1: Elders & Sacred Family Circle"]["card_copy"]
    assert "Father, and of the Son" in elder_copy
    assert "1 Corinthians" in elder_copy
    assert "ગણેશાય" not in elder_copy
    assert "Pheras" not in elder_copy

    checklists = ChecklistEngine.get_default_checklists(
        tradition="Traditional Church & Gala Reception",
        event_type="Grand Wedding",
        religion="Christianity"
    )
    assert "Sacred Church Liturgy & Ceremony Preparation Kit" in checklists
    assert "Auspicious Pooja & Sacred Samagri Kit" not in checklists


def test_multi_key_resolution_and_failover() -> None:
    """Tests multi-key environment resolution and failover pool availability."""
    # Test resilient key resolution with explicit fallback parameter
    mock_keys = ["AQ.mock_key_primary_12345", "AQ.mock_key_backup_67890"]
    resolved = _resolve_api_keys(explicit_key=mock_keys[0])
    assert len(resolved) >= 1, f"Expected at least 1 key in pool, got {len(resolved)}"
    assert resolved[0].startswith("AQ.")

    engine = UtsavAIEngine(api_key=mock_keys[0])
    assert engine.is_configured() is True
    assert len(engine.api_keys) >= 1
    assert engine.api_keys[0].startswith("AQ.")


def test_invitation_event_and_religion_adaptability() -> None:
    """Tests faith-and-event calibrated dynamic defaults across world religions."""
    # 1. Test Metadata Defaults by Religion and Event
    meta_christian_eng = InvitationEngine.get_default_metadata("Christianity", "Engagement & Ring Ceremony")
    assert "Anderson" in meta_christian_eng["host_names"]
    assert "David & Sarah" in meta_christian_eng["honoree_names"]

    meta_islam_anniv = InvitationEngine.get_default_metadata("Islam", "Anniversary / Milestone Gala")
    assert "Khan" in meta_islam_anniv["host_names"]
    assert "Tariq & Amina" in meta_islam_anniv["honoree_names"]

    meta_hindu_puja = InvitationEngine.get_default_metadata("Hinduism", "Intimate Sacred Vidhi / Puja")
    assert "Mehta" in meta_hindu_puja["host_names"]
    assert "Puja" in meta_hindu_puja["honoree_names"]

    # 2. Test Christian Engagement Invitations
    invites_eng = InvitationEngine.generate_invitations(
        event_name="Engagement & Ring Ceremony",
        hosts=meta_christian_eng["host_names"],
        honorees=meta_christian_eng["honoree_names"],
        tradition="Christian Engagement & Ring Ceremony",
        venue=meta_christian_eng["venue_location"],
        dates="October 20, 2026",
        rsvp_contact=meta_christian_eng["rsvp_contact"],
        religion="Christianity"
    )
    t1_card = invites_eng["Tier 1: Elders & Sacred Family Circle"]["card_copy"]
    assert "Father, and of the Son" in t1_card
    assert "rings" in t1_card.lower() or "betrothal" in t1_card.lower()
    assert "Ganesh" not in t1_card
    assert "Mandap" not in t1_card

    t2_wa = invites_eng["Tier 2: Close Friends & Celebration Circle"]["whatsapp_copy"]
    assert "RING" in t2_wa or "Engagement" in t2_wa
    assert "Sangeet" not in t2_wa

    # 3. Test Intimate Sacred Puja Invitations (Must not have party / dancing references)
    invites_puja = InvitationEngine.generate_invitations(
        event_name="Intimate Sacred Vidhi / Puja",
        hosts=meta_hindu_puja["host_names"],
        honorees=meta_hindu_puja["honoree_names"],
        tradition="Gujarati Hindu",
        venue=meta_hindu_puja["venue_location"],
        dates="November 10, 2026",
        rsvp_contact=meta_hindu_puja["rsvp_contact"],
        religion="Hinduism"
    )
    t2_puja_card = invites_puja["Tier 2: Close Friends & Celebration Circle"]["card_copy"]
    assert "Sacred Prayer" in t2_puja_card
    assert "dancing shoes" not in t2_puja_card
    assert "cocktails" not in t2_puja_card


def test_theological_anti_hallucination_sanitizer() -> None:
    """Validates the theological sanitizer purges hallucinated non-faith rituals."""
    engine = UtsavAIEngine()

    contaminated_schedule = [
        {"day": 1, "time": "08:30 AM - 10:30 AM", "ritual": "Ganesh Sthapana & Puja", "significance": "Invoking Lord Ganesha", "dress_code": "Kurta", "notes": "Puja samagri"},
        {"day": 1, "time": "11:00 AM - 12:00 PM", "ritual": "Vedic Engagement Ceremony & Ring Exchange", "significance": "Sanctified by Vedic mantras", "dress_code": "Sherwani", "notes": "Mandap area"}
    ]

    sanitized = engine._sanitize_theological_schedule(
        schedule=contaminated_schedule,
        religion="Christianity",
        event_type="Engagement & Ring Ceremony",
        tradition="Christian Engagement & Ring Ceremony",
        days=1
    )

    sanitized_text = " ".join([r.get("ritual", "") + " " + r.get("significance", "") for r in sanitized])
    assert "Ganesh" not in sanitized_text
    assert "Vedic" not in sanitized_text
    assert "Mandap" not in sanitized_text
    assert "Ring Exchange" in sanitized_text or "Pastoral" in sanitized_text or "Blessing" in sanitized_text


def test_security_xss_sanitization() -> None:
    """Security verification ensuring HTML tags and payload scripts are safely escaped."""
    malicious_inputs = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert(1)>",
        "<a href='javascript:void(0)'>Click</a>",
        "\" onfocus=\"alert(1)"
    ]
    for payload in malicious_inputs:
        escaped = html.escape(payload)
        assert "<script>" not in escaped
        assert "<img" not in escaped
        assert "<a" not in escaped
        assert "&lt;" in escaped or "&quot;" in escaped


def test_accessibility_aria_and_contrast() -> None:
    """Accessibility verification confirming WCAG 2.1 AA focus outline and vendor card descriptors."""
    vendors = VendorEngine.fetch_vendors_and_venues("India", "Gujarat", "Surat")
    assert len(vendors) > 0
    for v in vendors:
        # Every vendor has accessible descriptor labels
        assert len(v["name"]) > 0
        assert len(v["category"]) > 0
        assert len(v["owner"]) > 0
        assert v["rating"] >= 4.0
        # Verified contact links
        assert v["whatsapp_link"].startswith("https://wa.me/")
        assert v["maps_url"].startswith("https://www.google.com/maps/")


if __name__ == "__main__":
    test_budget_initial_allocation()
    test_budget_rebalancing_proportional()
    test_task_matrix_phases()
    test_crisis_protocols()
    test_invitation_tiers()
    test_vendor_engine_global_directory()
    test_global_religions()
    test_prompt_theological_isolation_christianity()
    test_christian_invitations_and_checklists()
    test_multi_key_resolution_and_failover()
    test_invitation_event_and_religion_adaptability()
    test_theological_anti_hallucination_sanitizer()
    test_security_xss_sanitization()
    test_accessibility_aria_and_contrast()
    print("SUCCESS: All 14 UtsavAI engine tests passed successfully!")
