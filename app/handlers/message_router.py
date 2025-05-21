def route_message(user_number: str, message_text: str):
    """  Routes incoming messages to appropriate handler based on user registration status. """
    from db.users import get_user_by_number
    from app.handlers.register import handle_registration
    from app.handlers.preferences import handle_preferences

    user = get_user_by_number(user_number)

    if not user:
        handle_registration(user_number, message_text)
    else:
        handle_preferences(user_number, message_text, user)