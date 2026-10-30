"""Comprehensive smoke & verification test for UtsavAI."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.traditions import (
    CULTURAL_TRADITIONS,
    EVENT_TYPES,
    DIETARY_PREFERENCES,
    VENUE_TYPES
)
from core.budget_engine import BudgetEngine
from core.itinerary_engine import ItineraryEngine
from core.checklist_engine import ChecklistEngine
from core.invitation_engine import InvitationEngine
from core.ai_client import UtsavAIEngine

def test_full_system_smoke():
    print("[1/6] Testing Cultural Traditions Database...")
    assert len(CULTURAL_TRADITIONS) >= 5
    for name, data in CULTURAL_TRADITIONS.items():
        assert "rituals" in data and len(data["rituals"]) > 0
        assert "default_budget_split" in data
        split_sum = sum(data["default_budget_split"].values())
        assert 98 <= split_sum <= 102, f"{name} split sum invalid: {split_sum}"
    print("  -> Passed! All traditions verified.")

    print("[2/6] Testing Budget Allocation, Rebalancing & Charts...")
    budget = 3500000.0  # 35 Lakhs
    guests = 400
    allocs = BudgetEngine.calculate_initial_allocation(budget)
    assert abs(sum(d["amount"] for d in allocs.values()) - budget) < 1.0

    # Test donut chart generation
    fig_donut = BudgetEngine.create_donut_chart(allocs, currency_symbol="₹")
    assert fig_donut is not None

    # Test comparison bar chart
    fig_bar = BudgetEngine.create_benchmark_comparison_chart(allocs)
    assert fig_bar is not None

    # Test rebalancing: increase catering from ~10.5L to 14L
    reb = BudgetEngine.rebalance(budget, allocs, "Catering & Delicacies", 1400000.0)
    assert abs(reb["actual_total"] - budget) < 1.0
    assert reb["allocations"]["Catering & Delicacies"]["amount"] == 1400000.0
    assert reb["allocations"]["Catering & Delicacies"]["locked"] is True

    # Test CSV export
    csv_str = BudgetEngine.export_csv(reb["allocations"], budget, "₹", guests)
    assert "Catering & Delicacies" in csv_str and "1400000" in csv_str
    print("  -> Passed! Budget engine, math, charts, and CSV verified.")

    print("[3/6] Testing Itinerary Generation & Markdown Export...")
    guj_rituals = CULTURAL_TRADITIONS["Gujarati Hindu"]["rituals"]
    stats = ItineraryEngine.calculate_stats(guj_rituals)
    assert stats["total_rituals"] > 0
    md_doc = ItineraryEngine.export_markdown(
        "Grand Wedding",
        "Gujarati Hindu",
        "15 Dec 2026",
        2,
        guj_rituals
    )
    assert "Mandap Mahurat" in md_doc
    assert "Day 1 Schedule" in md_doc
    print("  -> Passed! Itinerary and Markdown export verified.")

    print("[4/6] Testing Task Matrix, Statutory Permits & Crisis Runbooks...")
    checklists = ChecklistEngine.get_default_checklists("Gujarati Hindu")
    assert "Time-Phased Task Matrix" in checklists
    assert "Crisis & Risk Mitigation Protocols" in checklists
    assert len(checklists["Crisis & Risk Mitigation Protocols"]) >= 4
    assert len(checklists["Vendor Critical Questionnaires & SLAs"]) >= 3
    print("  -> Passed! Checklists and crisis protocols verified.")

    print("[5/6] Testing Personalized 3-Tier Invitation Suite...")
    invites = InvitationEngine.generate_invitations(
        event_name="Grand Wedding",
        hosts="The Sharmas",
        honorees="Rohan & Priya",
        tradition="Gujarati Hindu",
        venue="Royal Palace, Udaipur",
        dates="Dec 15-17, 2026",
        rsvp_contact="+91 98765 43210"
    )
    assert len(invites) == 3
    for tier, content in invites.items():
        assert "card_copy" in content and len(content["card_copy"]) > 30
        assert "whatsapp_copy" in content and len(content["whatsapp_copy"]) > 30
        assert "email_copy" in content and len(content["email_copy"]) > 30
    print("  -> Passed! Tiered invitations verified.")

    print("[6/6] Testing AI Client Layer & Resilient Presets...")
    ai = UtsavAIEngine()
    # Should safely return presets or AI responses without crashing
    itinerary_res = ai.generate_custom_itinerary(
        "Grand Wedding",
        "Gujarati Hindu",
        2,
        350,
        "Pure Vegetarian",
        "Heritage Palace"
    )
    assert itinerary_res is not None
    assert "source" in itinerary_res
    print("  -> Passed! AI client layer resilience verified.")

    print("\n=======================================================")
    print("SUCCESS: Full system smoke test passed flawlessly!")
    print("=======================================================")

if __name__ == "__main__":
    test_full_system_smoke()
