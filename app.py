"""
UtsavAI – The Cultural & Multi-Scale Event Architect
Built with Streamlit, Plotly, and Google Gemini Orchestration.
"""

import os
import json
import datetime
import pandas as pd
import streamlit as st
import plotly.express as px

from config.traditions import (
    CULTURAL_TRADITIONS,
    EVENT_TYPES,
    DIETARY_PREFERENCES,
    VENUE_TYPES
)
from config.global_traditions import GLOBAL_RELIGIONS
from core.budget_engine import BudgetEngine
from core.checklist_engine import ChecklistEngine
from core.invitation_engine import InvitationEngine
from core.itinerary_engine import ItineraryEngine
from core.vendor_engine import VendorEngine
from core.ai_client import UtsavAIEngine

# ---------------------------------------------------------
# Page Configuration & Modern Festive Theme
# ---------------------------------------------------------
st.set_page_config(
    page_title="UtsavAI – Cultural & Multi-Scale Event Architect",
    page_icon="🪔",
    layout="wide",
    initial_sidebar_state="expanded"
)

CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    h1, h2, h3, .festive-font {
        font-family: 'Cinzel', serif !important;
        letter-spacing: 0.5px;
    }

    .block-container {
        padding-top: 1.6rem;
        padding-bottom: 3.5rem;
    }

    /* Hero Card */
    .hero-card {
        background: linear-gradient(135deg, #18092B 0%, #290848 50%, #46117D 100%);
        border: 1px solid rgba(212, 175, 55, 0.45);
        border-radius: 16px;
        padding: 24px 28px;
        color: #FFFFFF;
        box-shadow: 0 10px 28px rgba(0, 0, 0, 0.4);
        margin-bottom: 22px;
        position: relative;
        overflow: hidden;
    }
    .hero-card::after {
        content: "🪔";
        position: absolute;
        right: 25px;
        top: 20px;
        font-size: 75px;
        opacity: 0.16;
    }
    .hero-title {
        font-size: 2.1rem;
        font-weight: 700;
        color: #D4AF37;
        margin-bottom: 6px;
    }
    .hero-subtitle {
        font-size: 1.02rem;
        color: #E2D9F3;
        margin-bottom: 14px;
        max-width: 85%;
    }

    /* Badges */
    .pill-badge {
        display: inline-block;
        background: rgba(212, 175, 55, 0.14);
        color: #F7E7B4;
        border: 1px solid rgba(212, 175, 55, 0.45);
        border-radius: 20px;
        padding: 4px 12px;
        font-size: 0.82rem;
        font-weight: 600;
        margin-right: 8px;
        margin-bottom: 6px;
    }

    /* Metric Cards */
    .metric-card {
        background: #111424;
        border: 1px solid #232840;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .metric-card:hover {
        border-color: #D4AF37;
        transform: translateY(-2px);
    }
    .metric-val {
        font-size: 1.6rem;
        font-weight: 700;
        color: #FFB703;
        font-family: 'Cinzel', serif;
    }
    .metric-lbl {
        font-size: 0.8rem;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-top: 4px;
    }

    /* Timeline Cards */
    .timeline-card {
        background: #121626;
        border-left: 4px solid #D4AF37;
        border-top: 1px solid #232840;
        border-right: 1px solid #232840;
        border-bottom: 1px solid #232840;
        border-radius: 0 12px 12px 0;
        padding: 18px 22px;
        margin-bottom: 14px;
    }
    .timeline-time {
        color: #FFB703;
        font-weight: 700;
        font-size: 0.92rem;
    }
    .timeline-title {
        color: #FFFFFF;
        font-size: 1.15rem;
        font-weight: 600;
        margin: 4px 0 8px 0;
    }
    .timeline-body {
        color: #CBD5E1;
        font-size: 0.93rem;
        line-height: 1.5;
    }
    .tag-dress {
        background: rgba(255, 107, 53, 0.15);
        color: #FFA578;
        border: 1px solid rgba(255, 107, 53, 0.35);
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.8rem;
    }
    .tag-notes {
        background: rgba(10, 92, 54, 0.2);
        color: #82E0AA;
        border: 1px solid rgba(10, 92, 54, 0.4);
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.8rem;
    }

    /* Crisis Cards */
    .crisis-card {
        background: #171221;
        border-left: 4px solid #EF476F;
        border-top: 1px solid #2C1A35;
        border-right: 1px solid #2C1A35;
        border-bottom: 1px solid #2C1A35;
        border-radius: 0 12px 12px 0;
        padding: 16px 20px;
        margin-bottom: 14px;
    }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #121524;
        border-radius: 8px 8px 0 0;
        padding: 10px 20px;
        color: #94A3B8;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #21193B !important;
        color: #FFD166 !important;
        border-bottom: 3px solid #D4AF37 !important;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ---------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------
def initialize_state():
    if "event_type" not in st.session_state:
        st.session_state.event_type = EVENT_TYPES[0]
    if "tradition" not in st.session_state:
        st.session_state.tradition = "Gujarati Hindu"
    if "guest_count" not in st.session_state:
        st.session_state.guest_count = 350
    if "total_budget" not in st.session_state:
        st.session_state.total_budget = 2500000.0  # ₹25 Lakhs
    if "currency" not in st.session_state:
        st.session_state.currency = "₹"
    if "event_duration" not in st.session_state:
        st.session_state.event_duration = 2
    if "start_date" not in st.session_state:
        st.session_state.start_date = datetime.date.today() + datetime.timedelta(days=90)
    if "venue_type" not in st.session_state:
        st.session_state.venue_type = VENUE_TYPES[0]
    if "dietary" not in st.session_state:
        st.session_state.dietary = DIETARY_PREFERENCES[0]
    if "host_names" not in st.session_state:
        st.session_state.host_names = "The Mehta & Shah Families"
    if "honoree_names" not in st.session_state:
        st.session_state.honoree_names = "Aarav & Ananya"
    if "venue_location" not in st.session_state:
        st.session_state.venue_location = "Royal Heritage Palace & Resorts, Udaipur"
    if "rsvp_contact" not in st.session_state:
        st.session_state.rsvp_contact = "+91 98765 43210 / celebrate@utsavai.com"
    if "selected_religion" not in st.session_state:
        st.session_state.selected_religion = "Hinduism"
    if "selected_country" not in st.session_state:
        st.session_state.selected_country = "India"
    if "selected_state" not in st.session_state:
        st.session_state.selected_state = "Gujarat"
    if "selected_city" not in st.session_state:
        st.session_state.selected_city = "Surat"

    # Allocations
    if "budget_allocations" not in st.session_state:
        trad_meta = CULTURAL_TRADITIONS.get(st.session_state.tradition, {})
        split = trad_meta.get("default_budget_split")
        st.session_state.budget_allocations = BudgetEngine.calculate_initial_allocation(
            st.session_state.total_budget,
            tradition_split=split
        )

    # Itinerary Schedule
    if "itinerary_data" not in st.session_state:
        trad_meta = CULTURAL_TRADITIONS.get(st.session_state.tradition, {})
        st.session_state.itinerary_data = trad_meta.get("rituals", [])

    # Checklists
    if "checklists" not in st.session_state:
        st.session_state.checklists = ChecklistEngine.get_default_checklists(
            st.session_state.tradition,
            st.session_state.event_type
        )

initialize_state()


# ---------------------------------------------------------
# Sidebar – Architectural Parameters
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; margin-bottom: 16px;">
            <div style="font-size: 2.3rem;">🪔</div>
            <h2 style="color: #D4AF37; margin: 0; font-size: 1.6rem;">UtsavAI</h2>
            <div style="font-size: 0.78rem; color: #94A3B8; letter-spacing: 1px;">THE CULTURAL EVENT ARCHITECT</div>
        </div>
    """, unsafe_allow_html=True)

    # Secrets Detection for Streamlit Cloud
    has_secret_key = False
    try:
        if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets and st.secrets["GEMINI_API_KEY"]:
            has_secret_key = True
    except Exception:
        pass

    with st.expander("🔑 AI Intelligence & API Keys", expanded=False):
        if has_secret_key:
            st.success("🔒 GEMINI_API_KEY detected via Streamlit Secrets!")
        api_key_input = st.text_input(
            "Google Gemini API Key",
            value="" if has_secret_key else os.getenv("GEMINI_API_KEY", ""),
            type="password",
            help="Optional. Leave blank to run in calibrated cultural preset mode, or if configured in Streamlit Cloud Secrets."
        )
        if api_key_input:
            os.environ["GEMINI_API_KEY"] = api_key_input

    st.markdown("### 🏛️ Global Heritage & Location")
    
    # Faith & World Religion Selection
    religions_list = list(GLOBAL_RELIGIONS.keys())
    selected_religion = st.selectbox(
        "Faith & Religion Tradition",
        religions_list,
        index=religions_list.index(st.session_state.selected_religion) if st.session_state.selected_religion in religions_list else 0
    )
    st.session_state.selected_religion = selected_religion

    # Sub-traditions under this religion
    sub_trad_dict = GLOBAL_RELIGIONS.get(selected_religion, {}).get("sub_traditions", {})
    sub_trad_names = list(sub_trad_dict.keys()) if sub_trad_dict else list(CULTURAL_TRADITIONS.keys())

    selected_tradition = st.selectbox(
        "Sub-Tradition / Ceremony Style",
        sub_trad_names,
        index=0 if st.session_state.tradition not in sub_trad_names else sub_trad_names.index(st.session_state.tradition)
    )

    selected_event = st.selectbox(
        "Event Type",
        EVENT_TYPES,
        index=EVENT_TYPES.index(st.session_state.event_type) if st.session_state.event_type in EVENT_TYPES else 0
    )

    # Global Location Selector
    st.markdown("### 📍 Destination & Host City")
    c_list = VendorEngine.get_supported_countries()
    sel_country = st.selectbox(
        "Country",
        c_list,
        index=c_list.index(st.session_state.selected_country) if st.session_state.selected_country in c_list else 0
    )
    st.session_state.selected_country = sel_country

    s_list = VendorEngine.get_states_for_country(sel_country)
    sel_state = st.selectbox(
        "State / Province",
        s_list,
        index=s_list.index(st.session_state.selected_state) if st.session_state.selected_state in s_list else 0
    )
    st.session_state.selected_state = sel_state

    city_list = VendorEngine.get_cities_for_state(sel_country, sel_state)
    sel_city = st.selectbox(
        "City",
        city_list,
        index=city_list.index(st.session_state.selected_city) if st.session_state.selected_city in city_list else 0
    )
    st.session_state.selected_city = sel_city

    col_cur, col_bud = st.columns([1, 2.5])
    with col_cur:
        currency = st.selectbox("Currency", ["₹", "$", "£", "AED"], index=0)
    with col_bud:
        default_val = float(st.session_state.total_budget) if currency == "₹" else 50000.0
        step_val = 50000.0 if currency == "₹" else 1000.0
        total_budget = st.number_input(
            f"Total Budget ({currency})",
            min_value=1000.0,
            value=default_val,
            step=step_val,
            format="%.0f"
        )

    col_g, col_d = st.columns(2)
    with col_g:
        guest_count = st.number_input("Guests", min_value=10, max_value=5000, value=st.session_state.guest_count, step=25)
    with col_d:
        event_duration = st.slider("Duration (Days)", min_value=1, max_value=5, value=st.session_state.event_duration)

    start_date = st.date_input("Commencement Date", value=st.session_state.start_date)

    with st.expander("🎨 Hospitality & Venue Nuances", expanded=False):
        venue_type = st.selectbox("Venue Style", VENUE_TYPES, index=0)
        dietary = st.selectbox("Culinary Directive", DIETARY_PREFERENCES, index=0)
        custom_notes = st.text_input("Special Traditions / Notes", placeholder="e.g. Include morning Anand Karaj / Sangeet garba fusion")

    st.markdown("<br>", unsafe_allow_html=True)
    architect_btn = st.button("✨ Architect Master Plan", type="primary", use_container_width=True)

    if architect_btn:
        st.session_state.event_type = selected_event
        st.session_state.tradition = selected_tradition
        st.session_state.guest_count = guest_count
        st.session_state.total_budget = total_budget
        st.session_state.currency = currency
        st.session_state.event_duration = event_duration
        st.session_state.start_date = start_date
        st.session_state.venue_type = venue_type
        st.session_state.dietary = dietary
        st.session_state.venue_location = f"{sel_city}, {sel_state}, {sel_country}"

        rel_data = GLOBAL_RELIGIONS.get(selected_religion, {}).get("sub_traditions", {})
        trad_meta = rel_data.get(selected_tradition, CULTURAL_TRADITIONS.get(selected_tradition, {}))
        split = trad_meta.get("default_budget_split")
        st.session_state.budget_allocations = BudgetEngine.calculate_initial_allocation(
            total_budget,
            tradition_split=split
        )

        ai_engine = UtsavAIEngine(api_key=api_key_input)
        if ai_engine.is_configured():
            with st.spinner("🤖 Consulting Gemini AI for culturally tailored rituals..."):
                ai_resp = ai_engine.generate_custom_itinerary(
                    selected_event,
                    selected_tradition,
                    event_duration,
                    guest_count,
                    dietary,
                    venue_type,
                    user_notes=custom_notes
                )
                if "schedule" in ai_resp and ai_resp["schedule"]:
                    st.session_state.itinerary_data = ai_resp["schedule"]
                else:
                    st.session_state.itinerary_data = trad_meta.get("rituals", [])
        else:
            st.session_state.itinerary_data = trad_meta.get("rituals", [])

        st.session_state.checklists = ChecklistEngine.get_default_checklists(
            selected_tradition,
            selected_event
        )
        st.success("✨ Master plan architected successfully!")
        st.rerun()


# ---------------------------------------------------------
# Main Body: Hero Banner & High-Level KPIs
# ---------------------------------------------------------
curr = st.session_state.currency
total_b = st.session_state.total_budget
guests = st.session_state.guest_count
days = st.session_state.event_duration
cost_per_guest = (total_b / guests) if guests > 0 else 0

st.markdown(f"""
    <div class="hero-card">
        <div class="hero-title">UtsavAI – {st.session_state.event_type}</div>
        <div class="hero-subtitle">
            Curating sacred muhurats, culturally authentic vidhis, dynamic financial balance, and tailored hospitality.
        </div>
        <div>
            <span class="pill-badge">🪔 Tradition: {st.session_state.tradition}</span>
            <span class="pill-badge">👥 Scale: {guests:,} Guests</span>
            <span class="pill-badge">📅 Duration: {days} Days</span>
            <span class="pill-badge">🏰 Venue: {st.session_state.venue_type}</span>
            <span class="pill-badge">🍲 Culinary: {st.session_state.dietary.split('(')[0].strip()}</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Top 4 KPIs with st.metric & Delta Indicators
total_allocated = sum(d["amount"] for d in st.session_state.budget_allocations.values())
var = total_b - total_allocated
days_until_event = (st.session_state.start_date - datetime.date.today()).days

with st.container(border=True):
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.metric(
            label="Total Budget vs Estimated Expenses",
            value=f"{curr}{total_b:,.0f}",
            delta="Balanced (100%)" if abs(var) < 1.0 else (f"{curr}{var:,.0f} reserve" if var > 0 else f"-{curr}{abs(var):,.0f} deficit"),
            delta_color="normal" if var >= 0 else "inverse"
        )
    with kpi2:
        st.metric(
            label="Per-Guest Investment",
            value=f"{curr}{cost_per_guest:,.0f}",
            delta=f"{guests:,} Total Guests"
        )
    with kpi3:
        rituals_count = len(st.session_state.itinerary_data)
        st.metric(
            label="Auspicious Milestones",
            value=f"{rituals_count} Vidhis",
            delta=f"{days}-Day Schedule"
        )
    with kpi4:
        start_fmt = st.session_state.start_date.strftime("%d %b %Y")
        st.metric(
            label="Shubh Muhurat Date",
            value=start_fmt,
            delta=f"T-{days_until_event} Days" if days_until_event >= 0 else "Event Passed"
        )

st.markdown("<br>", unsafe_allow_html=True)


# ---------------------------------------------------------
# Multi-Tab Navigation
# ---------------------------------------------------------
tab_itinerary, tab_budget, tab_checklists, tab_invitations, tab_directory = st.tabs([
    "📅 Master Itinerary & Muhurats",
    "💰 Smart Dynamic Budget Matrix",
    "📋 Task Dependency & Crisis Matrix",
    "💌 Personalized Invitation Suite",
    "🌐 Global Vendor & Venue Directory"
])


# =========================================================
# TAB 1: Master Itinerary & Muhurat Timeline
# =========================================================
with tab_itinerary:
    st.markdown("### 🪔 Auspicious Timeline & Ritual Architecture")
    st.caption("Synchronizing Vedic rituals, guest hospitality, setup intervals, and dress aesthetics.")

    itinerary_items = st.session_state.itinerary_data

    # Filter Bar
    all_days = sorted(list(set(item.get("day", 1) for item in itinerary_items)))
    day_options = ["All Days"] + [f"Day {d}" for d in all_days]

    col_flt1, col_flt2 = st.columns([1.5, 3.5])
    with col_flt1:
        selected_day_filter = st.selectbox("Filter Itinerary by Day", day_options, index=0)

    # Filtered list
    if selected_day_filter == "All Days":
        display_days = all_days
    else:
        target_day = int(selected_day_filter.replace("Day ", ""))
        display_days = [target_day]

    for d in display_days:
        st.markdown(f"#### 🌅 Day {d} Schedule")
        day_rituals = [r for r in itinerary_items if r.get("day", 1) == d]

        for rit in day_rituals:
            st.markdown(f"""
                <div class="timeline-card">
                    <div class="timeline-time">⏰ {rit.get('time', 'TBD')} {('• ' + rit.get('phase')) if rit.get('phase') else ''}</div>
                    <div class="timeline-title">{rit.get('ritual', 'Ceremony')}</div>
                    <div class="timeline-body">{rit.get('significance', '')}</div>
                    <div style="margin-top: 10px;">
                        <span class="tag-dress">👗 <b>Attire Vibe:</b> {rit.get('dress_code', 'Traditional Festive')}</span>
                        <span class="tag-notes" style="margin-left: 8px;">📌 <b>Operational Note:</b> {rit.get('operational_notes', rit.get('notes', 'Coordinate with priest and audio'))}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Expander to Add Custom Ritual
    with st.expander("➕ Add Custom Ceremony / Ritual", expanded=False):
        c_r1, c_r2 = st.columns(2)
        with c_r1:
            new_r_day = st.number_input("Day", min_value=1, max_value=st.session_state.event_duration, value=1)
            new_r_name = st.text_input("Ceremony Name", placeholder="e.g. Ring Ceremony / Family Dinner")
            new_r_time = st.text_input("Time Window", placeholder="e.g. 05:00 PM - 07:00 PM")
        with c_r2:
            new_r_sig = st.text_area("Significance / Purpose", placeholder="Key ceremonial or hospitality objective")
            new_r_dress = st.text_input("Dress Code", placeholder="e.g. Pastel Formals")
            new_r_notes = st.text_input("Operational Notes", placeholder="e.g. Stage lighting and acoustic mic")

        if st.button("Add Ceremony to Itinerary"):
            if new_r_name:
                st.session_state.itinerary_data.append({
                    "day": int(new_r_day),
                    "ritual": new_r_name,
                    "time": new_r_time or "TBD",
                    "significance": new_r_sig,
                    "dress_code": new_r_dress or "Festive",
                    "operational_notes": new_r_notes or "General coordination"
                })
                st.success(f"Added {new_r_name} to Day {new_r_day}!")
                st.rerun()

    # Action Toolbar: Downloads
    st.markdown("<br>", unsafe_allow_html=True)
    col_dl1, col_dl2, _ = st.columns([1.5, 1.5, 3])
    with col_dl1:
        itinerary_json = json.dumps(itinerary_items, indent=2)
        st.download_button(
            "📥 Export Itinerary (JSON)",
            data=itinerary_json,
            file_name=f"utsav_itinerary_{st.session_state.tradition.lower().replace(' ', '_')}.json",
            mime="application/json",
            use_container_width=True
        )
    with col_dl2:
        itinerary_md = ItineraryEngine.export_markdown(
            st.session_state.event_type,
            st.session_state.tradition,
            st.session_state.start_date.strftime("%B %d, %Y"),
            st.session_state.event_duration,
            itinerary_items
        )
        st.download_button(
            "📄 Export Itinerary (Markdown)",
            data=itinerary_md,
            file_name=f"utsav_itinerary_{st.session_state.tradition.lower().replace(' ', '_')}.md",
            mime="text/markdown",
            use_container_width=True
        )


# =========================================================
# TAB 2: Smart Dynamic Budget Matrix
# =========================================================
with tab_budget:
    st.markdown("### 💰 Smart Dynamic Budget Allocation & Rebalancing Engine")
    st.caption("Pillar-by-pillar capital distribution with automatic rebalancing logic and contingency buffers.")

    allocations = st.session_state.budget_allocations
    total_allocated = sum(d["amount"] for d in allocations.values())
    var = total_b - total_allocated

    # Visual Metric Cards
    with st.container(border=True):
        b_m1, b_m2, b_m3, b_m4 = st.columns(4)
        with b_m1:
            st.metric(
                "Total Target Capital",
                f"{curr}{total_b:,.0f}",
                delta="Aligned (100%)" if abs(var) < 1 else f"{curr}{var:+,.0f} Variance",
                delta_color="off" if abs(var) < 1 else ("normal" if var > 0 else "inverse")
            )
        with b_m2:
            st.metric(
                "Estimated Total Expenses",
                f"{curr}{total_allocated:,.0f}",
                delta=f"{(total_allocated/total_b)*100:.1f}% of Target" if total_b > 0 else "0%"
            )
        with b_m3:
            st.metric(
                "Per-Guest Spend",
                f"{curr}{(total_allocated/guests):,.0f}" if guests > 0 else "0",
                delta=f"{guests} Attendees"
            )
        with b_m4:
            buf_amt = allocations.get("Buffer Reserve", {}).get("amount", 0)
            st.metric(
                "Contingency Reserve",
                f"{curr}{buf_amt:,.0f}",
                delta=f"{allocations.get('Buffer Reserve', {}).get('percentage', 0)}% Liquidity"
            )

    st.markdown("<br>", unsafe_allow_html=True)

    col_chart, col_controls = st.columns([1.1, 1.2])

    with col_chart:
        st.markdown("##### 📊 Capital Allocation Breakdown")
        fig = BudgetEngine.create_donut_chart(allocations, currency_symbol=curr)
        st.plotly_chart(fig, use_container_width=True)

        total_allocated = sum(d["amount"] for d in allocations.values())
        var = total_b - total_allocated
        if abs(var) < 1.0:
            st.success(f"✅ Budget perfectly balanced to {curr}{total_b:,.0f} (100.0%)")
        elif var > 0:
            st.info(f"🛡️ Unallocated Capital Reserve: {curr}{var:,.0f}")
        else:
            st.warning(f"⚠️ Budget threshold exceeded by {curr}{abs(var):,.0f}!")

    with col_controls:
        st.markdown("##### 🎛️ Dynamic Category Overrides")
        st.caption("Override any category cost. Non-locked pillars automatically rebalance!")

        cat_names = list(allocations.keys())
        cat_to_adjust = st.selectbox("Select Pillar to Adjust", cat_names)

        curr_data = allocations[cat_to_adjust]
        new_val = st.number_input(
            f"Set {cat_to_adjust} ({curr})",
            min_value=0.0,
            value=float(curr_data["amount"]),
            step=25000.0 if curr == "₹" else 500.0,
            format="%.0f"
        )

        lock_toggle = st.checkbox("Lock this category amount", value=curr_data.get("locked", False))
        curr_data["locked"] = lock_toggle

        col_b1, col_b2 = st.columns(2)
        with col_b1:
            if st.button("⚡ Rebalance Rest Automatically", type="primary", use_container_width=True):
                reb_res = BudgetEngine.rebalance(
                    total_b,
                    allocations,
                    cat_to_adjust,
                    new_val
                )
                st.session_state.budget_allocations = reb_res["allocations"]
                st.rerun()

        with col_b2:
            if st.button("🔄 Reset to Cultural Benchmark", use_container_width=True):
                trad_meta = CULTURAL_TRADITIONS.get(st.session_state.tradition, {})
                split = trad_meta.get("default_budget_split")
                st.session_state.budget_allocations = BudgetEngine.calculate_initial_allocation(
                    total_b,
                    tradition_split=split
                )
                st.rerun()

        # Prompt Rebalance Input
        with st.expander("🤖 Rebalance via Natural Language AI Prompt", expanded=False):
            rebalance_prompt_input = st.text_input(
                "Directive",
                placeholder="e.g., Cut catering cost by 10% and allocate difference to Photography and Mandap"
            )
            if st.button("Apply AI Rebalance"):
                ai_engine = UtsavAIEngine()
                if ai_engine.is_configured() and rebalance_prompt_input:
                    with st.spinner("🤖 Recalculating allocations with Gemini..."):
                        reb_ai = ai_engine.rebalance_ai_budget(
                            total_b,
                            guests,
                            st.session_state.tradition,
                            allocations,
                            rebalance_prompt_input,
                            currency=curr
                        )
                        if "categories" in reb_ai:
                            for c_k, c_v in reb_ai["categories"].items():
                                if c_k in allocations:
                                    allocations[c_k]["amount"] = float(c_v.get("amount", allocations[c_k]["amount"]))
                                    allocations[c_k]["percentage"] = float(c_v.get("percentage", allocations[c_k]["percentage"]))
                            st.success("Rebalanced via AI prompt successfully!")
                            st.rerun()
                else:
                    st.info("💡 Enter your prompt and configure Gemini API key in sidebar to activate deep AI rebalancing.")

    # Benchmark Comparison Chart & Financial Insights
    st.markdown("---")
    col_bench, col_insights = st.columns([1.2, 1])

    with col_bench:
        st.markdown("##### 📈 Plan vs. Cultural Benchmark Comparison")
        fig_bar = BudgetEngine.create_benchmark_comparison_chart(allocations)
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_insights:
        st.markdown("##### 💡 Financial Advisory Insights")
        ai_engine = UtsavAIEngine()
        insights_text = ai_engine.analyze_budget_insights(
            total_b,
            allocations,
            curr,
            guests,
            st.session_state.tradition
        )
        st.markdown(insights_text)

    # Detailed Category Matrix Table
    st.markdown("---")
    st.markdown("##### 📋 Pillar-by-Pillar Expenditure Matrix")

    table_data = []
    for cat, d in allocations.items():
        table_data.append({
            "Pillar": f"{d['icon']} {cat}",
            f"Allocated ({curr})": f"{curr}{d['amount']:,.0f}",
            "Share (%)": f"{d['percentage']}%",
            f"Per Guest ({curr})": f"{curr}{(d['amount']/guests):,.0f}" if guests > 0 else "0",
            "Target Benchmark": f"{d['benchmark_range'][0]}% - {d['benchmark_range'][1]}%",
            "Operational Scope": d["description"],
            "Status": "🔒 Locked" if d.get("locked") else "🔄 Fluid"
        })

    df_budget = pd.DataFrame(table_data)
    st.dataframe(df_budget, use_container_width=True, hide_index=True)

    # Download CSV
    csv_data = BudgetEngine.export_csv(allocations, total_b, curr, guests)
    st.download_button(
        "📥 Download Budget Matrix (CSV)",
        data=csv_data,
        file_name="utsav_budget_matrix.csv",
        mime="text/csv"
    )

    # Cashflow & Vendor Payment Milestones
    st.markdown("---")
    st.markdown("##### ⏳ Milestone Vendor Cash-Flow Liquidity Schedule")
    milestones = BudgetEngine.get_cashflow_milestones(total_b, currency_symbol=curr)

    mcols = st.columns(len(milestones))
    for i, m in enumerate(milestones):
        with mcols[i]:
            st.markdown(f"""
                <div class="metric-card" style="text-align: left;">
                    <div style="font-weight: 700; color: #D4AF37; font-size: 0.95rem;">{m['milestone']}</div>
                    <div style="font-size: 0.8rem; color: #94A3B8; margin-bottom: 6px;">{m['timing']}</div>
                    <div class="metric-val" style="font-size: 1.3rem;">{curr}{m['amount']:,.0f}</div>
                    <div style="font-size: 0.78rem; color: #E2E8F0; margin-top: 6px;">{m['purpose']}</div>
                </div>
            """, unsafe_allow_html=True)


# =========================================================
# TAB 3: Task Dependency & Crisis Matrix
# =========================================================
with tab_checklists:
    st.markdown("### 📋 Task Dependency Matrix & Crisis Mitigation Engine")
    st.caption("Time-phased task governance, statutory clearances, vendor SLAs, and emergency crisis failovers.")

    checks = st.session_state.checklists
    task_matrix = checks.get("Time-Phased Task Matrix", [])
    crisis_protocols = checks.get("Crisis & Risk Mitigation Protocols", [])

    # Sub-tabs for clean organization
    subtab_phases, subtab_crisis, subtab_vendors, subtab_samagri = st.tabs([
        "⏳ Time-Phased Dependency Matrix",
        "🚨 Crisis & Weather Contingencies",
        "🤝 Vendor SLAs & Questionnaires",
        "🪔 Sacred Pooja & Samagri Kit"
    ])

    with subtab_phases:
        st.markdown("#### ⏳ Execution Countdown & Statutory Dependencies")
        for phase_group in task_matrix:
            with st.expander(f"{phase_group['badge']} — {phase_group['phase']}", expanded=True):
                for idx, t in enumerate(phase_group["tasks"]):
                    crit_color = "#EF476F" if t.get("criticality") == "Critical" else "#FFB703"
                    col_t1, col_t2 = st.columns([3.5, 1])
                    with col_t1:
                        c_box = st.checkbox(
                            f"**{t['task']}**",
                            value=t.get("status", False),
                            key=f"task_{phase_group['phase']}_{idx}"
                        )
                        t["status"] = c_box
                        st.caption(f"📌 **Dependency:** {t['dependency']}")
                        st.caption(f"🏛️ **Authority / Lead:** `{t['authority']}` | 🏷️ **Category:** `{t['category']}`")
                    with col_t2:
                        st.markdown(f"""
                            <div style="text-align: right; margin-top: 5px;">
                                <span style="background: rgba(212,175,55,0.15); color: {crit_color}; border: 1px solid {crit_color}; padding: 3px 8px; border-radius: 8px; font-size: 0.75rem; font-weight: 700;">
                                    {t.get('criticality', 'Normal')}
                                </span>
                                <div style="font-size: 0.8rem; color: #94A3B8; margin-top: 4px;">Deadline: <b>{t['deadline']}</b></div>
                            </div>
                        """, unsafe_allow_html=True)
                    st.markdown("<hr style='margin: 8px 0; border-color: #1F2438;'>", unsafe_allow_html=True)

    with subtab_crisis:
        st.markdown("#### 🚨 Emergency Crisis & Weather Mitigation Protocols")
        st.caption("Pre-calibrated failover runbooks to safeguard the celebration against severe disruptions.")

        for c in crisis_protocols:
            st.markdown(f"""
                <div class="crisis-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 1.1rem; font-weight: 700; color: #FFFFFF;">{c['risk']}</span>
                        <span style="background: rgba(239, 71, 111, 0.2); color: #FF7096; border: 1px solid #EF476F; padding: 2px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 700;">
                            {c['severity']}
                        </span>
                    </div>
                    <div style="color: #FFB703; font-size: 0.85rem; margin: 6px 0;"><b>Trigger Indicator:</b> {c['trigger_indicator']}</div>
                    <div style="color: #E2E8F0; font-size: 0.92rem; margin-bottom: 8px;"><b>Mitigation Protocol:</b> {c['mitigation_protocol']}</div>
                    <div style="background: #111424; padding: 10px 14px; border-radius: 8px; margin-top: 8px;">
                        <div style="font-size: 0.82rem; color: #D4AF37; font-weight: 600; margin-bottom: 4px;">⚡ Immediate Action Cues:</div>
                        {"".join([f"<div style='font-size: 0.82rem; color: #CBD5E1;'>• {step}</div>" for step in c['immediate_steps']])}
                    </div>
                    <div style="font-size: 0.8rem; color: #94A3B8; margin-top: 8px;">
                        👤 <b>Command Officer / Lead:</b> <span style="color: #F8FAFC;">{c['lead_poc']}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    with subtab_vendors:
        st.markdown("#### 🤝 Vendor Technical Questionnaires & Penalty SLAs")
        for v in checks.get("Vendor Critical Questionnaires & SLAs", []):
            with st.expander(f"📌 {v['vendor_type']}", expanded=True):
                st.markdown("**Questions to Mandate Before Signing:**")
                for q in v["questions"]:
                    st.markdown(f"- {q}")
                st.info(f"💡 **SLA Pro-Tip:** {v['sla_tip']}")

    with subtab_samagri:
        st.markdown("#### 🪔 Sacred Pooja & Samagri Kit Checklist")
        samagri_list = checks.get("Auspicious Pooja & Sacred Samagri Kit", [])
        col_s1, col_s2 = st.columns(2)
        half_len = (len(samagri_list) + 1) // 2

        with col_s1:
            for idx, item in enumerate(samagri_list[:half_len]):
                c_box = st.checkbox(f"{item['item']} `[{item['category']}]`", value=item.get("status", False), key=f"samagri_a_{idx}")
                item["status"] = c_box
        with col_s2:
            for idx, item in enumerate(samagri_list[half_len:], start=half_len):
                c_box = st.checkbox(f"{item['item']} `[{item['category']}]`", value=item.get("status", False), key=f"samagri_b_{idx}")
                item["status"] = c_box


# =========================================================
# TAB 4: Personalized Guest Tier & Invitation Suite
# =========================================================
with tab_invitations:
    st.markdown("### 💌 Personalized Multi-Tier Guest Invitation Suite")
    st.caption("Segment your guests into tiers to deliver culturally resonant, medium-specific invitations.")

    c_t1, c_t2, c_t3 = st.columns(3)
    t1_guests = int(guests * 0.20)
    t2_guests = int(guests * 0.45)
    t3_guests = guests - (t1_guests + t2_guests)

    with c_t1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-val">~{t1_guests}</div>
                <div class="metric-lbl">Tier 1: Sacred Family & Elders (20%)</div>
            </div>
        """, unsafe_allow_html=True)
    with c_t2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-val">~{t2_guests}</div>
                <div class="metric-lbl">Tier 2: Friends & Entourage (45%)</div>
            </div>
        """, unsafe_allow_html=True)
    with c_t3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-val">~{t3_guests}</div>
                <div class="metric-lbl">Tier 3: Network & Community (35%)</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("📝 Customize Invitation Details", expanded=False):
        c_h1, c_h2 = st.columns(2)
        with c_h1:
            host_in = st.text_input("Host Family Names", value=st.session_state.host_names)
            honoree_in = st.text_input("Honoree / Couple Names", value=st.session_state.honoree_names)
        with c_h2:
            venue_in = st.text_input("Venue Name & City", value=st.session_state.venue_location)
            rsvp_in = st.text_input("RSVP Phone & Email", value=st.session_state.rsvp_contact)

        if st.button("Update Invitation Copy"):
            st.session_state.host_names = host_in
            st.session_state.honoree_names = honoree_in
            st.session_state.venue_location = venue_in
            st.session_state.rsvp_contact = rsvp_in
            st.rerun()

    dates_str = f"{st.session_state.start_date.strftime('%B %d, %Y')} ({st.session_state.event_duration} Days)"
    invitations = InvitationEngine.generate_invitations(
        event_name=st.session_state.event_type,
        hosts=st.session_state.host_names,
        honorees=st.session_state.honoree_names,
        tradition=st.session_state.tradition,
        venue=st.session_state.venue_location,
        dates=dates_str,
        rsvp_contact=st.session_state.rsvp_contact
    )

    tier_tabs = st.tabs(list(invitations.keys()))

    for i, (tier_name, tier_content) in enumerate(invitations.items()):
        with tier_tabs[i]:
            st.markdown(f"#### {tier_content['badge']}")
            st.caption(f"**Target Audience:** {tier_content['audience']}")

            fmt_card, fmt_wa, fmt_email = st.tabs(["📜 Formal Digital Card Copy", "💬 WhatsApp Broadcast", "✉️ Formal Email"])

            with fmt_card:
                st.text_area("Digital Card Copy", value=tier_content["card_copy"], height=240, key=f"card_{i}")

            with fmt_wa:
                st.text_area("WhatsApp Broadcast (Formatted with Emojis & Bold)", value=tier_content["whatsapp_copy"], height=240, key=f"wa_{i}")

            with fmt_email:
                st.text_area("Email Invitation Copy", value=tier_content["email_copy"], height=240, key=f"email_{i}")


# =========================================================
# TAB 5: Global Vendor & Venue Directory Hub
# =========================================================
with tab_directory:
    st.markdown("### 🌐 Global Venue, Planner & Owner Direct Connection Hub")
    st.caption("Directly connect with venue owners, lead event planners, and banquet chefs worldwide. Real photos, verified occasion spend requirements, direct WhatsApp/Call links, and live Google Maps.")

    # Location controls bar
    c_loc1, c_loc2, c_loc3, c_loc4 = st.columns([1.2, 1.2, 1.2, 1.4])
    
    with c_loc1:
        countries_list = VendorEngine.get_supported_countries()
        curr_country = st.session_state.selected_country if st.session_state.selected_country in countries_list else countries_list[0]
        sel_country = st.selectbox("Destination Country", countries_list, index=countries_list.index(curr_country), key="tab5_country")
        st.session_state.selected_country = sel_country

    with c_loc2:
        states_list = VendorEngine.get_states_for_country(sel_country)
        curr_state = st.session_state.selected_state if st.session_state.selected_state in states_list else states_list[0]
        sel_state = st.selectbox("State / Province", states_list, index=states_list.index(curr_state), key="tab5_state")
        st.session_state.selected_state = sel_state

    with c_loc3:
        cities_list = VendorEngine.get_cities_for_state(sel_country, sel_state)
        curr_city = st.session_state.selected_city if st.session_state.selected_city in cities_list else cities_list[0]
        sel_city = st.selectbox("City", cities_list, index=cities_list.index(curr_city), key="tab5_city")
        st.session_state.selected_city = sel_city

    with c_loc4:
        cat_filter = st.selectbox(
            "Service Category",
            ["All Categories", "Venue & Banquets", "Lead Event Management", "Banquet Caterer", "Decor Architect"],
            key="tab5_category"
        )

    # Fetch directory cards (zero tokens consumed!)
    vendors = VendorEngine.fetch_vendors_and_venues(
        country=sel_country,
        state=sel_state,
        city=sel_city,
        event_type=st.session_state.event_type,
        category_filter=cat_filter,
        currency_symbol=curr
    )

    st.markdown(f"##### 📍 Showing {len(vendors)} Verified Partners in {sel_city}, {sel_state}, {sel_country}")

    for idx, v in enumerate(vendors):
        with st.container(border=True):
            col_v1, col_v2 = st.columns([1, 2.3])
            with col_v1:
                st.image(v["photo"], use_container_width=True)
                st.markdown(f"""
                    <div style="text-align: center; margin-top: 8px;">
                        <span style="background: rgba(16, 185, 129, 0.15); color: #10B981; border: 1px solid #10B981; padding: 2px 8px; border-radius: 6px; font-size: 0.78rem; font-weight: 700;">
                            ✓ Verified Partner
                        </span>
                        <div style="color: #FFB703; font-weight: 700; font-size: 0.92rem; margin-top: 4px;">
                            ★ {v['rating']} <span style="color: #94A3B8; font-weight: 400; font-size: 0.8rem;">({v['reviews_count']} reviews)</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            with col_v2:
                st.markdown(f"### {v['name']}")
                st.markdown(f"**🏷️ Role / Category:** `{v['category']}` &nbsp;|&nbsp; **👤 Owner / Contact:** **{v['owner']}** *({v['role_title']})*")
                
                # Pricing & Spend Highlight
                st.markdown(f"""
                    <div style="background: #171B2E; border-left: 3px solid #D4AF37; padding: 8px 14px; border-radius: 0 8px 8px 0; margin: 10px 0;">
                        <span style="color: #94A3B8; font-size: 0.82rem; text-transform: uppercase; letter-spacing: 0.5px;">Required Occasion Spend / Budget:</span><br/>
                        <span style="color: #FFD166; font-size: 1.25rem; font-weight: 700; font-family: 'Cinzel', serif;">{v['estimated_spend']}</span>
                        <span style="color: #CBD5E1; font-size: 0.85rem;"> • {v['pricing_unit']}</span>
                    </div>
                """, unsafe_allow_html=True)

                st.markdown(f"🏆 **Verified Track Record:** {v['projects_completed']}")
                st.markdown(f"📍 **Address / Location:** {v['address']}")
                
                # Specialties pills
                specialty_html = " ".join([f"<span class='pill-badge' style='font-size: 0.75rem; padding: 2px 8px;'>✨ {spec}</span>" for spec in v.get("specialties", [])])
                st.markdown(f"<div style='margin-bottom: 12px;'>{specialty_html}</div>", unsafe_allow_html=True)

                # Direct Connection Action Buttons
                b_c1, b_c2, b_c3, b_c4 = st.columns(4)
                with b_c1:
                    st.link_button("📞 Call Direct", v["call_link"], use_container_width=True)
                with b_c2:
                    st.link_button("💬 Chat WhatsApp", v["whatsapp_link"], use_container_width=True)
                with b_c3:
                    st.link_button("📍 Google Maps", v["maps_url"], use_container_width=True)
                with b_c4:
                    st.link_button("✉️ Email Direct", f"mailto:{v['email']}", use_container_width=True)


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #64748B; font-size: 0.85rem;">
        <b>UtsavAI</b> – GenAI Cultural & Multi-Scale Event Architect | Built for PromptWars Hackathon 2026<br>
        Empowering cultural authenticity, financial intelligence, and stress-free celebrations.
    </div>
    """,
    unsafe_allow_html=True
)
