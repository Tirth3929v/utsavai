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
            },
            "1-Day Vedic Vivaha & Reception": {
                "rituals": [
                    {"day": 1, "time": "08:30 AM - 10:00 AM", "ritual": "Ganesh Puja & Mandap Sthapana", "significance": "Sanctifying the sacred pavilion and invoking divine obstacles removal.", "dress_code": "Festive Yellow / Traditional Silk Kurta", "notes": "Puja samagri, coconut, gangajal, and havan preparation."},
                    {"day": 1, "time": "10:30 AM - 11:30 AM", "ritual": "Baraat Swagat & Varmala", "significance": "Welcoming groom and mutual exchange of fragrant rose garlands.", "dress_code": "Royal Sherwani & Regal Lehenga", "notes": "Entrance floral shower and brass band."},
                    {"day": 1, "time": "11:45 AM - 01:45 PM", "ritual": "Kanyadaan, Mangal Pheras & Saptapadi", "significance": "Seven sacred vows around the holy havan fire and lifetime bonding.", "dress_code": "Bridal Red/Pink Panetar & Royal Turban", "notes": "Agni havan wood, ghee, puffed rice (laja)."},
                    {"day": 1, "time": "02:00 PM - 03:30 PM", "ritual": "Traditional Wedding Feast (Mahaprasad)", "significance": "Elaborate multi-course pure vegetarian banquet for all guests.", "dress_code": "Festive Traditional", "notes": "Continuous buffet with sweets and live counters."},
                    {"day": 1, "time": "07:30 PM - 11:30 PM", "ritual": "Grand Evening Reception & Musical Gala", "significance": "Formal congratulations, stage photography, live music, and celebrations.", "dress_code": "Indo-Western Tuxedo / Designer Gown", "notes": "Stage lighting, couple entrance song, photo booth."}
                ],
                "default_budget_split": {"Venue & Stays": 32, "Catering & Delicacies": 32, "Decor & Mandap Art": 15, "Photography & Film": 11, "Attire & Trousseau": 5, "Entertainment & Logistics": 3, "Buffer Reserve": 2}
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
                    {"day": 1, "time": "05:00 PM - 07:00 PM", "ritual": "Church Rehearsal Walkthrough", "significance": "Bridal party rehearses processional order, altar placement, and vows with the Pastor.", "dress_code": "Cocktail Casual / Smart Semi-Formal", "notes": "Coordinate sound system with church music director and organist."},
                    {"day": 1, "time": "07:30 PM - 10:30 PM", "ritual": "Welcome Rehearsal Dinner & Toasts", "significance": "Intimate gathering thanking parents, bridal party, and out-of-town guests.", "dress_code": "Smart Casual Chic", "notes": "Wireless microphone for heartfelt family toasts and slide-shows."},
                    {"day": 2, "time": "01:30 PM - 03:00 PM", "ritual": "Sacred Holy Matrimony (Processional, Vows & Rings)", "significance": "Exchange of vows and rings before God, accompanied by choir hymns and pastoral blessing.", "dress_code": "White Lace Bridal Gown & Tuxedo / Morning Suit", "notes": "Order of service booklets, pew bows, flower girl petals for exit."},
                    {"day": 2, "time": "05:00 PM - 06:30 PM", "ritual": "Sunset Cocktail Hour & Hors d'Oeuvres", "significance": "Guests enjoy passed canapés, craft beverages, and lively acoustic melodies while couple takes formal portraits.", "dress_code": "Black-Tie / Formal Evening Wear", "notes": "String quartet or acoustic guitarist, passed champagne flutes."},
                    {"day": 2, "time": "07:00 PM - 12:30 AM", "ritual": "Grand Reception, First Dance & Dinner Banquet", "significance": "Couple grand entrance, ceremonial cake cutting, emotional first dance, dinner banquet, and dancing.", "dress_code": "Black-Tie / Evening Gowns", "notes": "Live brass band or DJ, champagne toast towers, photo booth, and sparkler exit."}
                ],
                "default_budget_split": {"Venue & Stays": 35, "Catering & Delicacies": 30, "Decor & Mandap Art": 12, "Photography & Film": 12, "Attire & Trousseau": 6, "Entertainment & Logistics": 3, "Buffer Reserve": 2}
            },
            "1-Day Holy Matrimony & Gala Reception": {
                "rituals": [
                    {"day": 1, "time": "10:30 AM - 12:30 PM", "ritual": "Bridal & Groom Suite Preparation & Photography", "significance": "Couple prepares with bridal party; first look reveal with parents and emotional portrait session.", "dress_code": "Satin Preparation Robes / Casual Elegance", "notes": "Hair and makeup artists on site, floral deliveries confirmed."},
                    {"day": 1, "time": "01:30 PM - 03:00 PM", "ritual": "Sacred Church Nuptial Service (Vows & Exchange of Rings)", "significance": "Solemn processional, biblical readings, pastoral vows, ring blessing, unity candle, and presentation of newlyweds.", "dress_code": "White Bridal Gown & Classic Dark Tuxedo", "notes": "Organist ready, wireless lapel mic for pastor, marriage certificate signing table."},
                    {"day": 1, "time": "03:30 PM - 05:00 PM", "ritual": "Courtyard Mingle & Family Formal Portraits", "significance": "Post-ceremony congratulations and formal group photography with extended family and church members.", "dress_code": "Formal Church Attire", "notes": "Light refreshments, cold sparkling water, dedicated portrait backdrop."},
                    {"day": 1, "time": "05:30 PM - 07:00 PM", "ritual": "Sunset Cocktail Hour & Passed Canapés", "significance": "Welcoming guests to the reception venue with signature mocktails, cocktails, and acoustic music.", "dress_code": "Black-Tie / Formal Evening Gowns", "notes": "Bar setup, passed canapés, guest book signing table."},
                    {"day": 1, "time": "07:15 PM - 08:30 PM", "ritual": "Grand Entrance, Toasts & Multi-Course Dinner", "significance": "Grand couple entrance followed by heartfelt speeches by Best Man, Maid of Honor, and father of the bride, accompanied by formal dinner.", "dress_code": "Black-Tie / Tuxedo", "notes": "Audio system for speeches, plated or luxury buffet service."},
                    {"day": 1, "time": "08:45 PM - 11:30 PM", "ritual": "Cake Cutting, First Dance & Joyful Dance Floor", "significance": "Ceremonial multi-tiered cake cutting, romantic first dance, father-daughter dance, and open celebration dancing.", "dress_code": "Formal Evening Wear", "notes": "Cake knife and champagne flutes, dynamic dance floor lighting, sparkler exit at 11:30 PM."}
                ],
                "default_budget_split": {"Venue & Stays": 36, "Catering & Delicacies": 30, "Decor & Mandap Art": 12, "Photography & Film": 12, "Attire & Trousseau": 5, "Entertainment & Logistics": 3, "Buffer Reserve": 2}
            },
            "Christian Engagement & Ring Ceremony": {
                "rituals": [
                    {"day": 1, "time": "11:00 AM - 12:30 PM", "ritual": "Pastoral Blessing & Ring Exchange Ceremony", "significance": "Opening prayer, pastoral reflection on commitment, exchange of engagement rings, and formal blessing by the minister.", "dress_code": "Smart Elegant / Pastel Cocktail Dresses & Suits", "notes": "Altar floral centerpiece, ring display cushion, order of service programs."},
                    {"day": 1, "time": "01:00 PM - 03:00 PM", "ritual": "Celebratory Luncheon & Family Felicitations", "significance": "Intimate luncheon uniting both families with heartfelt blessings and welcome speeches.", "dress_code": "Smart Chic", "notes": "Three-course plated lunch or gourmet buffet with wine/mocktail pairing."},
                    {"day": 1, "time": "06:30 PM - 08:00 PM", "ritual": "Sunset Welcome Cocktails & Mingling", "significance": "Evening cocktail reception welcoming extended friends and well-wishers.", "dress_code": "Cocktail Attire / Semi-Formal", "notes": "Passed canapés, signature his-and-hers mocktails/cocktails, ambient jazz music."},
                    {"day": 1, "time": "08:00 PM - 11:30 PM", "ritual": "Engagement Gala, Toasts, Cake Cutting & Dancing", "significance": "Formal couple entrance, celebratory champagne toasts, engagement cake cutting, and open dance floor.", "dress_code": "Evening Cocktail Glamour", "notes": "Wireless mic for toasts, audio console, photographer on couple stage."}
                ],
                "default_budget_split": {"Venue & Stays": 35, "Catering & Delicacies": 32, "Decor & Mandap Art": 12, "Photography & Film": 11, "Attire & Trousseau": 5, "Entertainment & Logistics": 3, "Buffer Reserve": 2}
            },
            "Catholic Holy Matrimony & Nuptial Mass": {
                "rituals": [
                    {"day": 1, "time": "05:00 PM - 07:00 PM", "ritual": "Church Rehearsal & Confession Walkthrough", "significance": "Reviewing liturgical movements, altar reverences, and mass readings with the parish priest.", "dress_code": "Modest Semi-Formal", "notes": "Coordinate lectors for 1st and 2nd scripture readings with parish coordinator."},
                    {"day": 1, "time": "07:30 PM - 10:00 PM", "ritual": "Rehearsal Welcome Dinner", "significance": "Pre-wedding dinner bringing both families together in gratitude and celebration.", "dress_code": "Smart Casual", "notes": "Private dining room reservation, toast speech microphone."},
                    {"day": 2, "time": "01:30 PM - 03:15 PM", "ritual": "Solemn Nuptial Mass & Liturgy of the Eucharist", "significance": "Full Catholic Mass with scripture readings, solemn consent, exchange of rings, arras/lazo (if traditional), and Holy Communion.", "dress_code": "Cathedral Length White Gown with Veil & Dark Tuxedo", "notes": "Pew missalettes, choir organist, kneeler cushions for bride and groom."},
                    {"day": 2, "time": "06:00 PM - 12:30 AM", "ritual": "Grand Ballroom Reception & Gala Dinner", "significance": "Grand bridal party entrance, formal banquet, wedding cake cutting, first dance, and celebration.", "dress_code": "Black-Tie / Ballgowns", "notes": "Live 7-piece wedding orchestra or DJ, champagne toast service."}
                ],
                "default_budget_split": {"Venue & Stays": 35, "Catering & Delicacies": 30, "Decor & Mandap Art": 12, "Photography & Film": 12, "Attire & Trousseau": 6, "Entertainment & Logistics": 3, "Buffer Reserve": 2}
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
                    {"day": 1, "time": "04:00 PM - 07:00 PM", "ritual": "Manjha & Mayun (Turmeric Ceremony)", "significance": "Beautification and cleansing ceremony with female relatives and cousins.", "dress_code": "Mustard Yellow Shararas & Kurtas", "notes": "Floral jewelry, marigold canopies, and traditional dholak."},
                    {"day": 1, "time": "07:30 PM - 11:30 PM", "ritual": "Festive Mehndi & Henna Gathering", "significance": "Intricate henna application with family musical performances and folk songs.", "dress_code": "Emerald Green & Teal Anarkalis", "notes": "Multiple henna artists and live acoustic singers."},
                    {"day": 2, "time": "11:00 AM - 01:30 PM", "ritual": "Nikah Ceremony & Ijab-e-Qubool", "significance": "Solemn marriage contract signing witnessed by Qazi and guardians with collective Dua.", "dress_code": "Regal Ivory Sherwani & Embroidered Pastel Gharara", "notes": "Mahr contract ready, sweet dates and rosewater for guests."},
                    {"day": 2, "time": "08:00 PM - 12:30 AM", "ritual": "Grand Walima Reception", "significance": "Sunnah banquet hosted by groom's family to celebrate the union.", "dress_code": "Formal Black-Tie / Embroidered Royal Tuxedo & Lehenga", "notes": "Royal dum biryani, kebabs, sheer khurma, and stage photography."}
                ],
                "default_budget_split": {"Venue & Stays": 32, "Catering & Delicacies": 34, "Decor & Mandap Art": 14, "Photography & Film": 10, "Attire & Trousseau": 6, "Entertainment & Logistics": 2, "Buffer Reserve": 2}
            },
            "1-Day Nikah Solemnization & Walima Feast": {
                "rituals": [
                    {"day": 1, "time": "10:30 AM - 11:45 AM", "ritual": "Baraat Swagat & Arrival", "significance": "Groom entourage arrives with rosewater spray and warm family greetings.", "dress_code": "Classic Embroidered Sherwani with Turban", "notes": "Welcome stage and fragrant jasmine garlands."},
                    {"day": 1, "time": "12:00 PM - 01:30 PM", "ritual": "Nikah Ceremony (Khutbah, Ijab-e-Qubool & Dua)", "significance": "Recitation of Quranic marriage khutbah, offer and acceptance in front of witnesses, and signing Nikah-nama.", "dress_code": "Traditional Royal Attire", "notes": "Qazi mic setup, marriage certificate pens, dates distribution."},
                    {"day": 1, "time": "01:45 PM - 03:30 PM", "ritual": "Grand Nikah Dawat (Royal Halal Feast)", "significance": "Lavish celebratory lunch featuring authentic biryani, kebabs, and traditional desserts.", "dress_code": "Festive Modest Wear", "notes": "Full halal certification, separate or family seating arranged."},
                    {"day": 1, "time": "07:30 PM - 11:30 PM", "ritual": "Grand Walima Reception & Stage Felicitations", "significance": "Formal celebratory banquet honoring the newlyweds with family photography and felicitations.", "dress_code": "Evening Royal Couture", "notes": "Bridal stage photography, live instrumental sufi music."}
                ],
                "default_budget_split": {"Venue & Stays": 33, "Catering & Delicacies": 35, "Decor & Mandap Art": 13, "Photography & Film": 10, "Attire & Trousseau": 5, "Entertainment & Logistics": 2, "Buffer Reserve": 2}
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
            },
            "1-Day Gurdwara Anand Karaj & Langar Seva": {
                "rituals": [
                    {"day": 1, "time": "08:30 AM - 09:30 AM", "ritual": "Milni Swagat at Gurdwara", "significance": "Greeting and flower garland exchange between corresponding elders.", "dress_code": "Modest Formal with Head Coverings", "notes": "Head scarves provided at entrance, shoe room managed."},
                    {"day": 1, "time": "09:45 AM - 11:30 AM", "ritual": "Sacred Anand Karaj (4 Lavaan Around Sri Guru Granth Sahib Ji)", "significance": "Holy marriage hymn recitation and circumambulation led by Granthi Sahib.", "dress_code": "Traditional Regal Punjabi Attire", "notes": "Karah Parshad prepared, Ragi Jatha acoustic harmonium."},
                    {"day": 1, "time": "11:45 AM - 01:30 PM", "ritual": "Guru Ka Langar Seva & Community Feast", "significance": "Sacred community vegetarian meal served on floor mats in the Langar Hall.", "dress_code": "Modest Attire", "notes": "Seva team organized, hot dal and prashad distribution."},
                    {"day": 1, "time": "07:00 PM - 11:30 PM", "ritual": "Grand Evening Reception & Bhangra Celebration", "significance": "Formal gala, stage felicitations, lavish dinner buffet, and dance floor.", "dress_code": "Black-Tie / Haute Couture Lehengas", "notes": "Live dhol drummers, DJ setup, couple grand entrance."}
                ],
                "default_budget_split": {"Venue & Stays": 31, "Catering & Delicacies": 33, "Decor & Mandap Art": 14, "Photography & Film": 11, "Attire & Trousseau": 5, "Entertainment & Logistics": 4, "Buffer Reserve": 2}
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
            },
            "1-Day Chuppah, Ketubah & Kosher Simcha Gala": {
                "rituals": [
                    {"day": 1, "time": "03:00 PM - 04:15 PM", "ritual": "Kabbalat Panim, Chosson's Tish & Ketubah Signing", "significance": "Separate greeting receptions, singing at groom's table, and formal signing of the Ketubah with two witnesses.", "dress_code": "Formal Attire with Kippah", "notes": "Ketubah table, kosher wine cups, observant witnesses present."},
                    {"day": 1, "time": "04:30 PM - 05:15 PM", "ritual": "Badeken (Veiling of the Bride)", "significance": "Groom veils the bride accompanied by joyful singing and parental blessings.", "dress_code": "Bridal Gown & Formal Suit", "notes": "Bridal throne chair, photographer ready for emotional reveal."},
                    {"day": 1, "time": "05:30 PM - 06:45 PM", "ritual": "Chuppah Ceremony & Glass Breaking", "significance": "Processional, Hakafot, Kiddushin, Sheva Brachot, and groom breaking the glass with joyful 'Mazel Tov!' shouts.", "dress_code": "Black-Tie / Formal Modest Wear", "notes": "Chuppah floral canopy, sound system for rabbi, linen-wrapped glass."},
                    {"day": 1, "time": "07:00 PM - 08:00 PM", "ritual": "Yichud & Sunset Cocktail Hour", "significance": "Couple shares intimate secluded moments while guests enjoy passed kosher hors d'oeuvres.", "dress_code": "Formal Evening Wear", "notes": "Private room with light refreshments for couple; cocktail bar open for guests."},
                    {"day": 1, "time": "08:15 PM - 12:30 AM", "ritual": "The Horah Circle Dance, Kosher Feast & Celebration", "significance": "Lifting bride and groom on chairs, Hamotzi blessing, multi-course glatt kosher banquet, and dancing.", "dress_code": "Black-Tie Gala", "notes": "Live Klezmer/simcha band, certified kosher catering team, Birkat Hamazon booklets."}
                ],
                "default_budget_split": {"Venue & Stays": 35, "Catering & Delicacies": 32, "Decor & Mandap Art": 13, "Photography & Film": 11, "Attire & Trousseau": 4, "Entertainment & Logistics": 3, "Buffer Reserve": 2}
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
            },
            "1-Day Tea Ceremony & Multi-Course Celebration Banquet": {
                "rituals": [
                    {"day": 1, "time": "09:00 AM - 10:15 AM", "ritual": "Door Games (Chuangmen) & Bridal Fetching", "significance": "Groom and groomsmen pass playful tests by bridesmaids to prove devotion.", "dress_code": "Traditional Silk Attire", "notes": "Red packets (Hongbao) prepared, creative props ready."},
                    {"day": 1, "time": "10:30 AM - 12:30 PM", "ritual": "Sacred Ancestral Homage & Tea Ceremony", "significance": "Couple kneels and offers sweet lotus tea to parents and elders in exchange for blessings and gold heirlooms.", "dress_code": "Traditional Embroidered Cheongsam / Hanbok", "notes": "Porcelain tea cups, sweet tea brewed with longan and red dates, kneeling cushions."},
                    {"day": 1, "time": "01:00 PM - 03:00 PM", "ritual": "Family Celebration Luncheon", "significance": "Auspicious meal bringing both clans together in fellowship.", "dress_code": "Festive Semi-Formal", "notes": "Family banquet tables with traditional dishes."},
                    {"day": 1, "time": "07:00 PM - 11:00 PM", "ritual": "Grand 8-Course Wedding Banquet & Yam Seng Toasts", "significance": "Symbolic 8-course banquet representing prosperity, joyous Yam Seng toasts, and stage speeches.", "dress_code": "Formal Evening Wear / Tuxedo & Gown", "notes": "Round tables of 10, stage backdrop with Double Happiness symbol, audiovisual projector."}
                ],
                "default_budget_split": {"Venue & Stays": 34, "Catering & Delicacies": 34, "Decor & Mandap Art": 13, "Photography & Film": 10, "Attire & Trousseau": 4, "Entertainment & Logistics": 3, "Buffer Reserve": 2}
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
                    {"day": 2, "time": "10:30 AM - 01:00 PM", "ritual": "Poolside Floral Fiesta", "significance": "Organic floral shower, live food carts, and sunshine celebrations.", "dress_code": "Boho Chic / Yellows & Pastels", "notes": "Marigold petals, water spritzers, and photo stations."},
                    {"day": 2, "time": "05:30 PM - 07:30 PM", "ritual": "Sunset Vows & Cultural Exchange", "significance": "Harmonious union blending ancestral traditions with modern personal vows.", "dress_code": "Ivory / Champagne Rose Gold", "notes": "Golden hour lighting coordinates with camera drones."},
                    {"day": 2, "time": "08:30 PM - 01:30 AM", "ritual": "Gala Dinner & International After-Party", "significance": "Formal speeches, cake cutting, multi-cuisine banquet, and dancing.", "dress_code": "Black-Tie / Tuxedo / Ballgown", "notes": "Midnight dessert bar and coffee lounge."}
                ],
                "default_budget_split": {"Venue & Stays": 35, "Catering & Delicacies": 28, "Decor & Mandap Art": 15, "Photography & Film": 12, "Attire & Trousseau": 5, "Entertainment & Logistics": 3, "Buffer Reserve": 2}
            },
            "1-Day Modern Fusion Vows & Gala Reception": {
                "rituals": [
                    {"day": 1, "time": "02:00 PM - 03:30 PM", "ritual": "Dual-Heritage Exchange of Vows & Ring Ceremony", "significance": "Personalized secular or interfaith vows uniting two backgrounds under an open floral canopy.", "dress_code": "Elegant Cocktail / Modern Attire", "notes": "Bilingual or dual-tradition program cards, wireless microphones."},
                    {"day": 1, "time": "04:00 PM - 05:30 PM", "ritual": "Cultural Heritage Showcase & Mingle", "significance": "Guests enjoy passed delicacies honoring both families' heritage cultures.", "dress_code": "Cocktail Chic", "notes": "Live acoustic fusion band, interactive guestbook."},
                    {"day": 1, "time": "06:00 PM - 07:30 PM", "ritual": "Sunset Cocktail Hour & Canapés", "significance": "Golden hour drinks, hors d'oeuvres, and couple photography session.", "dress_code": "Black-Tie Optional", "notes": "Passed cocktails, mocktail spritzers, ambient lounge jazz."},
                    {"day": 1, "time": "07:45 PM - 11:30 PM", "ritual": "Dinner Banquet, Speeches, Cake Cutting & Dancing", "significance": "Couple grand entrance, speeches by loved ones, custom multi-cuisine dinner, cake cutting, and high-energy dance party.", "dress_code": "Evening Formal", "notes": "Dynamic dance floor lighting, custom dessert table, late-night snacks."}
                ],
                "default_budget_split": {"Venue & Stays": 35, "Catering & Delicacies": 30, "Decor & Mandap Art": 14, "Photography & Film": 11, "Attire & Trousseau": 5, "Entertainment & Logistics": 3, "Buffer Reserve": 2}
            }
        }
    }
}
