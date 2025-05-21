def handle_preferences(user_number: str, message_text: str, user):
    """
    Updates user preferences for news topics and schedule.
    """
    from db.users import update_preferences, get_preferences, delete_user
    from app.services.twilio import send_whatsapp_message

    current_pref = get_preferences(user_number)

    if not current_pref['topic']:
        update_preferences(user_number, 'topic', message_text)
        send_whatsapp_message(user_number, "What days would you like to receive updates? (e.g., Mon, Wed, Fri)")
    elif not current_pref['days']:
        update_preferences(user_number, 'days', message_text)
        send_whatsapp_message(user_number, "What time would you like to receive news? (e.g., 08:00)")
    elif not current_pref['time']:
        update_preferences(user_number, 'time', message_text)
        send_whatsapp_message(user_number, "Great! You'll start receiving updates at the scheduled times.")
    else:
        message_text = message_text.strip().lower()
        if message_text in ["change", "change preferences"]:
            update_preferences(user_number, 'topic', None)
            update_preferences(user_number, 'days', None)
            update_preferences(user_number, 'time', None)
            send_whatsapp_message(user_number, "Let's update your preferences. What's your new favorite topic?")
        elif message_text in ["unsubscribe", "stop"]:
            delete_user(user_number)
            send_whatsapp_message(user_number, "You've been unsubscribed. Text again if you want to rejoin.")
        else:
            send_whatsapp_message(
                user_number,
                "You're already subscribed. Type 'change' to update preferences or 'unsubscribe' to stop receiving updates."
            )