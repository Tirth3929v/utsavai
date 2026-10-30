"""Smart Dynamic Budget Rebalancer for UtsavAI."""

from typing import Dict, Any, List, Optional
import pandas as pd
import plotly.graph_objects as go

class BudgetEngine:
    """Manages multi-category event budget allocation and dynamic rebalancing."""

    CATEGORY_METADATA = {
        "Venue & Stays": {
            "icon": "🏰",
            "desc": "Event banquets, lawns, guest room blocks, hospitality desks",
            "benchmark_range": (28, 38),
            "benchmark_avg": 32.0
        },
        "Catering & Delicacies": {
            "icon": "🍲",
            "desc": "Live food stations, royal thali, midnight street carts, mocktails",
            "benchmark_range": (25, 35),
            "benchmark_avg": 30.0
        },
        "Decor & Mandap Art": {
            "icon": "🌺",
            "desc": "Floral mandap, fairy-light canopies, stage backdrop, photobooths",
            "benchmark_range": (14, 22),
            "benchmark_avg": 16.0
        },
        "Photography & Film": {
            "icon": "📸",
            "desc": "Candid master photographers, drone cinematographers, live stream",
            "benchmark_range": (8, 14),
            "benchmark_avg": 10.0
        },
        "Attire & Trousseau": {
            "icon": "👗",
            "desc": "Ceremonial garments, bridal lehenga, sherwani, jewelry styling",
            "benchmark_range": (5, 10),
            "benchmark_avg": 6.0
        },
        "Entertainment & Logistics": {
            "icon": "🎵",
            "desc": "Dhol artists, live folk singer/DJ, sound & lighting console, valet",
            "benchmark_range": (4, 10),
            "benchmark_avg": 4.0
        },
        "Buffer Reserve": {
            "icon": "🛡️",
            "desc": "Contingency reserve for last-minute guest surge & weather backup",
            "benchmark_range": (2, 5),
            "benchmark_avg": 2.0
        }
    }

    @classmethod
    def calculate_initial_allocation(
        cls,
        total_budget: float,
        tradition_split: Optional[Dict[str, float]] = None
    ) -> Dict[str, Dict[str, Any]]:
        """Calculate initial budget split based on tradition benchmarks."""
        if not tradition_split:
            tradition_split = {
                "Venue & Stays": 30.0,
                "Catering & Delicacies": 30.0,
                "Decor & Mandap Art": 16.0,
                "Photography & Film": 10.0,
                "Attire & Trousseau": 6.0,
                "Entertainment & Logistics": 5.0,
                "Buffer Reserve": 3.0
            }

        total_pct = sum(tradition_split.values())
        allocations = {}

        for cat, pct in tradition_split.items():
            norm_pct = (pct / total_pct) * 100.0
            amount = (norm_pct / 100.0) * total_budget
            meta = cls.CATEGORY_METADATA.get(cat, {"icon": "💼", "desc": "", "benchmark_range": (5, 30), "benchmark_avg": 10.0})
            allocations[cat] = {
                "amount": round(amount, 2),
                "percentage": round(norm_pct, 1),
                "benchmark_pct": meta.get("benchmark_avg", round(norm_pct, 1)),
                "icon": meta["icon"],
                "description": meta["desc"],
                "benchmark_range": meta["benchmark_range"],
                "locked": False
            }

        return allocations

    @classmethod
    def rebalance(
        cls,
        total_budget: float,
        current_allocations: Dict[str, Dict[str, Any]],
        modified_category: str,
        new_amount: float
    ) -> Dict[str, Any]:
        """
        Dynamically adjust non-locked categories when one category is modified.
        Ensures the total matches total_budget or explains variance.
        """
        updated = {}
        for cat, data in current_allocations.items():
            updated[cat] = data.copy()

        # Update modified category
        updated[modified_category]["amount"] = max(0.0, float(new_amount))
        updated[modified_category]["locked"] = True

        locked_sum = sum(d["amount"] for cat, d in updated.items() if d.get("locked", False))
        unlocked_cats = [cat for cat, d in updated.items() if not d.get("locked", False)]

        notes = []

        if locked_sum > total_budget:
            deficit = locked_sum - total_budget
            notes.append(f"⚠️ Budget threshold exceeded by {deficit:,.2f}! Locked categories require {locked_sum:,.2f}.")
            for cat in unlocked_cats:
                updated[cat]["amount"] = 0.0
                updated[cat]["percentage"] = 0.0
        elif not unlocked_cats:
            variance = total_budget - locked_sum
            if abs(variance) > 1.0:
                notes.append(f"All categories locked. Net variance: {variance:+,.2f}.")
        else:
            remaining_budget = total_budget - locked_sum
            base_weights = {
                cat: updated[cat]["percentage"] if updated[cat]["percentage"] > 0 else 1.0
                for cat in unlocked_cats
            }
            sum_weights = sum(base_weights.values()) or 1.0

            for cat in unlocked_cats:
                cat_share = (base_weights[cat] / sum_weights) * remaining_budget
                updated[cat]["amount"] = round(max(0.0, cat_share), 2)
            notes.append(f"✨ Dynamically rebalanced remaining {remaining_budget:,.2f} across {len(unlocked_cats)} categories.")

        actual_total = sum(d["amount"] for d in updated.values())
        effective_total = actual_total if actual_total > 0 else total_budget
        for cat, d in updated.items():
            d["percentage"] = round((d["amount"] / effective_total) * 100.0, 1)

        return {
            "allocations": updated,
            "actual_total": actual_total,
            "variance": total_budget - actual_total,
            "notes": notes
        }

    @classmethod
    def get_cashflow_milestones(cls, total_budget: float, currency_symbol: str = "₹") -> List[Dict[str, Any]]:
        """Compute vendor payment stages."""
        return [
            {"milestone": "1. Retainers & Date Locks", "timing": "T-6 to T-4 Months", "pct": 25, "amount": total_budget * 0.25, "purpose": "Lock prime venue dates, head caterer advance, key cinematographers"},
            {"milestone": "2. Production & Bespoke Orders", "timing": "T-60 to T-30 Days", "pct": 40, "amount": total_budget * 0.40, "purpose": "Mandap structure fabrication, couture garment fittings, artisan decor"},
            {"milestone": "3. 48-Hour Pre-Event Liquidity", "timing": "T-2 Days", "pct": 25, "amount": total_budget * 0.25, "purpose": "Catering inventory raw settlement, generator backup fuel, valet transport"},
            {"milestone": "4. Post-Celebration Handover", "timing": "T+3 Days Post Event", "pct": 10, "amount": total_budget * 0.10, "purpose": "Damage security deposit refunds, high-res raw drive delivery, dakshina"}
        ]

    @classmethod
    def create_donut_chart(cls, allocations: Dict[str, Dict[str, Any]], currency_symbol: str = "₹"):
        """Generate high-aesthetic Plotly donut chart."""
        labels = [f"{data['icon']} {cat}" for cat, data in allocations.items()]
        values = [data["amount"] for data in allocations.values()]

        colors = [
            "#D4AF37",  # Gold
            "#FF6B35",  # Saffron
            "#8B0000",  # Royal Maroon
            "#1E3D59",  # Deep Royal Navy
            "#0A5C36",  # Emerald Green
            "#9B5DE5",  # Royal Purple
            "#F15BB5"   # Festive Magenta
        ]

        fig = go.Figure(data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.55,
                textinfo="label+percent",
                insidetextorientation="radial",
                marker=dict(colors=colors, line=dict(color="#1a1a1a", width=2)),
                hovertemplate="<b>%{label}</b><br>Amount: " + currency_symbol + "%{value:,.0f}<br>Share: %{percent}<extra></extra>"
            )
        ])

        fig.update_layout(
            showlegend=False,
            margin=dict(t=20, b=20, l=20, r=20),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=340,
            annotations=[
                dict(
                    text=f"<b>Utsav</b><br>Matrix",
                    x=0.5, y=0.5,
                    font_size=18,
                    font_color="#D4AF37",
                    showarrow=False
                )
            ]
        )
        return fig

    @classmethod
    def create_benchmark_comparison_chart(cls, allocations: Dict[str, Dict[str, Any]]):
        """Generate a grouped bar chart comparing current plan % vs benchmark %."""
        categories = [f"{d['icon']} {cat.split('&')[0].strip()}" for cat, d in allocations.items()]
        current_pcts = [d["percentage"] for d in allocations.values()]
        benchmark_pcts = [d.get("benchmark_pct", d["percentage"]) for d in allocations.values()]

        fig = go.Figure(data=[
            go.Bar(name='Current Plan', x=categories, y=current_pcts, marker_color='#D4AF37'),
            go.Bar(name='Cultural Benchmark', x=categories, y=benchmark_pcts, marker_color='#64748B')
        ])

        fig.update_layout(
            barmode='group',
            margin=dict(t=30, b=20, l=20, r=20),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=260,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            yaxis=dict(title="Share (%)", gridcolor="#232840"),
            xaxis=dict(tickangle=-20)
        )
        return fig

    @classmethod
    def export_csv(cls, allocations: Dict[str, Dict[str, Any]], total_budget: float, currency: str, guests: int) -> str:
        """Export budget allocations to CSV string."""
        rows = []
        for cat, d in allocations.items():
            per_guest = (d["amount"] / guests) if guests > 0 else 0
            rows.append({
                "Category": cat,
                f"Allocated ({currency})": d["amount"],
                "Share (%)": d["percentage"],
                f"Per Guest ({currency})": round(per_guest, 2),
                "Benchmark Range (%)": f"{d['benchmark_range'][0]}% - {d['benchmark_range'][1]}%",
                "Status": "Locked" if d.get("locked") else "Fluid",
                "Description": d["description"]
            })
        df = pd.DataFrame(rows)
        return df.to_csv(index=False)
