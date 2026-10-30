"""Personalized Multi-Tier Guest Invitation Suite for UtsavAI across World Religions."""

from typing import Dict, Any

class InvitationEngine:
    """Generates tiered and culturally personalized invitation templates for any world faith."""

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
        """Generate copy across tiers (Family, Friends, Colleagues) strictly respecting the selected religion."""

        # Determine Faith-Specific Invocations and Spiritual Verses
        rel_lower = (religion or "Hinduism").lower()

        if "christian" in rel_lower:
            invocation = "† In the Name of the Father, and of the Son, and of the Holy Spirit †"
            spiritual_verse = '"Love is patient, love is kind. It always protects, always trusts, always hopes, always perseveres." — 1 Corinthians 13:4-7'
            elder_greeting = "By the grace of the Almighty God,"
            ceremony_name = "sacred church vows and celebration"
        elif "islam" in rel_lower:
            invocation = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ\n(In the Name of Allah, the Most Gracious, the Most Merciful)"
            spiritual_verse = '"And among His signs is that He created for you mates from among yourselves, that you may dwell in tranquility." — Surah Ar-Rum 30:21'
            elder_greeting = "With the blessings of Allah (SWT) and our elders,"
            ceremony_name = "auspicious Nikah solemnization and Walima"
        elif "juda" in rel_lower:
            invocation = "בְּסִיַּעְתָּא דִשְׁמַיָּא (With the Help of Heaven) • Mazel Tov!"
            spiritual_verse = '"Ani l\'dodi v\'dodi li — I am my beloved\'s and my beloved is mine." — Song of Songs 6:3'
            elder_greeting = "With profound gratitude to the Almighty,"
            ceremony_name = "sacred Chuppah and joyful Simcha celebration"
        elif "sikh" in rel_lower:
            invocation = "॥ ੴ ਸਤਿਗੁਰ ਪ੍ਰਸਾਦਿ ॥ (Ik Onkar Satgur Prasad)"
            spiritual_verse = "By the grace of the True Guru, through devotion and humility, true union is blessed."
            elder_greeting = "With the divine blessings of Sri Guru Granth Sahib Ji,"
            ceremony_name = "sacred Anand Karaj and auspicious celebration"
        elif "buddh" in rel_lower or "east asian" in rel_lower:
            invocation = "☸ Namo Amitabha Buddha • May There Be Harmony & Blessings 囍"
            spiritual_verse = "May this sacred bond be blessed with peace, deep compassion, and lifelong harmony."
            elder_greeting = "With profound reverence for our ancestors and elders,"
            ceremony_name = "auspicious blessings, tea ceremony, and celebration banquet"
        elif "fusion" in rel_lower or "contemporary" in rel_lower:
            invocation = "✨ Two Hearts, Two Families, One Celebration ✨"
            spiritual_verse = "Celebrating the union of two unique paths and the joyous gathering of family and friends."
            elder_greeting = "With joy and gratitude in our hearts,"
            ceremony_name = "celebration and exchange of vows"
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
            spiritual_verse = "॥ મંગલમ્ ભગવાન વિષ્ણુઃ મંગલમ્ ગરુડધ્વજઃ મંગલમ્ પુંડરીકાક્ષો મંગલાય તનો હરિઃ ॥"
            elder_greeting = "With the divine blessings of our ancestors and the Almighty,"
            ceremony_name = "auspicious sacred vidhis and celebration"

        return {
            "Tier 1: Elders & Sacred Family Circle": {
                "badge": "👑 Sacred Family & Elders",
                "audience": "Immediate relatives, grandparents, church/community elders",
                "card_copy": (
                    f"{invocation}\n\n"
                    f"{spiritual_verse}\n\n"
                    f"{elder_greeting}\n"
                    f"{hosts}\n"
                    f"cordially request the honor of your gracious presence and prayers\n"
                    f"at the celebration of the {event_name} of\n\n"
                    f"✨ {honorees} ✨\n\n"
                    f"📅 Date: {dates}\n"
                    f"📍 Venue: {venue}\n\n"
                    f"Your loving presence, prayers, and elder blessings are our greatest treasure as we embark on this sacred journey.\n\n"
                    f"Warmest Regards & Blessings,\n{hosts}\nRSVP: {rsvp_contact}"
                ),
                "whatsapp_copy": (
                    f"🙏 *{invocation}*\n\n"
                    f"Respected Elders & Dear Family Members,\n\n"
                    f"{elder_greeting} {hosts} warmly invite you to join us and shower your blessings upon our beloved *{honorees}* on their *{event_name}*.\n\n"
                    f"📅 *Dates:* {dates}\n"
                    f"📍 *Venue:* {venue}\n"
                    f"📌 *Google Maps:* [Insert Venue Map Link]\n\n"
                    f"Please join us for the {ceremony_name}. Your presence is deeply cherished.\n\n"
                    f"With deep respect & love,\n*{hosts}*\n📞 RSVP: {rsvp_contact}"
                ),
                "email_copy": (
                    f"Subject: Sacred Invitation: {event_name} of {honorees} - Blessings & Prayers Solicited\n\n"
                    f"Dear Respected Elders and Family,\n\n"
                    f"We seek your revered presence and blessings as our family celebrates the {event_name} of {honorees}.\n\n"
                    f"The ceremonies will be observed in sacred solemnity across {dates} at {venue}.\n\n"
                    f"A detailed day-wise itinerary and program is attached for your convenience. Please grace the occasion with your presence and prayers.\n\n"
                    f"Respectfully,\n{hosts}\nContact: {rsvp_contact}"
                )
            },
            "Tier 2: Close Friends & Celebration Circle": {
                "badge": "🎉 Friends & Entourage",
                "audience": "Cousins, friends, bridal party, youth entourage",
                "card_copy": (
                    f"The Celebration of a Lifetime Begins! 🌟\n\n"
                    f"Get ready for unforgettable music, cocktails, delicious feasts, and non-stop dancing!\n\n"
                    f"Join us in celebrating the {event_name} of\n"
                    f"💫 {honorees} 💫\n\n"
                    f"📅 Dates: {dates}\n"
                    f"📍 Location: {venue}\n\n"
                    f"Bring your dancing shoes, your best fits, and your loudest cheers!\n\n"
                    f"RSVP & Music Playlist Submissions: {rsvp_contact}"
                ),
                "whatsapp_copy": (
                    f"🔥 *SAVE THE DATES: IT'S CELEBRATION TIME!* 🔥\n\n"
                    f"Hey friends! The countdown has officially begun! We're celebrating the *{event_name}* of *{honorees}*!\n\n"
                    f"Expect grand vibes, amazing food, great music, and memories for life! 💃🕺🥂\n\n"
                    f"🗓️ *When:* {dates}\n"
                    f"📍 *Where:* {venue}\n"
                    f"👗 *Dress Theme:* Check Itinerary for daily attire vibe check!\n\n"
                    f"Drop your RSVPs ASAP so we can reserve your welcome kits and party spots!\n"
                    f"📞 Ping: {rsvp_contact}"
                ),
                "email_copy": (
                    f"Subject: You're Invited! Join the Celebration of {honorees}'s {event_name}! 🥂\n\n"
                    f"Dear Friends,\n\n"
                    f"We're getting ready to host an extraordinary celebration and it wouldn't be complete without you!\n\n"
                    f"Join {honorees} for the {event_name} from {dates} at {venue}.\n\n"
                    f"Pack your party outfits and prepare for an unforgettable gathering.\n\n"
                    f"See you on the dance floor!\nCheers,\n{hosts}"
                )
            },
            "Tier 3: Esteemed Colleagues & Network": {
                "badge": "💼 Professional Network & Community",
                "audience": "Colleagues, business associates, neighborhood community",
                "card_copy": (
                    f"Warm Greetings,\n\n"
                    f"{hosts} take immense pleasure in inviting you and your family to the {event_name} celebration of\n\n"
                    f"✨ {honorees} ✨\n\n"
                    f"We would be delighted to have your company as we celebrate this special personal milestone.\n\n"
                    f"📅 Date & Time: {dates}\n"
                    f"📍 Venue: {venue}\n\n"
                    f"Dinner Banquet & Reception to follow.\n\n"
                    f"Warm Regards,\n{hosts}\nRSVP: {rsvp_contact}"
                ),
                "whatsapp_copy": (
                    f"Dear Colleague / Friend,\n\n"
                    f"Warm greetings from *{hosts}*.\n\n"
                    f"You and your family are cordially invited to celebrate the *{event_name}* of *{honorees}*.\n\n"
                    f"📅 *Date:* {dates}\n"
                    f"📍 *Venue:* {venue}\n"
                    f"🍽️ *Dinner Reception:* Evening onwards\n\n"
                    f"We look forward to welcoming you and celebrating together.\n\n"
                    f"Best wishes,\n*{hosts}*\nRSVP: {rsvp_contact}"
                ),
                "email_copy": (
                    f"Subject: Cordial Invitation: {event_name} Reception of {honorees}\n\n"
                    f"Dear Colleague / Associate,\n\n"
                    f"It is our great pleasure to invite you and your family to join us in celebrating the {event_name} of {honorees}.\n\n"
                    f"The Reception banquet will take place on {dates} at {venue}.\n\n"
                    f"We would be honored by your gracious company on this celebratory evening.\n\n"
                    f"Warm regards,\n{hosts}\nRSVP: {rsvp_contact}"
                )
            }
        }
