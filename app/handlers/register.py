def handle_registration(user_number: str, message_text: str):
    """
    Collects and stores initial registration info from the user.
    """
    from db.users import insert_user
    from app.services.twilio import send_whatsapp_message

    if insert_user(user_number, message_text):
        send_whatsapp_message(user_number, "Welcome to WhatsUp! Please tell us your favorite topic.")