"""
Global Religious, Cultural Traditions & Sub-traditions Database for UtsavAI.
Designed for zero-token retrieval architecture across all major world religions.
"""

GLOBAL_RELIGIONS = {
    "Hinduism": {
        "icon": "🕉️",
        "calendar_system": "Vedic Panchang & Lunar Tithis",
        "auspicious_logic": "Vedic Muhurat, Abhijit Muhurat, Godhuli & Planetary Nakshatras",
        "dietary_standard": "Pure Vegetarian (Satvik / Jain Options, No Onion/Garlic on request)",
        "sub_traditions": {
            "Gujarati Hindu": {
                "rituals": [
                    {"day": 1, "time": "09:30 AM - 11:30 AM", "ritual": "Mandap Mahurat & Ganesh Sthapana", "significance": "Invoking Lord Ganesha to bless the wedding festivities and sanctify the venue.", "dress_code": "Traditional Bandhani / Kurta Pajama (Yellow/Orange)", "notes": "Priest requires coconut, gangajal, supari, and sacred havan kund."},
                    {"day": 1, "time": "03:00 PM - 05:30 PM", "ritual": "Pithi (Haldi Ceremony)", "significance": "Turmeric paste application for radiant skin and spiritual protection.", "dress_code": "Bright Yellow / Mustard Floral Outfits", "notes": "Prepare natural turmeric paste bowls and warm towels."},
                    {"day": 1, "time": "07:30 PM - 12:00 AM", "ritual": "Sangeet & Raas Garba Night", "significance": "Traditional folk dance uniting both families in celebration.", "dress_code": "Chaniya Choli & Kediyu with mirror work", "notes": "Arrange wooden dandiya sticks and live dhol percussionists."},
                    {"day": 2, "time": "09:00 AM - 10:30 AM", "ritual": "Jaan Aagman & Ponkhana", "significance": "Welcoming groom entourage by mother-in-law with playful blessings.", "dress_code": "Regal Sherwani & Pastel Lehengas", "notes": "Brass pestle, rolling pin, and sweet curd ready at entrance."},
                    {"day": 2, "time": "11:15 AM - 01:30 PM", "ritual": "Lagna Mandap (Mangal Pheras & Saptapadi)", "significance": "Seven sacred steps and vows around the holy havan fire.", "dress_code": "Panetar / Gharchola & Royal Embroidered Sherwani", "notes": "Mandap smoke ventilation verified; shehnai background."},
                    {"day": 2, "time": "02:00 PM - 03:30 PM", "ritual": "Kanya Daan & Vidaai", "significance": "Heartfelt parental blessing and bride send-off.", "dress_code": "Elegant Pastels", "notes": "Decorated farewell car ready with family escort."}
                ],
                "default_budget_split": {"Venue & Stays": 32, "Catering & Delicacies": 30, "Decor & Mandap Art": 16, "Photography & Film": 10, "Attire & Trousseau": 6, "Entertainment & Logistics": 4, "Buffer Reserve": 2}
            },
            "Punjabi Hindu / Sikh": {
                "rituals": [
                    {"day": 1, "time": "10:00 AM - 12:30 PM", "ritual": "Chooda & Kalire Ceremony", "significance": "Maternal uncle gifts red/white ivory bangles and umbrella charms.", "dress_code": "Phulkari Salwar Suit / Embroidered Kurta", "notes": "Kalire tying thread and sweet prasad."},
                    {"day": 1, "time": "02:00 PM - 04:30 PM", "ritual": "Vatna & Haldi Scrub", "significance": "Herbal cleansing paste session with lively folk teasing.", "dress_code": "Sunshine Yellow & Orange", "notes": "Waterproof decor and dhol drummers."},
                    {"day": 1, "time": "07:30 PM - 01:00 AM", "ritual": "Jaggo & High-Wattage Sangeet", "significance": "Nocturnal village lantern procession with bhangra routines.", "dress_code": "Sequined Lehengas & Indo-Western Tuxedos", "notes": "Lighted brass pots and DJ sound console."},
                    {"day": 2, "time": "09:30 AM - 10:30 AM", "ritual": "Sehrabandi & Ghodi Chadhna", "significance": "Headdress tying by sisters and groom ceremonial procession.", "dress_code": "Regal Sherwani with Safa/Turban", "notes": "Horse handler and brass band route."},
                    {"day": 2, "time": "11:00 AM - 01:30 PM", "ritual": "Varmala & Sacred Pheras", "significance": "Garland exchange and sacred fire vows.", "dress_code": "Crimson Velvet & Ivory Gold", "notes": "Floral shower petals and havan firewood."},
                    {"day": 2, "time": "08:00 PM - 12:30 AM", "ritual": "Grand Reception & Toasting", "significance": "Celebratory banquet and family speeches.", "dress_code": "Black-Tie / Haute Couture", "notes": "Cinematic couple shoot and live acoustic band."}
                ],
                "default_budget_split": {"Venue & Stays": 30, "Catering & Delicacies": 32, "Decor & Mandap Art": 15, "Photography & Film": 11, "Attire & Trousseau": 6, "Entertainment & Logistics": 4, "Buffer Reserve": 2}
            },
            "South Indian (Tamil / Telugu / Kannada)": {
                "rituals": [
                    {"day": 1, "time": "07:30 AM - 09:30 AM", "ritual": "Vratham & Mangala Snanam", "significance": "Dawn holy bath and purification prayers for spiritual alignment.", "dress_code": "Traditional Madisar / Pattu Veshti", "notes": "Sacred pots, sesame oil, and priest arrangements."},
                    {"day": 1, "time": "04:30 PM - 06:30 PM", "ritual": "Nichayathartham (Engagement)", "significance": "Formal reading of wedding lagna patrika in front of elders.", "dress_code": "Kanjeevaram Silk & Silk Kurta", "notes": "Plates with dry fruits, gold coins, and tamboolam."},
                    {"day": 1, "time": "07:00 PM - 10:00 PM", "ritual": "Carnatic Recital & Welcome Dinner", "significance": "Classical musical celebration honoring arriving guests.", "dress_code": "Temple Silks", "notes": "Nadaswaram and Mridangam acoustic setups."},
                    {"day": 2, "time": "06:00 AM - 07:30 AM", "ritual": "Kashi Yatra & Oonjal (Swing)", "significance": "Playful procession followed by couple on decorated swing.", "dress_code": "Pattu Veshti & Temple Jewelry", "notes": "Floral swing and colored rice balls."},
                    {"day": 2, "time": "08:15 AM - 10:00 AM", "ritual": "Mangalya Dharanam (Muhurtham)", "significance": "Tying the sacred Thali accompanied by loud Ketti Melam drums.", "dress_code": "Koora Pattu in Mustard/Red", "notes": "Strict adherence to muhurtham window."},
                    {"day": 2, "time": "11:30 AM - 02:00 PM", "ritual": "Traditional Banana Leaf Feast (Elai Saapadu)", "significance": "Multi-course satvik culinary feast served on fresh banana leaves.", "dress_code": "Traditional Silks", "notes": "Floor/table continuous traditional service."}
                ],
                "default_budget_split": {"Venue & Stays": 28, "Catering & Delicacies": 34, "Decor & Mandap Art": 16, "Photography & Film": 10, "Attire & Trousseau": 7, "Entertainment & Logistics": 3, "Buffer Reserve": 2}
            },
            "Bengali Hindu": {
                "rituals": [
                    {"day": 1, "time": "09:00 AM - 11:30 AM", "ritual": "Dodhi Mangal & Gaye Holud", "significance": "Dawn yogurt meal followed by fragrant mustard turmeric blessings.", "dress_code": "Lal-Paar White Silk / Dhoti", "notes": "Mustard oil, whole rohu fish gifting tray, conch shells."},
                    {"day": 1, "time": "06:30 PM - 08:30 PM", "ritual": "Bor Jatri & Bor Boron", "significance": "Ceremonial welcome of the groom's entourage with earthen lamps.", "dress_code": "Topor headdress & embroidered Kurta", "notes": "Boron plate, betel leaves, sweets."},
                    {"day": 1, "time": "09:00 PM - 11:30 PM", "ritual": "Saat Paak & Subho Drishti", "significance": "Bride lifted on wooden Piri seven times around groom; first sacred eye-contact.", "dress_code": "Benarasi Silk in Crimson / Scarlet", "notes": "7 brothers/friends to carry the wooden Piri."},
                    {"day": 2, "time": "12:00 PM - 03:30 PM", "ritual": "Bou Bhaat & Reception", "significance": "Formal welcome feast where bride serves ghee-rice to family.", "dress_code": "Traditional Gorod Silk", "notes": "Royal Bengali cuisine with authentic mishti roshogollas."}
                ],
                "default_budget_split": {"Venue & Stays": 30, "Catering & Delicacies": 33, "Decor & Mandap Art": 15, "Photography & Film": 10, "Attire & Trousseau": 7, "Entertainment & Logistics": 3, "Buffer Reserve": 2}
            }
        }
    },
    "Islam": {
        "icon": "☪️",
        "calendar_system": "Hijri Lunar Calendar",
        "auspicious_logic": "Post-Friday Prayers (Jummah), Shawwal & Non-Fasting Months",
        "dietary_standard": "100% Halal Certified Catering, Strict Alcohol-Free Banquet",
        "sub_traditions": {
            "Traditional Nikah & Walima": {
                "rituals": [
                    {"day": 1, "time": "04:00 PM - 07:00 PM", "ritual": "Manjha & Mayun (Turmeric Ceremony)", "significance": "Beautification and cleansing ceremony with sisters and aunts.", "dress_code": "Mustard Yellow Shararas & Kurtas", "notes": "Floral jewelry, marigold canopies, and traditional dholak."},
                    {"day": 1, "time": "07:30 PM - 11:30 PM", "ritual": "Mehendi & Sangeet Gathering", "significance": "Intricate henna application with family musical performances.", "dress_code": "Emerald Green & Teal Anarkalis", "notes": "Multiple henna artists and live acoustic singers."},
                    {"day": 2, "time": "11:00 AM - 01:30 PM", "ritual": "Nikah Ceremony & Ijab-e-Qubool", "significance": "Solemn marriage contract signing witnessed by Qazi and guardians.", "dress_code": "Regal Ivory Sherwani & Embroidered Pastel Gharara", "notes": "Segregated or unified seating per family customs, Mahr contract ready."},
                    {"day": 2, "time": "08:00 PM - 12:30 AM", "ritual": "Grand Walima Reception", "significance": "Sunnah banquet hosted by groom's family to celebrate the union.", "dress_code": "Formal Black-Tie / Embroidered Royal Tuxedo & Lehenga", "notes": "Royal dum biryani, kebabs, sheer khurma, and stage photography."}
                ],
                "default_budget_split": {"Venue & Stays": 32, "Catering & Delicacies": 34, "Decor & Mandap Art": 14, "Photography & Film": 10, "Attire & Trousseau": 6, "Entertainment & Logistics": 2, "Buffer Reserve": 2}
            }
        }
    },
    "Christianity": {
        "icon": "✝️",
        "calendar_system": "Gregorian Calendar",
        "auspicious_logic": "Weekend Church Liturgy, Outside of Lent / Holy Week",
        "dietary_standard": "Multi-Cuisine Continental, Canape Cocktails & Formal Banquet",
        "sub_traditions": {
            "Traditional Church & Gala Reception": {
                "rituals": [
                    {"day": 1, "time": "05:00 PM - 07:00 PM", "ritual": "Rehearsal Walkthrough & Bridal Shower", "significance": "Bridal party rehearses processional order and altar placement.", "dress_code": "Cocktail Casual / Pastel Silks", "notes": "Coordinate sound system with church music director."},
                    {"day": 1, "time": "07:30 PM - 10:30 PM", "ritual": "Welcome Rehearsal Dinner", "significance": "Intimate gathering thanking parents and wedding party entourage.", "dress_code": "Smart Casual Chic", "notes": "Microphone for heartfelt toasts and speeches."},
                    {"day": 2, "time": "02:00 PM - 03:30 PM", "ritual": "Holy Matrimony (Vows & Rings)", "significance": "Exchange of vows and rings before God, accompanied by pipe organ hymns.", "dress_code": "White Lace Bridal Gown & Tuxedo / Morning Suit", "notes": "Order of service booklets and flower petals for church exit."},
                    {"day": 2, "time": "06:30 PM - 01:00 AM", "ritual": "Grand Reception, First Dance & Banquet", "significance": "Formal grand entrance, first couple dance, wedding cake cutting, and feast.", "dress_code": "Black-Tie / Evening Gowns", "notes": "Live brass band or DJ, champagne toast towers, and photo booth."}
                ],
                "default_budget_split": {"Venue & Stays": 35, "Catering & Delicacies": 30, "Decor & Mandap Art": 12, "Photography & Film": 12, "Attire & Trousseau": 6, "Entertainment & Logistics": 3, "Buffer Reserve": 2}
            }
        }
    },
    "Sikhism": {
        "icon": "ੴ",
        "calendar_system": "Nanakshahi Calendar",
        "auspicious_logic": "Morning Amrit Vela / Daylight Anand Karaj Windows",
        "dietary_standard": "Pure Vegetarian Satvik Langar & Lavish Reception Banquet",
        "sub_traditions": {
            "Anand Karaj & Grand Reception": {
                "rituals": [
                    {"day": 1, "time": "11:00 AM - 02:00 PM", "ritual": "Maiyan & Haldi Ceremony", "significance": "Rangoli floral patterns, oil, and cleansing paste rituals with cousins.", "dress_code": "Bright Yellow Phulkari", "notes": "Peera wooden seat, red dupatta, and traditional vatna."},
                    {"day": 1, "time": "07:30 PM - 12:30 AM", "ritual": "Sangeet & Dhol Night", "significance": "Celebratory bhangra routines and family musical face-offs.", "dress_code": "Glamorous Punjabi Silk Suits & Kurta Jackets", "notes": "Professional dholis, dance floor stage, and cocktail buffet."},
                    {"day": 2, "time": "09:00 AM - 10:00 AM", "ritual": "Milni Ceremony at Gurdwara", "significance": "Formal meeting and garland exchange between corresponding family elders.", "dress_code": "Formal Sherwani & Head Scarves", "notes": "Head coverings mandatory; socks required inside Gurdwara."},
                    {"day": 2, "time": "10:15 AM - 12:00 PM", "ritual": "Anand Karaj (Four Sacred Lavaan)", "significance": "Circumambulating Sri Guru Granth Sahib Ji four times in spiritual union.", "dress_code": "Pastel Pink / Crimson Royalty", "notes": "Ragi jatha hymn singers and Karah Prasad distribution."},
                    {"day": 2, "time": "12:30 PM - 02:30 PM", "ritual": "Guru Ka Langar", "significance": "Egalitarian community feast served on floor mats with divine reverence.", "dress_code": "Modest traditional attire", "notes": "Volunteer seva brigade for serving hot roti and daal."}
                ],
                "default_budget_split": {"Venue & Stays": 30, "Catering & Delicacies": 34, "Decor & Mandap Art": 14, "Photography & Film": 10, "Attire & Trousseau": 6, "Entertainment & Logistics": 4, "Buffer Reserve": 2}
            }
        }
    },
    "Judaism": {
        "icon": "✡️",
        "calendar_system": "Hebrew Lunar Calendar",
        "auspicious_logic": "Non-Sabbath Windows (Sunday Weddings Preferred, Sunset Havdalah)",
        "dietary_standard": "Strict Glatt Kosher Certified Kitchen & Wine",
        "sub_traditions": {
            "Traditional Chuppah & Horah": {
                "rituals": [
                    {"day": 1, "time": "04:30 PM - 05:30 PM", "ritual": "Ketubah Signing & Badeken", "significance": "Signing the marriage contract witnessed by two rabbis and bride veiling.", "dress_code": "Formal Attire / Yarmulke / Kippah", "notes": "Ketubah quill pen and ceremonial display easel."},
                    {"day": 1, "time": "06:00 PM - 07:15 PM", "ritual": "Chuppah & Seven Blessings (Sheva Brachot)", "significance": "Ceremony under 4-pillared open canopy and breaking of the glass.", "dress_code": "Bridal Gown & Formal Suit", "notes": "Glass wrapped in linen napkin for groom step; Mazel Tov cheers."},
                    {"day": 1, "time": "08:00 PM - 01:00 AM", "ritual": "The Horah Dance & Kosher Gala Dinner", "significance": "High-energy circle dancing lifting the bride and groom high on chairs.", "dress_code": "Black-Tie Elegant", "notes": "Sturdy wooden armchairs for chair-lifting, live klezmer band."}
                ],
                "default_budget_split": {"Venue & Stays": 34, "Catering & Delicacies": 32, "Decor & Mandap Art": 14, "Photography & Film": 10, "Attire & Trousseau": 5, "Entertainment & Logistics": 3, "Buffer Reserve": 2}
            }
        }
    },
    "Buddhism & East Asian Traditions": {
        "icon": "☸️",
        "calendar_system": "Lunar Calendar",
        "auspicious_logic": "Auspicious Lunar Days, Monastic Blessing Windows",
        "dietary_standard": "Vegetarian Buddhist Delicacies & Tea Ceremony",
        "sub_traditions": {
            "Monastic Blessing & Tea Ceremony": {
                "rituals": [
                    {"day": 1, "time": "09:00 AM - 10:30 AM", "ritual": "Monk Chanting & Holy Water Blessing", "significance": "Revered Buddhist monks chant parittas and sprinkle sacred water for merit.", "dress_code": "Traditional White / Gold Brocade", "notes": "Monk seating mats, lotus flower offerings, and alms gifts."},
                    {"day": 1, "time": "11:30 AM - 01:30 PM", "ritual": "Respectful Tea Ceremony", "significance": "Serving ceremonial tea to parents and elder ancestors.", "dress_code": "Traditional Silk Cheongsam / Hanbok / Kimono", "notes": "Porcelain tea set with sweet lotus seeds and red dates."},
                    {"day": 1, "time": "07:00 PM - 10:30 PM", "ritual": "Multi-Course Celebration Banquet", "significance": "Festive community banquet celebrating harmony and lineage.", "dress_code": "Formal Festive", "notes": "Round table banquet service and toast speeches."}
                ],
                "default_budget_split": {"Venue & Stays": 32, "Catering & Delicacies": 34, "Decor & Mandap Art": 14, "Photography & Film": 10, "Attire & Trousseau": 5, "Entertainment & Logistics": 3, "Buffer Reserve": 2}
            }
        }
    },
    "Contemporary & Interfaith Fusion": {
        "icon": "✨",
        "calendar_system": "Universal Calendar",
        "auspicious_logic": "Golden Hour Sunset & Holiday Long Weekends",
        "dietary_standard": "Custom Fusion Menu (Vegan/Jain/Halal/Gluten-Free Options)",
        "sub_traditions": {
            "Global Fusion Celebration": {
                "rituals": [
                    {"day": 1, "time": "04:30 PM - 07:00 PM", "ritual": "Sunset Welcome Cocktails & Sundowner", "significance": "Ice-breaker gathering for global travelers with acoustic melodies.", "dress_code": "Resort Chic / Pastel Linen", "notes": "Signature mocktails/cocktails and live saxophone artist."},
                    {"day": 1, "time": "08:00 PM - 01:00 AM", "ritual": "Global Sangeet & Musical Showcase", "significance": "Choreographed cross-cultural performances and dance battles.", "dress_code": "Contemporary Fusion / Metallic Glamour", "notes": "LED backdrop wall and dance-floor lighting."},
                    {"day": 2, "time": "10:30 AM - 01:00 PM", "ritual": "Poolside Floral Fiesta (Haldi / Flower Shower)", "significance": "Organic floral holi, live food carts, and sunshine celebrations.", "dress_code": "Boho Chic / Yellows & Pastels", "notes": "Marigold petals, water spritzers, and photo stations."},
                    {"day": 2, "time": "05:30 PM - 07:30 PM", "ritual": "Sunset Vows & Floral Mandap Exchange", "significance": "Harmonious union blending ancestral traditions with modern personal vows.", "dress_code": "Ivory / Champagne Rose Gold", "notes": "Golden hour lighting coordinates with camera drones."},
                    {"day": 2, "time": "08:30 PM - 01:30 AM", "ritual": "Gala Dinner & International After-Party", "significance": "Formal speeches, cake cutting, multi-cuisine banquet, and dancing.", "dress_code": "Black-Tie / Tuxedo / Ballgown", "notes": "Midnight dessert bar and coffee lounge."}
                ],
                "default_budget_split": {"Venue & Stays": 35, "Catering & Delicacies": 28, "Decor & Mandap Art": 15, "Photography & Film": 12, "Attire & Trousseau": 5, "Entertainment & Logistics": 3, "Buffer Reserve": 2}
            }
        }
    }
}

