"""
Localized Vendor, Ritual & Logistics Checklist Engine for UtsavAI.
Includes Time-Phased Dependency Matrix and Crisis Risk Protocols.
"""

from typing import Dict, List, Any

class ChecklistEngine:
    """Provides actionable checklists, task dependencies, vendor SLAs, and crisis failover guides."""

    @classmethod
    def get_time_phased_task_matrix(cls, tradition: str = "Gujarati Hindu", event_type: str = "Grand Wedding (Multi-Day)") -> List[Dict[str, Any]]:
        """Returns a structured, time-phased task dependency matrix."""
        return [
            {
                "phase": "T-60 to T-30 Days (Foundational & Statutory)",
                "badge": "🏛️ Foundation Phase",
                "tasks": [
                    {
                        "task": "Submit Police Loudspeaker & Night Extension Application",
                        "category": "Statutory Permit",
                        "dependency": "Requires confirmed venue contract, layout diagram, and decibel compliance undertaking.",
                        "deadline": "T-30 Days",
                        "criticality": "Critical",
                        "authority": "Local Police Commissionerate / ACP Office",
                        "status": False
                    },
                    {
                        "task": "Procure PPL & IPRS Commercial Music Licenses",
                        "category": "Legal Compliance",
                        "dependency": "Requires DJ tracklist category and expected guest headcount.",
                        "deadline": "T-25 Days",
                        "criticality": "High",
                        "authority": "Phonographic Performance Ltd & IPRS",
                        "status": False
                    },
                    {
                        "task": "Finalize Head Priest (Panditji / Granthi) & Samagri Requisition",
                        "category": "Ritual Protocol",
                        "dependency": "Align date & exact muhurat window according to planetary panchang.",
                        "deadline": "T-35 Days",
                        "criticality": "High",
                        "authority": "Family Head Priest",
                        "status": False
                    },
                    {
                        "task": "Conduct Comprehensive Menu Tasting & Jain/Satvik Counter Segregation",
                        "category": "Hospitality",
                        "dependency": "Verify separate kitchen fryers and zero onion-garlic cross-contamination setup.",
                        "deadline": "T-30 Days",
                        "criticality": "Medium",
                        "authority": "Executive Banquet Chef",
                        "status": False
                    }
                ]
            },
            {
                "phase": "T-14 to T-7 Days (Production & Final Approvals)",
                "badge": "⚡ Production Phase",
                "tasks": [
                    {
                        "task": "Inspect Fire Department NOC & Indoor Havan Kund Safety",
                        "category": "Safety Clearance",
                        "dependency": "Ensure 5kg ABC powder fire extinguishers on standby and flame-retardant fabric certs.",
                        "deadline": "T-7 Days",
                        "criticality": "Critical",
                        "authority": "Municipal Fire Brigade",
                        "status": False
                    },
                    {
                        "task": "Freeze Final Guest Headcounts with +10% Buffer with Caterer",
                        "category": "Catering Operations",
                        "dependency": "Consolidate RSVPs from Digital Invitations Suite.",
                        "deadline": "T-7 Days",
                        "criticality": "High",
                        "authority": "Catering Lead",
                        "status": False
                    },
                    {
                        "task": "Validate DGCA Drone Flight Zone (Red/Green Airspace Check)",
                        "category": "Regulatory",
                        "dependency": "Check DigitalSky portal to confirm venue is clear of military/airport no-fly zone.",
                        "deadline": "T-10 Days",
                        "criticality": "Medium",
                        "authority": "Cinematography Crew Lead",
                        "status": False
                    },
                    {
                        "task": "Rehearse Sangeet Audio-Visual Cues & Soundboard Balancing",
                        "category": "Entertainment",
                        "dependency": "Collect all pen-drives and audio cloud links in MP3/WAV format.",
                        "deadline": "T-5 Days",
                        "criticality": "Medium",
                        "authority": "DJ & Sound Console Engineer",
                        "status": False
                    }
                ]
            },
            {
                "phase": "T-48 to T-24 Hours (Rehearsals & Liquidity)",
                "badge": "⏳ 48-Hour Countdown",
                "tasks": [
                    {
                        "task": "Mandap Structural Sign-Off & Open-Air Weather Proofing",
                        "category": "Infrastructure",
                        "dependency": "Physical walkthrough of mandap pillar stability and hidden tie-down ropes.",
                        "deadline": "T-24 Hours",
                        "criticality": "Critical",
                        "authority": "Decor Fabrication Lead",
                        "status": False
                    },
                    {
                        "task": "Verify Priest Dakshina & Vendor Liquidity Envelopes",
                        "category": "Cashflow Liquidity",
                        "dependency": "Segregate pristine cash envelopes for panditji, dhol artists, and valet tips.",
                        "deadline": "T-24 Hours",
                        "criticality": "High",
                        "authority": "Family Treasury Lead",
                        "status": False
                    },
                    {
                        "task": "Cold-Chain Storage for Fresh Floral Garlands (Jaimala)",
                        "category": "Floral Care",
                        "dependency": "Store in 18°C air-conditioned bridal suite with moisture misting.",
                        "deadline": "T-12 Hours",
                        "criticality": "Medium",
                        "authority": "Bridal Attendant / Florist",
                        "status": False
                    }
                ]
            },
            {
                "phase": "Day-Of Execution (Real-Time Cues)",
                "badge": "🪔 Shubh Muhurat Day",
                "tasks": [
                    {
                        "task": "Silent Diesel Generator (DG Set) Fuel Check & Live Auto-Cutover Test",
                        "category": "Power Backup",
                        "dependency": "Ensure full fuel tank and 5-second automatic failover during sacred chants.",
                        "deadline": "Hour -3",
                        "criticality": "Critical",
                        "authority": "Venue Chief Engineer",
                        "status": False
                    },
                    {
                        "task": "Distribute Chilled Water Bottles & Hydration Wet Wipes for Baraat",
                        "category": "Guest Care",
                        "dependency": "Station mobile hospitality cart 200m before the grand arrival gate.",
                        "deadline": "Hour -1",
                        "criticality": "Medium",
                        "authority": "Hospitality Brigade",
                        "status": False
                    },
                    {
                        "task": "Place Sacred Akshat Rice & Rose Petal Cones at Every Guest Seat",
                        "category": "Vidhi Preparation",
                        "dependency": "Arrange decorated brass bowls along the mandap perimeter.",
                        "deadline": "Hour -0.5",
                        "criticality": "High",
                        "authority": "Ritual Coordinator",
                        "status": False
                    }
                ]
            }
        ]

    @classmethod
    def get_crisis_protocols(cls) -> List[Dict[str, Any]]:
        """Returns actionable contingency failover protocols for high-stakes emergencies."""
        return [
            {
                "risk": "🌧️ Unseasonal Rainstorm on Open Lawn Mandap",
                "severity": "Critical",
                "trigger_indicator": "Rain radar warning or sudden precipitation > 30 minutes before Muhurat.",
                "mitigation_protocol": "Activate pre-contracted German waterproof hangar roof or immediately transition ceremony into the pre-held indoor backup ballroom.",
                "immediate_steps": [
                    "Sound team transitions wireless microphones to indoor console in 15 mins.",
                    "Deploy water vacuum extractors and heavy rubber runner mats along the bride's entry path.",
                    "Move sacred havan kund to dedicated ventilated indoor pavilion."
                ],
                "lead_poc": "Venue Director & Mandap Decor Lead"
            },
            {
                "risk": "⚡ Sudden Main Power Grid Blackout",
                "severity": "Critical",
                "trigger_indicator": "Loss of municipal power grid supply.",
                "mitigation_protocol": "Dedicated dual 125 kVA silent diesel generators on hot-standby with automatic cut-over.",
                "immediate_steps": [
                    "Priority 1 power routed to Mandap havan lighting, altar sound, and live cameras.",
                    "Emergency battery LED uplights stationed at all exit stairways.",
                    "Keep technician stationed beside switchgear during peak rituals."
                ],
                "lead_poc": "Electrical Engineering Officer"
            },
            {
                "risk": "👥 Unregistered Guest Surge (>20% Above Guaranteed Capacity)",
                "severity": "High",
                "trigger_indicator": "Headcount counter at welcome desk crosses 90% capacity 1 hour before dining.",
                "mitigation_protocol": "Activate the Emergency Catering Scalability SLA buffer.",
                "immediate_steps": [
                    "Caterer opens 3 supplementary fast-track live bread and rice stations.",
                    "Valet marshals redirect excess vehicles to pre-contracted secondary overflow parking.",
                    "Hospitality team deploys supplementary banquet seating within 20 mins."
                ],
                "lead_poc": "Head Banquet Caterer & Valet Manager"
            },
            {
                "risk": "🚨 Police Sound Curfew Notice Post 10:00 PM",
                "severity": "High",
                "trigger_indicator": "Local police patrol inspection or decibel warning.",
                "mitigation_protocol": "Seamless transition from outdoor high-wattage line array to Indoor Silent Headphone Party or Acoustic Lounge.",
                "immediate_steps": [
                    "Kill exterior subwoofers precisely at 09:55 PM.",
                    "Shift late-night Sangeet after-party into the insulated indoor soundproof club lounge.",
                    "Display approved police loudspeaker permit copy at main security entrance."
                ],
                "lead_poc": "Show Director & Security Head"
            },
            {
                "risk": "🔥 Havan Flame Smoke or Fabric Proximity Hazard",
                "severity": "Critical",
                "trigger_indicator": "Excessive smoke plume or high flame near decorative drape fabric.",
                "mitigation_protocol": "Pre-treated fire-retardant fabric mandate and certified havan smoke exhaust.",
                "immediate_steps": [
                    "Priest adjusts ghee pouring rate and uses low-smoke samagri wood.",
                    "Overhead industrial smoke ventilator activated.",
                    "Water spray mist and clean sand buckets stationed behind priest seating."
                ],
                "lead_poc": "Safety Marshall & Panditji Coordinator"
            }
        ]

    @classmethod
    def get_default_checklists(cls, tradition: str = "Gujarati Hindu", event_type: str = "Grand Wedding (Multi-Day)", religion: str = "Hinduism") -> Dict[str, Any]:
        """Consolidates all statutory, vendor SLA, ceremony essentials kit, and contingency modules."""
        rel_lower = (religion or "Hinduism").lower()

        # Faith-specific ceremony kit
        if "christian" in rel_lower:
            kit_title = "Sacred Church Liturgy & Ceremony Preparation Kit"
            kit_items = [
                {"item": "Order of Service booklets printed & placed in church pews", "category": "Liturgy", "status": False},
                {"item": "Marriage License & Certificate paperwork from civil registrar", "category": "Legal", "status": False},
                {"item": "Polished wedding rings in ceremonial cushion / ring box", "category": "Rings", "status": False},
                {"item": "Unity Candle and taper lighters for church altar", "category": "Altar", "status": False},
                {"item": "Fresh rose petal cones / confetti for church exit walk", "category": "Send-off", "status": False},
                {"item": "Clergy honorarium and organist gratuity envelopes", "category": "Honorarium", "status": False}
            ]
        elif "islam" in rel_lower:
            kit_title = "Sacred Nikah & Walima Preparation Kit"
            kit_items = [
                {"item": "Official Nikah-Nama contract folders & calligraphy signing pens", "category": "Nikah Legal", "status": False},
                {"item": "Mahr marital gift documentation & designated presentation box", "category": "Mahr", "status": False},
                {"item": "Premium Ajwa dates and celebratory mithai for post-Nikah distribution", "category": "Sunnah", "status": False},
                {"item": "Fragrant rosewater brass sprinklers and fresh jasmine garlands", "category": "Swagat", "status": False},
                {"item": "100% Halal catering verification certificate signed by head chef", "category": "Catering", "status": False},
                {"item": "Qazi / Imam honorarium and Dua token envelopes", "category": "Clergy", "status": False}
            ]
        elif "juda" in rel_lower:
            kit_title = "Sacred Chuppah & Ketubah Kit"
            kit_items = [
                {"item": "Illustrated Ketubah contract and archival ink quill pen", "category": "Legal", "status": False},
                {"item": "Two silver Kosher wine cups and certified kosher wine", "category": "Kiddushin", "status": False},
                {"item": "Plain, unadorned gold wedding band", "category": "Rings", "status": False},
                {"item": "Linen napkin-wrapped glass for groom stomping", "category": "Chuppah", "status": False},
                {"item": "Kippot / Yarmulkes basket for guests at Chuppah entrance", "category": "Sanctum", "status": False},
                {"item": "Rabbi and Cantor honorarium envelopes", "category": "Clergy", "status": False}
            ]
        elif "sikh" in rel_lower:
            kit_title = "Sacred Anand Karaj & Gurdwara Kit"
            kit_items = [
                {"item": "Embroidered Rumalla Sahib offering for Sri Guru Granth Sahib Ji", "category": "Darbar", "status": False},
                {"item": "Fresh floral Jaimala garlands for Gurdwara Milni greeting", "category": "Milni", "status": False},
                {"item": "Sacred Palla cloth for groom and bride knot ceremony", "category": "Laavan", "status": False},
                {"item": "Karah Parshad ingredients verified with Gurdwara kitchen team", "category": "Parshad", "status": False},
                {"item": "Head coverings (Rumals/Dupattas) for all attending guests", "category": "Sanctum", "status": False},
                {"item": "Granthi Sahib and Ragi Jatha seva honorarium envelopes", "category": "Seva", "status": False}
            ]
        elif "buddh" in rel_lower or "east asian" in rel_lower:
            kit_title = "Sacred Tea Ceremony & Ancestral Homage Kit"
            kit_items = [
                {"item": "Traditional porcelain tea set with Double Happiness motif", "category": "Tea Ceremony", "status": False},
                {"item": "Sweet tea brewed with longan, red dates, and lotus seeds", "category": "Tea Brew", "status": False},
                {"item": "Comfortable kneeling cushions for bride and groom", "category": "Homage", "status": False},
                {"item": "Red envelopes (Hongbao) with crisp new currency notes", "category": "Tradition", "status": False},
                {"item": "Fresh lotus blooms and monastic alms offerings", "category": "Blessing", "status": False},
                {"item": "Door games props and challenge envelopes for bridal party", "category": "Celebration", "status": False}
            ]
        elif "fusion" in rel_lower or "contemporary" in rel_lower:
            kit_title = "Modern Ceremony & Celebration Essentials Kit"
            kit_items = [
                {"item": "Printed personalized vow booklets in keepsake leather covers", "category": "Vows", "status": False},
                {"item": "Wedding rings in velvet display box", "category": "Rings", "status": False},
                {"item": "Marriage certificate registry and sign-off pens", "category": "Legal", "status": False},
                {"item": "Wireless lapel microphones for celebrant and couple", "category": "Audio", "status": False},
                {"item": "Biodegradable petal confetti / sparklers for grand exit", "category": "Send-off", "status": False},
                {"item": "Celebrant honorarium and vendor coordinator envelopes", "category": "Gratuity", "status": False}
            ]
        else:
            kit_title = "Auspicious Pooja & Sacred Samagri Kit"
            kit_items = [
                {"item": "Ganesh Murti / Supari & Kalash with Mango Leaves", "category": "Sanctum", "status": False},
                {"item": "Pure Gangajal, Rose Water & Panchamrut (Milk, Curd, Ghee, Honey, Sugar)", "category": "Purification", "status": False},
                {"item": "Dry Havan Samagri, Camphor (Kapur), Sandalwood Sticks & Cow Dung Cakes", "category": "Havan", "status": False},
                {"item": "Sacred Thread (Moli/Nadachhadi), Red Cloth (Kanku Pagla), Haldi Powder & Akshat Rice", "category": "Offerings", "status": False},
                {"item": "Fresh Garlands (Jaimala) kept in cool temperature with moisture wrap", "category": "Jaimala", "status": False},
                {"item": "Dakshina Envelopes (Shagun Lifafas) with pristine currency notes", "category": "Tradition", "status": False}
            ]

        return {
            "Time-Phased Task Matrix": cls.get_time_phased_task_matrix(tradition, event_type),
            "Crisis & Risk Mitigation Protocols": cls.get_crisis_protocols(),
            "Vendor Critical Questionnaires & SLAs": [
                {
                    "vendor_type": "Caterer & Beverage Partner",
                    "questions": [
                        "Can you guarantee dietary compliance (e.g., Satvik, Halal, Kosher, or Gluten-Free counters)?",
                        "What is your food wastage protocol, and can surplus be channeled to local verified food banks?",
                        "What is the staff-to-guest ratio for live table service (recommended 1 server per 15 guests)?",
                        "Are backup cooking gas cylinders and mobile kitchen induction units available on-site?"
                    ],
                    "sla_tip": "Include penalty clause of 5% deduction for food delays exceeding 30 minutes beyond scheduled ceremony."
                },
                {
                    "vendor_type": "Decor & Floral Architect",
                    "questions": [
                        "What is the strike-time and setup handover window before the first ritual begins?",
                        "In case of unseasonal rain/wind, what is the storm backup plan for open-air installations?",
                        "Are real fresh blooms guaranteed instead of artificial plastic sprays?",
                        "Is generator power backup (silent DG set) included in your quote?"
                    ],
                    "sla_tip": "Mandate photo sign-off of the sample floral centerpiece 48 hours prior to delivery."
                },
                {
                    "vendor_type": "Photography & Cinematography Crew",
                    "questions": [
                        "How many candid shooters vs traditional videographers will be deployed per ceremony?",
                        "What is the turnaround time for the same-day teaser reel (ideal: 24 hours)?",
                        "Will you bring backup dual-slot camera bodies and external audio recorders for ceremony vows?",
                        "Do you hold all raw footage backup on cloud storage for minimum 90 days?"
                    ],
                    "sla_tip": "Tie final 20% payment to delivery of the master album and high-res raw drive."
                }
            ],
            kit_title: kit_items
        }
