"""Personalized Multi-Tier Guest Invitation Suite for UtsavAI."""

from typing import Dict, Any

class InvitationEngine:
    """Generates tiered and culturally personalized invitation templates."""

    @classmethod
    def generate_invitations(
        cls,
        event_name: str,
        hosts: str,
        honorees: str,
        tradition: str,
        venue: str,
        dates: str,
        rsvp_contact: str
    ) -> Dict[str, Dict[str, str]]:
        """Generate copy across tiers (Family, Friends, Colleagues) and mediums."""

        # Tradition invocation header
        if "Gujarati" in tradition:
            invocation = "॥ શ્રી ગણેશાય નમઃ ॥ શ્રી કુળદેવી કૃપા ॥"
        elif "Punjabi" in tradition:
            invocation = "॥ ੴ ਸਤਿਗੁਰ ਪ੍ਰਸਾਦਿ ॥"
        elif "South Indian" in tradition:
            invocation = "॥ ॐ શ્રી ગુરુભ્યો નમઃ ॥ હરિઃ ૐ ॥"
        elif "Bengali" in tradition:
            invocation = "॥ ॐ શ્રી શ્રી પ્રજાપતયે નમઃ ॥"
        else:
            invocation = "॥ ॐ શ્રી ગણેશાય નમઃ ॥"

        return {
            "Tier 1: Elders & Sacred Family Circle": {
                "badge": "👑 Sacred Family & Elders",
                "audience": "Immediate relatives, grandparents, elder patrons",
                "card_copy": (
                    f"{invocation}\n\n"
                    f"With the divine blessings of our ancestors and the Almighty,\n"
                    f"{hosts}\n"
                    f"cordially request the honor of your gracious presence and heartfelt blessings\n"
                    f"on the auspicious occasion of the {event_name} of\n\n"
                    f"✨ {honorees} ✨\n\n"
                    f"📅 Auspicious Dates: {dates}\n"
                    f"📍 Sacred Venue: {venue}\n\n"
                    f"Your loving presence and elder blessings are our greatest treasure as we embark on this sacred journey.\n\n"
                    f"Warm Regards & Pranaam,\n{hosts}\nRSVP: {rsvp_contact}"
                ),
                "whatsapp_copy": (
                    f"🙏 *{invocation}* 🙏\n\n"
                    f"Respected Elders & Dear Family Members,\n\n"
                    f"By God's supreme grace, {hosts} warmly invite you to shower your eternal blessings upon our beloved *{honorees}* on their *{event_name}*.\n\n"
                    f"🪔 *Dates:* {dates}\n"
                    f"📍 *Venue:* {venue}\n"
                    f"📌 *Google Maps:* [Insert Venue Map Link]\n\n"
                    f"Please join us from the morning prayers onwards. Your presence is essential for all auspicious vidhis.\n\n"
                    f"With deep respect & love,\n*{hosts}*\n📞 RSVP: {rsvp_contact}"
                ),
                "email_copy": (
                    f"Subject: Sacred Invitation: {event_name} of {honorees} - Blessings Solicited\n\n"
                    f"Dear Respected Elders and Family,\n\n"
                    f"We seek your revered presence and blessings as our family celebrates the {event_name} of {honorees}.\n\n"
                    f"The ceremonies will be observed in traditional sanctity across {dates} at {venue}.\n\n"
                    f"A detailed day-wise Muhurat and ritual schedule is attached for your convenience. Please grace the occasion and make our celebration complete.\n\n"
                    f"Respectfully,\n{hosts}\nContact: {rsvp_contact}"
                )
            },
            "Tier 2: Close Friends & Celebration Circle": {
                "badge": "🎉 Friends & Entourage",
                "audience": "Cousins, college friends, youth squad, squad entourage",
                "card_copy": (
                    f"The Celebration of a Lifetime Begins! 🌟\n\n"
                    f"Get ready for non-stop dhol beats, vibrant garba, stellar sangeet routines, and unlimited feasts!\n\n"
                    f"Celebrate the {event_name} of\n"
                    f"💫 {honorees} 💫\n\n"
                    f"📅 Dates: {dates}\n"
                    f"📍 Location: {venue}\n\n"
                    f"Bring your dancing shoes, your best festive fits, and your loudest cheers!\n\n"
                    f"RSVP & Sangeet Track Submissions: {rsvp_contact}"
                ),
                "whatsapp_copy": (
                    f"🔥 *SAVE THE DATES: IT'S CELEBRATION TIME!* 🔥\n\n"
                    f"Hey guys! The wait is finally over! We're celebrating the *{event_name}* of *{honorees}*!\n\n"
                    f"Expect madness, unforgettable Sangeet dance face-offs, midnight food carts, and memories for life! 💃🕺\n\n"
                    f"🗓️ *When:* {dates}\n"
                    f"📍 *Where:* {venue}\n"
                    f"👗 *Dress Themes:* Check Itinerary Tab for daily vibe check!\n\n"
                    f"Drop your RSVPs ASAP so we can reserve your welcome kits and party spots!\n"
                    f"📞 Ping: {rsvp_contact}"
                ),
                "email_copy": (
                    f"Subject: You're Invited! Join the Celebration of {honorees}'s {event_name}! 🥂\n\n"
                    f"Dear Friends,\n\n"
                    f"We're getting ready to host an extraordinary celebration and it wouldn't be complete without you!\n\n"
                    f"Join {honorees} for the {event_name} from {dates} at {venue}.\n\n"
                    f"Pack your glamorous outfits for the Sangeet and prepare for grand celebrations across every single hour.\n\n"
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
                    f"Cocktails & Dinner Reception to follow.\n\n"
                    f"Warm Regards,\n{hosts}\nRSVP: {rsvp_contact}"
                ),
                "whatsapp_copy": (
                    f"Dear Colleague / Friend,\n\n"
                    f"Warm greetings from *{hosts}*.\n\n"
                    f"You and your family are cordially invited to celebrate the *{event_name}* of *{honorees}*.\n\n"
                    f"📅 *Date:* {dates}\n"
                    f"📍 *Venue:* {venue}\n"
                    f"🍽️ *Dinner Reception:* 07:30 PM onwards\n\n"
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

