"""Cultural traditions, ceremonies, and sub-traditions metadata for UtsavAI."""

CULTURAL_TRADITIONS = {
    "Gujarati Hindu": {
        "description": "Rich in vibrant garba rhythms, sacred homas, and warm hospitality.",
        "rituals": [
            {"day": 1, "time": "09:30 AM - 11:30 AM", "ritual": "Mandap Mahurat & Ganesh Sthapana", "significance": "Invoking Lord Ganesha to bless the wedding festivities and purify the premises.", "dress_code": "Traditional Bandhani / Kurta Pajama (Yellow/Orange)", "notes": "Priest requires coconut, gangajal, supari, and sacred havan kund."},
            {"day": 1, "time": "03:00 PM - 05:30 PM", "ritual": "Pithi (Haldi Ceremony)", "significance": "Turmeric paste application for radiant glow and warding off negativity.", "dress_code": "Bright Yellow / Mustard Floral Outfits", "notes": "Prepare extra bowls, towels, and skin-friendly natural paste."},
            {"day": 1, "time": "07:30 PM - 12:00 AM", "ritual": "Sangeet & Raas Garba Night", "significance": "Folk dance celebrations uniting both families in celebratory rhythm.", "dress_code": "Chaniya Choli & Kediyu with mirror work", "notes": "Arrange wooden dandiya sticks, DJ with dhol artists, and late-night snacks."},
            {"day": 2, "time": "09:00 AM - 10:30 AM", "ritual": "Jaan Aagman & Ponkhana", "significance": "Grand groom arrival welcomed affectionately by the mother-in-law.", "dress_code": "Regal Sherwani & Pastel Lehengas", "notes": "Keep brass pestle, rolling pin, and sweet curd ready for welcome."},
            {"day": 2, "time": "11:15 AM - 01:30 PM", "ritual": "Lagna Mandap (Jaimala, Hastamelap, Mangal Pheras)", "significance": "The sacred vows around the holy fire and solemnizing the union.", "dress_code": "Panetar / Gharchola & Embroidered Royal Sherwani", "notes": "Sacred fire ventilation required; live shehnai background."},
            {"day": 2, "time": "02:00 PM - 03:30 PM", "ritual": "Kanya Daan & Vidaai", "significance": "Emotional send-off and blessing of the newly wedded couple.", "dress_code": "Elegant Pastels", "notes": "Keep decorative car ready; tissues and quiet farewell space."},
        ],
        "default_budget_split": {
            "Venue & Stays": 32,
            "Catering & Delicacies": 30,
            "Decor & Mandap Art": 16,
            "Photography & Film": 10,
            "Attire & Trousseau": 6,
            "Entertainment & Logistics": 4,
            "Buffer Reserve": 2
        }
    },
    "Punjabi Sikh/Hindu": {
        "description": "High-energy, joyous, hearty hospitality with grand musical traditions.",
        "rituals": [
            {"day": 1, "time": "10:00 AM - 12:30 PM", "ritual": "Chooda & Kalire Ceremony", "significance": "Maternal uncles gift red/white bangles and umbrella charms symbolizing blessings.", "dress_code": "Vibrant Phulkari Salwar Kameez", "notes": "Ensure silken threads and sweet prasad are ready."},
            {"day": 1, "time": "02:00 PM - 04:30 PM", "ritual": "Haldi & Vatna", "significance": "Herbal cleansing paste session with folk songs and teasing.", "dress_code": "Yellow / Sunshine Orange", "notes": "Waterproof decor and dhol percussionists."},
            {"day": 1, "time": "07:30 PM - 01:00 AM", "ritual": "Jaggo & High-Energy Sangeet", "significance": "Nocturnal village procession with decorated earthen pots and bhangra.", "dress_code": "Glamorous Sequined Lehengas & Tuxedos/Kurta Jackets", "notes": "Lighted brass pots, dhol players, and high-wattage sound setup."},
            {"day": 2, "time": "09:30 AM - 10:30 AM", "ritual": "Sehrabandi & Ghodi Chadhna", "significance": "Tying the golden headdress and groom procession on ceremonial mare.", "dress_code": "Regal Sherwani with Safa/Turban", "notes": "Coordinate horse handler and brass band procession."},
            {"day": 2, "time": "11:00 AM - 01:30 PM", "ritual": "Anand Karaj (or Varmala & Pheras)", "significance": "Four sacred Lavan hymns in Gurdwara or floral mandap pheras.", "dress_code": "Pastel Pink / Crimson Royalty", "notes": "Head coverings mandatory for all guests if Gurdwara ceremony."},
            {"day": 2, "time": "08:00 PM - 12:30 AM", "ritual": "Grand Reception & Toasting", "significance": "Celebratory feast, live band, and formal introductions.", "dress_code": "Black Tie / Indo-Western Haute Couture", "notes": "Multi-tier stage, bar logistics, and cinematic couple shoot."},
        ],
        "default_budget_split": {
            "Venue & Stays": 30,
            "Catering & Delicacies": 32,
            "Decor & Mandap Art": 15,
            "Photography & Film": 11,
            "Attire & Trousseau": 6,
            "Entertainment & Logistics": 4,
            "Buffer Reserve": 2
        }
    },
    "South Indian (Tamil / Telugu / Kannada)": {
        "description": "Serene Vedic chants, auspicious Nadaswaram, aromatic filter coffee, and golden silk.",
        "rituals": [
            {"day": 1, "time": "07:30 AM - 09:30 AM", "ritual": "Vratham & Mangala Snanam", "significance": "Sacred purification fast and dawn holy bath for both bride and groom.", "dress_code": "Traditional Madisar / Veshti with Angavastram", "notes": "Sacred river waters, clay pots, and priest arrangements."},
            {"day": 1, "time": "04:30 PM - 06:30 PM", "ritual": "Nichayathartham (Formal Engagement)", "significance": "Recitation of legal lagna patrika by priests in presence of elders.", "dress_code": "Kanjeevaram Silk Sarees & Silk Shirts", "notes": "Plates with dry fruits, gold coins, and traditional tamboolam."},
            {"day": 1, "time": "07:00 PM - 10:00 PM", "ritual": "Carnatic Musical Evening & Reception", "significance": "Classical or fusion musical recital honoring guests.", "dress_code": "Temple Silk / Traditional Finery", "notes": "Traditional seating, violin/mridangam acoustics."},
            {"day": 2, "time": "06:00 AM - 07:30 AM", "ritual": "Kashi Yatra & Oonjal (Swing Ritual)", "significance": "Playful procession followed by couple seated on decorated swing fed milk & bananas.", "dress_code": "Kanjeevaram with temple jewelry / Pattu Veshti", "notes": "Floral wooden swing, colored rice balls for warding evil eye."},
            {"day": 2, "time": "08:15 AM - 10:00 AM", "ritual": "Kanyadaanam & Mangalya Dharanam (Muhurtham)", "significance": "Auspicious tying of the sacred Thali / Mangalsutra accompanied by 'Ketti Melam'.", "dress_code": "Sacred Koora Pattu (Red/Mustard)", "notes": "Auspicious muhurtham window strict adherence."},
            {"day": 2, "time": "11:30 AM - 02:00 PM", "ritual": "Traditional Banana Leaf Feast (Elai Saapadu)", "significance": "Authentic multi-course satvik culinary feast served on fresh banana leaves.", "dress_code": "Traditional comfortable silks", "notes": "Continuous floor/table service with payasam varieties."},
        ],
        "default_budget_split": {
            "Venue & Stays": 28,
            "Catering & Delicacies": 34,
            "Decor & Mandap Art": 16,
            "Photography & Film": 10,
            "Attire & Trousseau": 7,
            "Entertainment & Logistics": 3,
            "Buffer Reserve": 2
        }
    },
    "Bengali Hindu": {
        "description": "Lyrical conch blowing, sacred betel leaf rituals, and rich heritage feasts.",
        "rituals": [
            {"day": 1, "time": "09:00 AM - 11:30 AM", "ritual": "Dodhi Mangal & Gaye Holud", "significance": "Early morning yogurt meal followed by fragrant turmeric ceremony.", "dress_code": "Lal-Paar White Silk / Dhoti Kurta", "notes": "Mustard oil, whole fish gifting tray, conch shells."},
            {"day": 1, "time": "06:30 PM - 08:30 PM", "ritual": "Bor Jatri & Bor Boron", "significance": "Ceremonial arrival of groom's entourage and mother-in-law's blessing.", "dress_code": "Topor headdress & embroidered Kurta", "notes": "Boron plate with earthen lamp, betel leaves, sweets."},
            {"day": 1, "time": "09:00 PM - 11:30 PM", "ritual": "Saat Paak & Subho Drishti", "significance": "Bride carried on wooden stool (Piri) seven times around groom; first sacred eye-contact.", "dress_code": "Benarasi Silk in Crimson / Scarlet", "notes": "Seven brothers/friends to lift the Piri steadily."},
            {"day": 2, "time": "12:00 PM - 03:00 PM", "ritual": "Bou Bhaat (Bride's Welcome Feast)", "significance": "Groom formally vows to provide rice & apparel; bride serves ghee-rice to family.", "dress_code": "Traditional Gorod / Tussar Silk", "notes": "Grand royal Bengali lunch with authentic roshogollas."},
        ],
        "default_budget_split": {
            "Venue & Stays": 30,
            "Catering & Delicacies": 33,
            "Decor & Mandap Art": 15,
            "Photography & Film": 10,
            "Attire & Trousseau": 7,
            "Entertainment & Logistics": 3,
            "Buffer Reserve": 2
        }
    },
    "Contemporary & Multi-Cultural Fusion": {
        "description": "Elegant blend of timeless rituals with modern experiential hospitality.",
        "rituals": [
            {"day": 1, "time": "04:00 PM - 07:00 PM", "ritual": "Sunset Welcome Cocktails & Sundowner", "significance": "Warm ice-breaker gathering for out-of-town guests with acoustic melodies.", "dress_code": "Resort Chic / Pastel Linen", "notes": "Signature mocktails/cocktails and live saxophone/acoustic artist."},
            {"day": 1, "time": "08:00 PM - 01:00 AM", "ritual": "The Sangeet & Musical Showcase", "significance": "Choreographed family performances, dance battle, and DJ set.", "dress_code": "Contemporary Fusion / Metallic Glamour", "notes": "LED backdrop wall, professional choreography sync."},
            {"day": 2, "time": "10:00 AM - 01:00 PM", "ritual": "Celebratory Poolside Haldi & Mela", "significance": "Organic floral holi, games, live street food carts, and photobooths.", "dress_code": "Vibrant Yellow & Bohemian Prints", "notes": "Marigold petals, water guns, and stain-resistant fabric."},
            {"day": 2, "time": "05:30 PM - 07:30 PM", "ritual": "Sunset Vows & Floral Mandap Ceremony", "significance": "Harmonious exchange of rings, personalized vows, and sacred rituals.", "dress_code": "Ivory / Rose Gold Couture", "notes": "Golden hour lighting coordinates with photographer."},
            {"day": 2, "time": "08:30 PM - 01:30 AM", "ritual": "Gala Dinner & After-Party", "significance": "Formal speeches, cake cutting, decadent multi-cuisine banquet, and dancing.", "dress_code": "Black-Tie / Tuxedo / Ballgown", "notes": "Special dessert bar, midnight coffee station."},
        ],
        "default_budget_split": {
            "Venue & Stays": 35,
            "Catering & Delicacies": 28,
            "Decor & Mandap Art": 15,
            "Photography & Film": 12,
            "Attire & Trousseau": 5,
            "Entertainment & Logistics": 3,
            "Buffer Reserve": 2
        }
    },
    "Community Utsav (Festival / Gala / Milap)": {
        "description": "Large-scale community festival or anniversary gala with structured volunteer & public flow.",
        "rituals": [
            {"day": 1, "time": "08:30 AM - 10:30 AM", "ritual": "Deepotsav & Inaugural Vandana", "significance": "Lighting of the mega ceremonial lamp and prayer invocation by elders.", "dress_code": "Traditional Festal Attire", "notes": "Audio system with high vocal clarity, floral garlands."},
            {"day": 1, "time": "11:00 AM - 02:00 PM", "ritual": "Community Langar / Maha Prasad", "significance": "Egalitarian community feast served with reverence.", "dress_code": "Modest Comfortable Wear", "notes": "Eco-friendly leaf tableware, volunteer brigade rosters."},
            {"day": 1, "time": "06:00 PM - 10:30 PM", "ritual": "Grand Cultural Pageant & Folk Orchestra", "significance": "Youth drama, folk music recitals, community felicitation honors.", "dress_code": "Ethnic Formal", "notes": "Green room coordinator, crowd safety barricades."},
        ],
        "default_budget_split": {
            "Venue & Stays": 25,
            "Catering & Delicacies": 35,
            "Decor & Mandap Art": 15,
            "Photography & Film": 8,
            "Attire & Trousseau": 2,
            "Entertainment & Logistics": 12,
            "Buffer Reserve": 3
        }
    }
}

EVENT_TYPES = [
    "Grand Wedding (Multi-Day)",
    "Milestone Anniversary (25th / 50th)",
    "Community Festival (Navratri / Diwali Gala)",
    "Sacred Thread / Upanayana / Yagnopavit",
    "Engagement & Ring Ceremony",
    "Grand Baby Shower / Seemantam / Godh Bharai",
]

DIETARY_PREFERENCES = [
    "Pure Vegetarian (Satvik / Jain Options)",
    "Strict Vegetarian (No Onion/Garlic on Request)",
    "Multi-Cuisine (Vegetarian & Non-Vegetarian Sections)",
    "Regional Specialty Authentic Traditional Feast"
]

VENUE_TYPES = [
    "Heritage Palace / Haveli",
    "Luxury Beachfront / Lakeview Resort",
    "Five-Star City Hotel & Ballroom",
    "Open Royal Lawn & Farmhouse",
    "Community Temple / Mandap Hall"
]

