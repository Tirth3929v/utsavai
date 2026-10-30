"""Localized Vendor, Ritual & Logistics Checklist Engine for UtsavAI."""

from typing import Dict, List, Any

class ChecklistEngine:
    """Provides actionable checklists, vendor negotiation prompts, and regulatory permit guides."""

    @classmethod
    def get_default_checklists(cls, tradition: str = "Gujarati Hindu", event_type: str = "Grand Wedding (Multi-Day)") -> Dict[str, List[Dict[str, Any]]]:
        return {
            "Mandatory Permits & Regulatory Clearances": [
                {
                    "item": "Loudspeaker & Sound Extension Permission",
                    "details": "Required from local police station/ACP for sound beyond 10:00 PM. Decibel limit compliance (typically under 55dB after hours).",
                    "authority": "Local Police Commissionerate / Collectorate",
                    "status": False,
                    "deadline": "T-15 Days"
                },
                {
                    "item": "IPRS & PPL Commercial Music Licenses",
                    "details": "Mandatory copyright licenses for playing copyrighted Bollywood / Western songs at Sangeet & Reception.",
                    "authority": "Novex Communications / Phonographic Performance Ltd",
                    "status": False,
                    "deadline": "T-10 Days"
                },
                {
                    "item": "Fire Department NOC & Havan Safety Clearance",
                    "details": "Verification of indoor/tent flame retardant fabrics, havan kund ventilation, and fire extinguisher deployment.",
                    "authority": "Municipal Fire Brigade",
                    "status": False,
                    "deadline": "T-7 Days"
                },
                {
                    "item": "DGCA Drone Airspace Clearance",
                    "details": "Ensure venue is not in a No-Fly Red Zone near defense establishments or airports.",
                    "authority": "DigitalSky / Local Air Traffic",
                    "status": False,
                    "deadline": "T-14 Days"
                },
                {
                    "item": "Valet & Traffic Parking Permission",
                    "details": "Arrangement for dedicated traffic marshals and off-street parking for 100+ vehicles.",
                    "authority": "Traffic Police Division",
                    "status": False,
                    "deadline": "T-5 Days"
                }
            ],
            "Vendor Critical Questionnaires & SLAs": [
                {
                    "vendor_type": "Caterer & Beverage Partner",
                    "questions": [
                        "Can you guarantee dedicated Jain/Satvik live counters with zero onion-garlic cross-contamination?",
                        "What is your food wastage protocol, and can surplus be channeled to local food banks?",
                        "What is the staff-to-guest ratio for live table service (recommended 1 server per 15 guests)?",
                        "Are backup gas cylinders and mobile kitchen induction units available on-site?"
                    ],
                    "sla_tip": "Include penalty clause for food delays exceeding 30 minutes beyond scheduled muhurat."
                },
                {
                    "vendor_type": "Decor & Floral Architect",
                    "questions": [
                        "What is the strike-time and setup handover window before the first ritual begins?",
                        "In case of unseasonal rain/wind, what is the storm backup plan for open-air mandaps?",
                        "Are real fresh tuberoses/marigolds guaranteed instead of artificial plastic sprays?",
                        "Is generator power backup (silent DG set) included in your quote?"
                    ],
                    "sla_tip": "Mandate photo sign-off of the sample floral centerpiece 48 hours prior."
                },
                {
                    "vendor_type": "Photography & Cinematography Crew",
                    "questions": [
                        "How many candid shooters vs traditional videographers will be deployed per ritual?",
                        "What is the turnaround time for the same-day teaser reel (ideal: 24 hours)?",
                        "Will you bring backup dual-slot camera bodies and external audio recorders for priest chants?",
                        "Do you hold all raw footage backup on cloud storage for minimum 90 days?"
                    ],
                    "sla_tip": "Tie final 20% payment to delivery of the master album and high-res raw drive."
                }
            ],
            "Auspicious Pooja & Sacred Samagri Kit": [
                {"item": "Ganesh Murti / Supari & Kalash with Mango Leaves", "category": "Sanctum", "status": False},
                {"item": "Pure Gangajal, Rose Water & Panchamrut (Milk, Curd, Ghee, Honey, Sugar)", "category": "Purification", "status": False},
                {"item": "Dry Havan Samagri, Camphor (Kapur), Sandalwood Sticks & Cow Dung Cakes", "category": "Havan", "status": False},
                {"item": "Sacred Thread (Moli/Nadachhadi), Red Cloth (Kanku Pagla), Haldi Powder & Akshat Rice", "category": "Offerings", "status": False},
                {"item": "Fresh Garlands (Jaimala) kept in cool temperature with moisture wrap", "category": "Jaimala", "status": False},
                {"item": "Dakshina Envelopes (Shagun Lifafas) with pristine currency notes", "category": "Tradition", "status": False}
            ],
            "Weather & Seasonal Contingency Kit": [
                {"item": "Transparent waterproof tarpaulin sheets on standby above open Mandap", "season": "Monsoon / Winter Dew", "status": False},
                {"item": "High-powered silent mist fans & mobile sugarcane/coconut hydration stalls", "season": "Summer", "status": False},
                {"item": "Decorative electric infrared heaters & warm Kashmiri pashmina wraps for elders", "season": "Winter", "status": False},
                {"item": "Emergency medical first-aid kit with ORS, antacids, glucose & ice bags", "season": "All Seasons", "status": False}
            ]
        }

