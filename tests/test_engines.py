"""Unit and integration validation for UtsavAI core engines."""

import os
import sys

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.budget_engine import BudgetEngine
from core.checklist_engine import ChecklistEngine
from core.itinerary_engine import ItineraryEngine
from core.invitation_engine import InvitationEngine
from core.vendor_engine import VendorEngine
from config.traditions import CULTURAL_TRADITIONS
from config.global_traditions import GLOBAL_RELIGIONS

def test_budget_initial_allocation():
    total_budget = 2000000.0  # 20 Lakhs
    allocations = BudgetEngine.calculate_initial_allocation(total_budget)
    
    allocated_sum = sum(d["amount"] for d in allocations.values())
    assert abs(allocated_sum - total_budget) < 1.0, f"Sum mismatch: {allocated_sum} vs {total_budget}"
    
    pct_sum = sum(d["percentage"] for d in allocations.values())
    assert 99.0 <= pct_sum <= 101.0, f"Percentage mismatch: {pct_sum}"

def test_budget_rebalancing_proportional():
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

def test_task_matrix_phases():
    matrix = ChecklistEngine.get_time_phased_task_matrix("Gujarati Hindu")
    assert len(matrix) >= 4, "Must contain at least 4 operational countdown phases"
    
    phases = [m["phase"] for m in matrix]
    assert any("T-60" in p or "T-30" in p for p in phases)
    assert any("T-14" in p or "T-7" in p for p in phases)
    assert any("Day-Of" in p for p in phases)

def test_crisis_protocols():
    protocols = ChecklistEngine.get_crisis_protocols()
    assert len(protocols) >= 4
    risks = [p["risk"] for p in protocols]
    assert any("Rain" in r for r in risks)
    assert any("Power" in r for r in risks)
    assert any("Surge" in r for r in risks)

def test_invitation_tiers():
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

def test_vendor_engine_global_directory():
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

def test_global_religions():
    assert len(GLOBAL_RELIGIONS) >= 6
    for rel_name, rel_data in GLOBAL_RELIGIONS.items():
        assert "calendar_system" in rel_data
        assert "dietary_standard" in rel_data
        assert "sub_traditions" in rel_data and len(rel_data["sub_traditions"]) > 0

if __name__ == "__main__":
    test_budget_initial_allocation()
    test_budget_rebalancing_proportional()
    test_task_matrix_phases()
    test_crisis_protocols()
    test_invitation_tiers()
    test_vendor_engine_global_directory()
    test_global_religions()
    print("SUCCESS: All UtsavAI engine tests passed successfully!")
