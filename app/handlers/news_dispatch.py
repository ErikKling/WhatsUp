def send_scheduled_news():
    """
    Sends news to users based on their preferences and schedule.
    """
    from db.users import get_all_users
    from app.services.twilio import send_whatsapp_message

    users = get_all_users()
    for user in users:
        if all([user['topic'], user['days'], user['time']]):
            # Replace this with real news fetching logic
            news_content = f"Today's update on {user['topic']}..."
            send_whatsapp_message(user['phone_number'], news_content)