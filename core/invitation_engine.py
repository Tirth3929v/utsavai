"""Personalized Multi-Tier Guest Invitation Suite for UtsavAI across World Religions & Events."""

from typing import Dict, Any

class InvitationEngine:
    """Generates tiered and culturally personalized invitation templates for any world faith and event type."""

    @classmethod
    def get_default_metadata(
        cls,
        religion: str = "Hinduism",
        event_type: str = "Grand Wedding",
        country: str = "India",
        city: str = "Surat"
    ) -> Dict[str, str]:
        """Provides culturally and event-appropriate sample defaults for hosts, honorees, and venues."""
        rel_lower = (religion or "Hinduism").lower()
        evt_lower = (event_type or "Grand Wedding").lower()

        is_wedding = ("wedding" in evt_lower or "matrimony" in evt_lower or "vivaha" in evt_lower or
                      "nikah" in evt_lower or "anand karaj" in evt_lower or "marriage" in evt_lower)
        is_anniversary = ("anniversary" in evt_lower or "milestone" in evt_lower or "jubilee" in evt_lower) and not is_wedding
        is_engagement = ("engagement" in evt_lower or "ring" in evt_lower or "sagai" in evt_lower or "mangni" in evt_lower or "roka" in evt_lower or "kurmai" in evt_lower or "vort" in evt_lower) and not is_wedding
        is_puja = ("vidhi" in evt_lower or "puja" in evt_lower or "prayer" in evt_lower or "havan" in evt_lower or "paath" in evt_lower) and not is_wedding
        is_festival = ("festival" in evt_lower or "community" in evt_lower or "cultural gala" in evt_lower or "utsav" in evt_lower or "milan" in evt_lower) and not (is_wedding or is_engagement or is_anniversary or is_puja)

        if "christian" in rel_lower:
            if is_anniversary:
                return {
                    "host_names": "The Anderson Family & Children",
                    "honoree_names": "Arthur & Eleanor Anderson (Golden 50th Anniversary)",
                    "venue_location": "St. Regis Grand Ballroom & Terrace",
                    "rsvp_contact": "celebrate@andersonfamily.org / +1 (555) 345-6789"
                }
            elif is_festival:
                return {
                    "host_names": "St. Michael's Cultural Committee",
                    "honoree_names": "Annual Festival of Fellowship & Heritage",
                    "venue_location": "Metropolitan Cathedral Fellowship Hall",
                    "rsvp_contact": "events@stmichaelscatholic.org / +1 (555) 789-0123"
                }
            elif is_puja:
                return {
                    "host_names": "The Anderson Family",
                    "honoree_names": "Thanksgiving & Family Prayer Service for David & Sarah",
                    "venue_location": "Grace Chapel & Fellowship Garden",
                    "rsvp_contact": "rsvp@andersonfamily.org / +1 (555) 234-5678"
                }
            elif is_engagement:
                return {
                    "host_names": "The Anderson & Miller Families",
                    "honoree_names": "David & Sarah",
                    "venue_location": "The Waterfront Pavilion & Lakeview Terrace",
                    "rsvp_contact": "rsvp@davidandsarah.org / +1 (555) 234-5678"
                }
            else:
                # Wedding
                return {
                    "host_names": "The Anderson & Miller Families",
                    "honoree_names": "David & Sarah",
                    "venue_location": "Grace Cathedral & The Grand Ballroom",
                    "rsvp_contact": "celebrate@davidandsarah.com / +1 (555) 123-4567"
                }

        elif "islam" in rel_lower:
            if is_anniversary:
                return {
                    "host_names": "The Khan Family & Children",
                    "honoree_names": "Tariq & Amina Khan (Silver Jubilee Celebration)",
                    "venue_location": "Emirates Palace Grand Ballroom, Dubai",
                    "rsvp_contact": "tariq.khan@jubilee25.com / +971 50 123 4567"
                }
            elif is_festival:
                return {
                    "host_names": "Community Eid & Cultural Committee",
                    "honoree_names": "Annual Community Eid Milan & Cultural Dawat",
                    "venue_location": "Civic Cultural Center & Gardens",
                    "rsvp_contact": "eidfellowship@community.org / +971 50 987 6543"
                }
            elif is_puja:
                return {
                    "host_names": "The Khan Family",
                    "honoree_names": "Khatam-e-Quran & Shukrana Dua Gathering",
                    "venue_location": "Khan Family Residence & Community Hall",
                    "rsvp_contact": "dua@khanfamily.com / +971 50 456 7890"
                }
            elif is_engagement:
                return {
                    "host_names": "The Khan & Rahman Families",
                    "honoree_names": "Zayn & Fatima",
                    "venue_location": "Al-Bustan Palace & Royal Banquet, Dubai",
                    "rsvp_contact": "mangni@zaynandfatima.com / +971 50 234 5678"
                }
            else:
                return {
                    "host_names": "The Khan & Rahman Families",
                    "honoree_names": "Zayn & Fatima",
                    "venue_location": "Al-Bustan Palace & Royal Banquet, Dubai",
                    "rsvp_contact": "nikah@zaynandfatima.com / +971 50 234 5678"
                }

        elif "juda" in rel_lower:
            if is_anniversary:
                return {
                    "host_names": "The Cohen Family",
                    "honoree_names": "Samuel & Miriam Cohen (Golden 50th Anniversary)",
                    "venue_location": "The Plaza Crystal Ballroom, New York",
                    "rsvp_contact": "simcha@cohen50th.com / +1 (212) 555-8901"
                }
            elif is_festival:
                return {
                    "host_names": "Shalom Cultural Society",
                    "honoree_names": "Annual Heritage Hanukkah / Simchat Gala",
                    "venue_location": "Jewish Cultural Center Grand Pavilion",
                    "rsvp_contact": "shalom@culturalgala.org / +1 (212) 555-3456"
                }
            elif is_puja:
                return {
                    "host_names": "The Cohen Family",
                    "honoree_names": "Sacred Family Havdalah & Gratitude Service",
                    "venue_location": "Temple Beth Sholom Community Hall",
                    "rsvp_contact": "havdalah@cohenfamily.org / +1 (212) 555-6789"
                }
            elif is_engagement:
                return {
                    "host_names": "The Cohen & Goldberg Families",
                    "honoree_names": "Noah & Rebecca",
                    "venue_location": "Temple Beth Sholom Terrace & Ballroom",
                    "rsvp_contact": "tenaim@noahandrebecca.com / +1 (212) 555-7890"
                }
            else:
                return {
                    "host_names": "The Cohen & Goldberg Families",
                    "honoree_names": "Noah & Rebecca",
                    "venue_location": "Temple Beth Sholom & The Plaza Ballroom",
                    "rsvp_contact": "mazeltov@noahandrebecca.com / +1 (212) 555-7890"
                }

        elif "sikh" in rel_lower:
            if is_anniversary:
                return {
                    "host_names": "The Gill Family & Children",
                    "honoree_names": "Sardar Jaswant Singh & Sardarni Harjit Kaur Gill (50th Anniversary)",
                    "venue_location": "Royal Heritage Palace Banquet, Amritsar",
                    "rsvp_contact": "gill50th@celebrations.in / +91 98140 12345"
                }
            elif is_festival:
                return {
                    "host_names": "Gurdwara Management & Youth Committee",
                    "honoree_names": "Vaisakhi Cultural & Heritage Nagar Kirtan Gala",
                    "venue_location": "Khalsa Community Grounds & Banquet",
                    "rsvp_contact": "vaisakhi@khalsacouncil.org / +91 98140 56789"
                }
            elif is_puja:
                return {
                    "host_names": "The Gill Family",
                    "honoree_names": "Sehaj Paath Bhog & Kirtan Darbar",
                    "venue_location": "Gurdwara Darbar Sahib & Langar Hall",
                    "rsvp_contact": "paath@gillfamily.in / +91 98140 23456"
                }
            elif is_engagement:
                return {
                    "host_names": "The Gill & Dhillon Families",
                    "honoree_names": "Harpreet & Gurleen",
                    "venue_location": "Grand Amber Resort & Gardens, Chandigarh",
                    "rsvp_contact": "kurmai@harpreetgurleen.in / +91 98140 34567"
                }
            else:
                return {
                    "host_names": "The Gill & Dhillon Families",
                    "honoree_names": "Harpreet & Gurleen",
                    "venue_location": "Darbar Sahib & Royal Amber Banquet, Chandigarh",
                    "rsvp_contact": "anandkaraj@harpreetgurleen.in / +91 98140 34567"
                }

        elif "buddh" in rel_lower or "east asian" in rel_lower:
            if is_anniversary:
                return {
                    "host_names": "The Chen Family",
                    "honoree_names": "Mr. Zhang & Mrs. Mei Chen (Golden Milestone)",
                    "venue_location": "Lotus Blossom Grand Hall, Singapore",
                    "rsvp_contact": "chenfamily@longevity.sg / +65 9123 4567"
                }
            elif is_festival:
                return {
                    "host_names": "Heritage Buddhist & Cultural Association",
                    "honoree_names": "Annual Lunar Heritage & Mid-Autumn Celebration",
                    "venue_location": "Dragon Pavilion Cultural Theater",
                    "rsvp_contact": "harmony@heritagefest.sg / +65 9234 5678"
                }
            elif is_puja:
                return {
                    "host_names": "The Chen Family",
                    "honoree_names": "Monastic Chanting & Ancestral Blessing Service",
                    "venue_location": "Peace Temple Sanctuary & Tea Garden",
                    "rsvp_contact": "blessings@chenfamily.sg / +65 9345 6789"
                }
            elif is_engagement:
                return {
                    "host_names": "The Chen & Wong Families",
                    "honoree_names": "Liam & Mei-Ling",
                    "venue_location": "Harmony Dragon Banquet Pavilion, Singapore",
                    "rsvp_contact": "rsvp@liammeiling.sg / +65 9456 7890"
                }
            else:
                return {
                    "host_names": "The Chen & Wong Families",
                    "honoree_names": "Liam & Mei-Ling",
                    "venue_location": "Harmony Garden Ballroom, Singapore",
                    "rsvp_contact": "wedding@liammeiling.sg / +65 9456 7890"
                }

        elif "fusion" in rel_lower or "contemporary" in rel_lower:
            if is_anniversary:
                return {
                    "host_names": "The Carter Family & Friends",
                    "honoree_names": "Robert & Evelyn Carter (30th Milestone)",
                    "venue_location": "The Conservatory Ballroom & Skyline Terrace",
                    "rsvp_contact": "carter30th@celebrations.com / +1 (555) 901-2345"
                }
            elif is_festival:
                return {
                    "host_names": "Global Unity Cultural Forum",
                    "honoree_names": "Annual Harmony Gala & World Cultural Showcase",
                    "venue_location": "Metropolitan Arts Pavilion",
                    "rsvp_contact": "info@harmonygala.org / +1 (555) 890-1234"
                }
            elif is_puja:
                return {
                    "host_names": "The Carter Family",
                    "honoree_names": "Sacred Gratitude & Blessing Gathering for Alex & Jordan",
                    "venue_location": "Botanical Glasshouse Sanctuary",
                    "rsvp_contact": "blessings@cartersterling.com / +1 (555) 678-9012"
                }
            elif is_engagement:
                return {
                    "host_names": "The Carter & Sterling Families",
                    "honoree_names": "Alex & Jordan",
                    "venue_location": "Skyline Glasshouse & Gardens",
                    "rsvp_contact": "engagement@alexandjordan.com / +1 (555) 456-7890"
                }
            else:
                return {
                    "host_names": "The Carter & Sterling Families",
                    "honoree_names": "Alex & Jordan",
                    "venue_location": "Skyline Glasshouse & Gardens",
                    "rsvp_contact": "rsvp@alexandjordan.com / +1 (555) 456-7890"
                }

        else:
            # Hinduism / Vedic Default
            if is_anniversary:
                return {
                    "host_names": "The Mehta Family & Children",
                    "honoree_names": "Ramesh & Sharda Mehta (Golden Jubilee 50th Anniversary)",
                    "venue_location": "Grand Ambience Banquet & Lawns, Surat",
                    "rsvp_contact": "mehta50th@celebrations.in / +91 98250 12345"
                }
            elif is_festival:
                return {
                    "host_names": "Shri Cultural Utsav Samiti",
                    "honoree_names": "Annual Diwali Mahotsav & Raas Garba Gala",
                    "venue_location": "Heritage Cultural Grounds & Amphitheatre",
                    "rsvp_contact": "utsav@suratcultural.org / +91 98250 56789"
                }
            elif is_puja:
                return {
                    "host_names": "The Mehta Family",
                    "honoree_names": "Shri Satyanarayan Maha Puja & Vastu Shanti Vidhi",
                    "venue_location": "Mehta Residence & Mandir Hall, Surat",
                    "rsvp_contact": "puja@mehtafamily.in / +91 98250 23456"
                }
            elif is_engagement:
                return {
                    "host_names": "The Mehta & Shah Families",
                    "honoree_names": "Aarav & Ananya",
                    "venue_location": "The Grand Emerald Lawn & Ballroom, Surat",
                    "rsvp_contact": "sagai@aaravananya.in / +91 98250 34567"
                }
            else:
                return {
                    "host_names": "The Mehta & Shah Families",
                    "honoree_names": "Aarav & Ananya",
                    "venue_location": "Royal Heritage Palace & Resorts, Udaipur",
                    "rsvp_contact": "+91 98765 43210 / celebrate@utsavai.com"
                }

    @classmethod
    def generate_invitations(
        cls,
        event_name: str,
        hosts: str,
        honorees: str,
        tradition: str,
        venue: str,
        dates: str,
        rsvp_contact: str,
        religion: str = "Hinduism"
    ) -> Dict[str, Dict[str, str]]:
        """
        Generate copy across tiers (Family, Friends, Colleagues) strictly respecting
        BOTH the selected faith and the specific event type.
        """
        rel_lower = (religion or "Hinduism").lower()
        evt_lower = (event_name or "Grand Wedding").lower()

        is_wedding = ("wedding" in evt_lower or "matrimony" in evt_lower or "vivaha" in evt_lower or
                      "nikah" in evt_lower or "anand karaj" in evt_lower or "marriage" in evt_lower)
        is_anniversary = ("anniversary" in evt_lower or "milestone" in evt_lower or "jubilee" in evt_lower) and not is_wedding
        is_engagement = ("engagement" in evt_lower or "ring" in evt_lower or "sagai" in evt_lower or "mangni" in evt_lower or "roka" in evt_lower or "kurmai" in evt_lower or "vort" in evt_lower) and not is_wedding
        is_puja = ("vidhi" in evt_lower or "puja" in evt_lower or "prayer" in evt_lower or "havan" in evt_lower or "paath" in evt_lower) and not is_wedding
        is_festival = ("festival" in evt_lower or "community" in evt_lower or "cultural gala" in evt_lower or "utsav" in evt_lower or "milan" in evt_lower) and not (is_wedding or is_engagement or is_anniversary or is_puja)

        # -------------------------------------------------------------
        # Faith Invocations, Scripture, and Elder Greetings
        # -------------------------------------------------------------
        if "christian" in rel_lower:
            invocation = "† In the Name of the Father, and of the Son, and of the Holy Spirit †"
            elder_greeting = "By the grace of Almighty God,"
            if is_anniversary:
                spiritual_verse = '"Above all, love each other deeply, because love covers over a multitude of sins." — 1 Peter 4:8'
                ceremony_desc = "vow reaffirmation, thanksgiving liturgy, and celebratory anniversary banquet"
                journey_phrase = "honoring decades of enduring devotion, marital fidelity, and God's abundant blessings."
            elif is_festival:
                spiritual_verse = '"Every good and perfect gift is from above, coming down from the Father of heavenly lights." — James 1:17'
                ceremony_desc = "choral thanksgiving service, cultural fellowship, and celebration feast"
                journey_phrase = "celebrating our shared faith, cultural heritage, and community unity."
            elif is_puja:
                spiritual_verse = '"For where two or three gather in my name, there am I with them." — Matthew 18:20'
                ceremony_desc = "sacred prayer service, hymns of thanksgiving, and fellowship luncheon"
                journey_phrase = "gathering in prayerful devotion to seek divine blessings and peace."
            elif is_engagement:
                spiritual_verse = '"Two are better than one, because they have a good return for their labor." — Ecclesiastes 4:9'
                ceremony_desc = "sacred blessing of engagement rings and celebratory reception"
                journey_phrase = "as the betrothed couple exchanges sacred promises of commitment and prepares for marriage."
            else:
                spiritual_verse = '"Love is patient, love is kind. It always protects, always trusts, always hopes, always perseveres." — 1 Corinthians 13:4-7'
                ceremony_desc = "sacred Church Nuptial Service and Grand Gala Reception"
                journey_phrase = "as they embark on the holy covenant of Christian marriage."

        elif "islam" in rel_lower:
            invocation = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n(In the Name of Allah, the Most Gracious, the Most Merciful)"
            elder_greeting = "With the blessings of Allah (SWT) and our elders,"
            if is_anniversary:
                spiritual_verse = '"Our Lord, grant us from among our spouses and offspring comfort to our eyes." — Surah Al-Furqan 25:74'
                ceremony_desc = "Shukrana Dua and celebratory jubilee dawat"
                journey_phrase = "reflecting with gratitude on years of marital harmony and family barakah."
            elif is_festival:
                spiritual_verse = '"Celebrate the praises of your Lord, and pray for His forgiveness." — Surah An-Nasr 110:3'
                ceremony_desc = "community prayers, cultural fellowship, and traditional feast"
                journey_phrase = "celebrating our sacred traditions, fraternity, and cultural heritage."
            elif is_puja:
                spiritual_verse = '"Call upon Me; I will respond to you." — Surah Ghafir 40:60'
                ceremony_desc = "Khatam-e-Quran, sacred Dua-e-Khair, and blessed tabarruk"
                journey_phrase = "seeking the divine grace, peace, and protection of Allah (SWT)."
            elif is_engagement:
                spiritual_verse = '"And He placed between you love and mercy." — Surah Ar-Rum 30:21'
                ceremony_desc = "auspicious Mangni ceremony, ring exchange, and celebratory feast"
                journey_phrase = "as two families unite in formal betrothal and promise of union."
            else:
                spiritual_verse = '"And among His signs is that He created for you mates from among yourselves, that you may dwell in tranquility." — Surah Ar-Rum 30:21'
                ceremony_desc = "auspicious Nikah solemnization and Grand Walima banquet"
                journey_phrase = "as they unite in the Sunnah of sacred marriage and lifelong companionship."

        elif "juda" in rel_lower:
            invocation = "בְּסִיַּעְתָּא דִשְׁמַיָּא (With the Help of Heaven) • Mazel Tov!"
            elder_greeting = "With profound gratitude to the Almighty and our heritage,"
            if is_anniversary:
                spiritual_verse = '"Grow old along with me! The best is yet to be." — Ecclesiastes / Jewish Tradition'
                ceremony_desc = "reaffirmation under the canopy, tribute toasts, and kosher anniversary gala"
                journey_phrase = "honoring a beautiful lifelong journey of love, Torah values, and family devotion."
            elif is_festival:
                spiritual_verse = '"Serve the Lord with gladness; come before His presence with singing." — Psalm 100:2'
                ceremony_desc = "community candle lighting, festival songs, and holiday feast"
                journey_phrase = "celebrating Jewish heritage, perseverance, and joyful community fellowship."
            elif is_puja:
                spiritual_verse = '"The Lord bless you and keep you; the Lord make His face shine upon you." — Numbers 6:24-25'
                ceremony_desc = "sacred Havdalah blessing, Torah reflection, and Kiddush meal"
                journey_phrase = "gathering in reverence to welcome peace, spiritual warmth, and divine blessing."
            elif is_engagement:
                spiritual_verse = '"I have found the one whom my soul loves." — Song of Songs 3:4'
                ceremony_desc = "Tenaim betrothal ceremony, plate breaking, and celebratory Simcha"
                journey_phrase = "as the couple formalizes their commitment with love and ancient tradition."
            else:
                spiritual_verse = '"Ani l\'dodi v\'dodi li — I am my beloved\'s and my beloved is mine." — Song of Songs 6:3'
                ceremony_desc = "sacred Chuppah ceremony and joyous Simcha reception"
                journey_phrase = "as they establish a Jewish home rooted in love, holiness, and kindness."

        elif "sikh" in rel_lower:
            invocation = "॥ ੴ ਸਤਿਗੁਰ ਪ੍ਰਸਾਦਿ ॥ (Ik Onkar Satgur Prasad)"
            elder_greeting = "With the divine blessings of Sri Guru Granth Sahib Ji,"
            if is_anniversary:
                spiritual_verse = '"O Nanak, the True Guru has united them; they shall not be separated again."'
                ceremony_desc = "Sukhmani Sahib Paath, Ardas of thanksgiving, and family dawat"
                journey_phrase = "celebrating decades of marital dedication, seva, and divine grace."
            elif is_festival:
                spiritual_verse = '"Countless are the blessings bestowed upon us; sing praises of the Creator."'
                ceremony_desc = "Gurmat Kirtan Darbar, Langar seva, and cultural celebration"
                journey_phrase = "honoring Sikh history, egalitarian community spirit, and cultural pride."
            elif is_puja:
                spiritual_verse = '"Through devotion and humility, true union and inner peace are attained."'
                ceremony_desc = "Sehaj Paath Bhog, Anand Sahib recitation, and Guru Ka Langar"
                journey_phrase = "seeking the eternal guidance and blessings of the True Guru."
            elif is_engagement:
                spiritual_verse = '"The divine union is guided by the Almighty through patience and mutual devotion."'
                ceremony_desc = "Kurmai / Roka ceremony, presentation of Kada & ring, and celebratory feast"
                journey_phrase = "as the families unite in solemn betrothal and seek Satguru Ji\'s blessings."
            else:
                spiritual_verse = '"They are not husband and wife who merely sit together. They alone are husband and wife, who have one soul in two bodies." — Guru Amar Das Ji'
                ceremony_desc = "sacred Anand Karaj (Four Laavan) and Langar Seva followed by Reception"
                journey_phrase = "as they embark on the spiritual journey of marital unity."

        elif "buddh" in rel_lower or "east asian" in rel_lower:
            invocation = "☸ Namo Amitabha Buddha • May There Be Harmony & Blessings 囍"
            elder_greeting = "With profound reverence for our ancestors, teachers, and elders,"
            if is_anniversary:
                spiritual_verse = '"Like the deep-rooted lotus, mindful love endures through every season with grace."'
                ceremony_desc = "ancestral tea ceremony of gratitude and celebratory longevity banquet"
                journey_phrase = "honoring lifelong fidelity, familial respect, and generational wisdom."
            elif is_festival:
                spiritual_verse = '"May all beings dwell in safety, peace, and loving-kindness."'
                ceremony_desc = "cultural lantern ceremony, festive lion dance, and celebration banquet"
                journey_phrase = "celebrating ancestral customs, filial piety, and community harmony."
            elif is_puja:
                spiritual_verse = '"With peaceful hearts and focused minds, we offer gratitude for all life."'
                ceremony_desc = "monastic chanting, incense offering, and vegetarian fellowship meal"
                journey_phrase = "cultivating spiritual mindfulness, merit, and inner serenity."
            elif is_engagement:
                spiritual_verse = '"Two sincere hearts walking together bring boundless harmony to both families."'
                ceremony_desc = "betrothal gift ceremony, exchange of commitment rings, and tea offering"
                journey_phrase = "as the couple pledges mutual respect and promises lifelong devotion."
            else:
                spiritual_verse = '"May this sacred union be blessed with deep compassion, patience, and lifelong harmony."'
                ceremony_desc = "monastic blessing, traditional Tea Ceremony, and Grand Auspicious Banquet"
                journey_phrase = "as they unite their lives in mindful harmony and mutual honor."

        elif "fusion" in rel_lower or "contemporary" in rel_lower:
            invocation = "✨ Two Hearts, Two Families, One Celebration ✨"
            elder_greeting = "With joy and gratitude in our hearts,"
            if is_anniversary:
                spiritual_verse = '"Love does not consist in gazing at each other, but in looking outward together in the same direction."'
                ceremony_desc = "vow reaffirmation, memory retrospective, and anniversary gala banquet"
                journey_phrase = "celebrating an extraordinary journey of shared adventures and enduring love."
            elif is_festival:
                spiritual_verse = '"Culture connects our past to our future, uniting hearts across traditions."'
                ceremony_desc = "cultural showcase, live musical performances, and international food gala"
                journey_phrase = "celebrating diversity, creative heritage, and community solidarity."
            elif is_puja:
                spiritual_verse = '"Gratitude turns what we have into enough, and opens the door to serenity."'
                ceremony_desc = "mindful blessing ceremony, words of wisdom, and intimate dinner"
                journey_phrase = "pausing in peaceful reflection to celebrate family, love, and life."
            elif is_engagement:
                spiritual_verse = '"Love is the beginning of an incredible adventure together."'
                ceremony_desc = "modern ring exchange ceremony, sunset cocktails, and celebratory dinner"
                journey_phrase = "as they celebrate their commitment to a shared future."
            else:
                spiritual_verse = '"Celebrating the union of two unique paths and the joyous gathering of family and friends."'
                ceremony_desc = "contemporary vows exchange and Grand Evening Reception"
                journey_phrase = "as they celebrate love, unity, and the promise of tomorrow."

        else:
            # Hinduism / Vedic Default
            if "gujarati" in tradition.lower():
                invocation = "॥ શ્રી ગણેશાય નમઃ ॥ શ્રી કુળદેવી કૃપા ॥"
            elif "punjabi" in tradition.lower():
                invocation = "॥ ੴ ਸਤਿਗੁਰ ਪ੍ਰਸਾਦਿ ॥"
            elif "south indian" in tradition.lower() or "tamil" in tradition.lower():
                invocation = "॥ ॐ શ્રી ગુરુભ્યો નમઃ ॥ હરિઃ ૐ ॥"
            elif "bengali" in tradition.lower():
                invocation = "॥ ॐ શ્રી શ્રી પ્રજાપતયે નમઃ ॥"
            else:
                invocation = "॥ ॐ શ્રી ગણેશાય નમઃ ॥"

            elder_greeting = "With the divine blessings of our ancestors and the Almighty,"
            if is_anniversary:
                spiritual_verse = "॥ ॐ સહ નાવવતુ સહ નૌ ભુનક્તુ સહ વીર્યં કરવાવહૈ તેજસ્વિનાવધીતમસ્તુ મા વિદ્વિષાવહૈ ॥"
                ceremony_desc = "Swasti Vachan, Ashirwad ceremony, and celebratory jubilee feast"
                journey_phrase = "celebrating decades of marital harmony, dharma, and family blessings."
            elif is_festival:
                spiritual_verse = "॥ ॐ સર્વે ભવન્તુ સુખિનઃ સર્વે સન્તુ નિરામયાઃ સર્વે ભદ્રાણિ પશ્યન્તુ મા કશ્ચિદ્દુઃખભાગ્ભવેત્ ॥"
                ceremony_desc = "sacred Aarti, cultural Raas Garba, and traditional Mahaprasad"
                journey_phrase = "celebrating our divine cultural heritage, joy, and collective prosperity."
            elif is_puja:
                spiritual_verse = "॥ ॐ નમો ભગવતે વાસુદેવાય ॥ શ્રી કૃષ્ણાય નમઃ ॥"
                ceremony_desc = "auspicious Vedic Puja, Havan, and consecrated Mahaprasad"
                journey_phrase = "invoking the divine presence to bless our home with peace and auspiciousness."
            elif is_engagement:
                spiritual_verse = "॥ મંગલમ્ ભગવાન વિષ્ણુઃ મંગલમ્ ગરુડધ્વજઃ મંગલમ્ પુંડરીકાક્ષો મંગલાય તનો હરિઃ ॥"
                ceremony_desc = "auspicious Sagai, Tilak vidhi, and ring exchange ceremony"
                journey_phrase = "as the families unite in sacred commitment and seek elders' blessings."
            else:
                spiritual_verse = "॥ મંગલમ્ ભગવાન વિષ્ણુઃ મંગલમ્ ગરુડધ્વજઃ મંગલમ્ પુંડરીકાક્ષો મંગલાય તનો હરિઃ ॥"
                ceremony_desc = "sacred Vivah Sanskar vidhis and Grand Reception feast"
                journey_phrase = "as they take the sacred Saptapadi steps together in holy matrimony."

        # -------------------------------------------------------------
        # Tier 1: Elders & Sacred Family Circle
        # -------------------------------------------------------------
        t1_card = (
            f"{invocation}\n\n"
            f"{spiritual_verse}\n\n"
            f"{elder_greeting}\n"
            f"{hosts}\n"
            f"cordially request the honor of your gracious presence and prayers\n"
            f"at the {event_name} of\n\n"
            f"✨ {honorees} ✨\n\n"
            f"📅 Date: {dates}\n"
            f"📍 Venue: {venue}\n\n"
            f"Program: {ceremony_desc.title()}\n\n"
            f"Your loving presence, prayers, and elder blessings are our greatest treasure {journey_phrase}\n\n"
            f"Warmest Regards & Respect,\n{hosts}\nRSVP: {rsvp_contact}"
        )

        t1_wa = (
            f"🙏 *{invocation}*\n\n"
            f"Respected Elders & Dear Family Members,\n\n"
            f"{elder_greeting} *{hosts}* warmly invite you to grace the *{event_name}* of our beloved *{honorees}*.\n\n"
            f"📅 *Dates:* {dates}\n"
            f"📍 *Venue:* {venue}\n"
            f"🕊️ *Ceremony:* {ceremony_desc.title()}\n\n"
            f"Your presence and prayers are deeply cherished {journey_phrase}\n\n"
            f"With highest respect & love,\n*{hosts}*\n📞 RSVP: {rsvp_contact}"
        )

        t1_email = (
            f"Subject: Sacred Invitation: {event_name} of {honorees} — Blessings Solicited\n\n"
            f"Dear Respected Elders and Family,\n\n"
            f"{elder_greeting}\n\n"
            f"We seek your revered presence, prayers, and blessings as our family celebrates the {event_name} of {honorees}.\n\n"
            f"The ceremonies will be observed across {dates} at {venue}.\n"
            f"Program Highlights: {ceremony_desc.title()}.\n\n"
            f"We look forward to welcoming you. Your blessings mean the world to our family {journey_phrase}\n\n"
            f"Respectfully,\n{hosts}\nContact: {rsvp_contact}"
        )

        # -------------------------------------------------------------
        # Tier 2: Close Friends & Celebration Circle
        # -------------------------------------------------------------
        if is_puja:
            t2_card = (
                f"Sacred Prayer & Family Gathering 🙏✨\n\n"
                f"You are warmly invited to join us for the {event_name} of\n"
                f"💫 {honorees} 💫\n\n"
                f"📅 Date: {dates}\n"
                f"📍 Location: {venue}\n\n"
                f"Join us for devotional prayers, spiritual blessings, and a consecrated feast with close family and friends.\n\n"
                f"Warm Regards,\n{hosts}\nRSVP: {rsvp_contact}"
            )
            t2_wa = (
                f"🕊️ *SACRED FAMILY PRAYER INVITATION* 🕊️\n\n"
                f"Dear Friends & Family, you are warmly invited to join us for the *{event_name}* of *{honorees}*.\n\n"
                f"🗓️ *When:* {dates}\n"
                f"📍 *Where:* {venue}\n"
                f"🪔 *Ceremony:* {ceremony_desc.title()}\n\n"
                f"Please join us in seeking blessings followed by a blessed fellowship meal.\n"
                f"📞 Ping: {rsvp_contact}"
            )
            t2_email = (
                f"Subject: You're Invited: {event_name} & Prayer Gathering of {honorees}\n\n"
                f"Dear Friends,\n\n"
                f"Please join us in observing the {event_name} of {honorees} on {dates} at {venue}.\n\n"
                f"The prayer service will be followed by a blessed meal and warm fellowship. We would be honored to have you with us.\n\n"
                f"Warmly,\n{hosts}"
            )
        elif is_anniversary:
            t2_card = (
                f"A Lifetime of Love & Milestone Celebration! 🥂✨\n\n"
                f"Decades of laughter, togetherness, and wonderful memories!\n\n"
                f"Join us as we raise a toast to the {event_name} of\n"
                f"💫 {honorees} 💫\n\n"
                f"📅 Date: {dates}\n"
                f"📍 Location: {venue}\n\n"
                f"Get ready for heartwarming tribute toasts, great music, delicious dining, and dancing the night away!\n\n"
                f"RSVP & Toast Coordination: {rsvp_contact}"
            )
            t2_wa = (
                f"🥂 *CELEBRATING A LIFETIME OF LOVE!* 🥂\n\n"
                f"Hey everyone! Join us for a milestone celebration honoring the *{event_name}* of *{honorees}*!\n\n"
                f"Expect heartfelt toasts, amazing dinner, nostalgic stories, and plenty of dancing! 💃🕺✨\n\n"
                f"🗓️ *When:* {dates}\n"
                f"📍 *Where:* {venue}\n\n"
                f"Drop your RSVPs ASAP to reserve your seats for this special evening!\n"
                f"📞 Ping: {rsvp_contact}"
            )
            t2_email = (
                f"Subject: Milestone Celebration: Honoring the {event_name} of {honorees}! 🥂\n\n"
                f"Dear Friends,\n\n"
                f"We are throwing a special celebration to honor the {event_name} of {honorees} on {dates} at {venue}.\n\n"
                f"Join us for tribute speeches, exceptional dining, and an unforgettable evening of celebration.\n\n"
                f"See you there!\nCheers,\n{hosts}"
            )
        elif is_engagement:
            t2_card = (
                f"The Ring Exchange Celebration! 💍✨\n\n"
                f"The countdown has begun as two hearts pledge their forever!\n\n"
                f"Join us in celebrating the {event_name} of\n"
                f"💫 {honorees} 💫\n\n"
                f"📅 Dates: {dates}\n"
                f"📍 Location: {venue}\n\n"
                f"Bring your brightest smiles, your party fits, and let's toast to the newly engaged couple!\n\n"
                f"RSVP & Playlist Requests: {rsvp_contact}"
            )
            t2_wa = (
                f"💍 *SAVE THE DATE: THEY SAID YES!* 💍\n\n"
                f"Hey friends! We're celebrating the *{event_name}* of *{honorees}*!\n\n"
                f"Get ready for sunset drinks, ring exchange cheers, great music, and celebration vibes! 🥂🎉\n\n"
                f"🗓️ *When:* {dates}\n"
                f"📍 *Where:* {venue}\n"
                f"👗 *Vibe Check:* Chic Evening Cocktail / Festive Glam\n\n"
                f"Drop your RSVPs so we can get your party spots ready!\n"
                f"📞 Ping: {rsvp_contact}"
            )
            t2_email = (
                f"Subject: You're Invited! Celebrate the {event_name} of {honorees}! 💍\n\n"
                f"Dear Friends,\n\n"
                f"We are thrilled to invite you to celebrate the {event_name} of {honorees} on {dates} at {venue}.\n\n"
                f"Pack your party outfits and come ready to toast, laugh, and celebrate this special milestone!\n\n"
                f"Cheers,\n{hosts}"
            )
        elif is_festival:
            t2_card = (
                f"Celebrate Our Culture & Festive Heritage! 🏮🎶\n\n"
                f"Get ready for vibrant music, traditional arts, delicious street treats, and festive fellowship!\n\n"
                f"Join us for the {event_name}\n"
                f"✨ {honorees} ✨\n\n"
                f"📅 Dates: {dates}\n"
                f"📍 Location: {venue}\n\n"
                f"Bring your friends and family for an unforgettable cultural showcase!\n\n"
                f"RSVP: {rsvp_contact}"
            )
            t2_wa = (
                f"🏮 *FESTIVAL TIME: JOIN THE CELEBRATION!* 🏮\n\n"
                f"Hey friends! The *{event_name}* is here! Celebrating *{honorees}* with music, food, and culture! 🎶🍲🎉\n\n"
                f"🗓️ *When:* {dates}\n"
                f"📍 *Where:* {venue}\n\n"
                f"Bring your highest energy and enjoy live performances and festive culinary feasts!\n"
                f"📞 Ping: {rsvp_contact}"
            )
            t2_email = (
                f"Subject: Festive Gathering: Join us for the {event_name}! 🏮\n\n"
                f"Dear Friends,\n\n"
                f"You're warmly invited to join us for the {event_name} featuring {honorees} on {dates} at {venue}.\n\n"
                f"Look forward to an evening of rich cultural performances, live entertainment, and authentic food.\n\n"
                f"Best regards,\n{hosts}"
            )
        else:
            # Grand Wedding
            t2_card = (
                f"The Celebration of a Lifetime Begins! 🌟\n\n"
                f"Get ready for unforgettable music, cocktails, delicious feasts, and non-stop dancing!\n\n"
                f"Join us in celebrating the {event_name} of\n"
                f"💫 {honorees} 💫\n\n"
                f"📅 Dates: {dates}\n"
                f"📍 Location: {venue}\n\n"
                f"Bring your dancing shoes, your best fits, and your loudest cheers!\n\n"
                f"RSVP & Playlist Requests: {rsvp_contact}"
            )
            t2_wa = (
                f"🔥 *SAVE THE DATES: IT'S CELEBRATION TIME!* 🔥\n\n"
                f"Hey friends! The countdown has officially begun! We're celebrating the *{event_name}* of *{honorees}*!\n\n"
                f"Expect grand vibes, amazing food, great music, and memories for life! 💃🕺🥂\n\n"
                f"🗓️ *When:* {dates}\n"
                f"📍 *Where:* {venue}\n"
                f"👗 *Dress Theme:* Check Itinerary for daily attire vibe check!\n\n"
                f"Drop your RSVPs ASAP so we can reserve your party spots!\n"
                f"📞 Ping: {rsvp_contact}"
            )
            t2_email = (
                f"Subject: You're Invited! Join the Celebration of {honorees}'s {event_name}! 🥂\n\n"
                f"Dear Friends,\n\n"
                f"We're getting ready to host an extraordinary celebration and it wouldn't be complete without you!\n\n"
                f"Join {honorees} for the {event_name} from {dates} at {venue}.\n\n"
                f"Pack your party outfits and prepare for an unforgettable gathering.\n\n"
                f"See you on the dance floor!\nCheers,\n{hosts}"
            )

        # -------------------------------------------------------------
        # Tier 3: Esteemed Colleagues & Network
        # -------------------------------------------------------------
        t3_card = (
            f"Warm Greetings,\n\n"
            f"{hosts} take immense pleasure in inviting you and your family to the {event_name} celebration of\n\n"
            f"✨ {honorees} ✨\n\n"
            f"We would be delighted to have your company as we celebrate this special milestone.\n\n"
            f"📅 Date & Time: {dates}\n"
            f"📍 Venue: {venue}\n\n"
            f"Dinner Banquet & Reception to follow.\n\n"
            f"Warm Regards,\n{hosts}\nRSVP: {rsvp_contact}"
        )

        t3_wa = (
            f"Dear Colleague / Friend,\n\n"
            f"Warm greetings from *{hosts}*.\n\n"
            f"You and your family are cordially invited to celebrate the *{event_name}* of *{honorees}*.\n\n"
            f"📅 *Date:* {dates}\n"
            f"📍 *Venue:* {venue}\n"
            f"🍽️ *Dinner Reception:* Evening onwards\n\n"
            f"We look forward to welcoming you and celebrating together.\n\n"
            f"Best wishes,\n*{hosts}*\nRSVP: {rsvp_contact}"
        )

        t3_email = (
            f"Subject: Cordial Invitation: {event_name} Reception of {honorees}\n\n"
            f"Dear Colleague / Associate,\n\n"
            f"It is our great pleasure to invite you and your family to join us in celebrating the {event_name} of {honorees}.\n\n"
            f"The celebration and banquet will take place on {dates} at {venue}.\n\n"
            f"We would be honored by your gracious company on this celebratory occasion.\n\n"
            f"Warm regards,\n{hosts}\nRSVP: {rsvp_contact}"
        )

        return {
            "Tier 1: Elders & Sacred Family Circle": {
                "badge": "👑 Sacred Family & Elders",
                "audience": "Immediate relatives, grandparents, religious & community elders",
                "card_copy": t1_card,
                "whatsapp_copy": t1_wa,
                "email_copy": t1_email
            },
            "Tier 2: Close Friends & Celebration Circle": {
                "badge": "🎉 Friends & Entourage",
                "audience": "Cousins, close friends, wedding party, youth entourage",
                "card_copy": t2_card,
                "whatsapp_copy": t2_wa,
                "email_copy": t2_email
            },
            "Tier 3: Esteemed Colleagues & Network": {
                "badge": "💼 Professional Network & Community",
                "audience": "Colleagues, business associates, neighborhood community",
                "card_copy": t3_card,
                "whatsapp_copy": t3_wa,
                "email_copy": t3_email
            }
        }
