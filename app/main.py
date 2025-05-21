from app.handlers.message_router import route_message
from app.services.twilio import poll_messages

if __name__ == '__main__':
    print("Starting WhatsApp News Bot...")
    poll_messages(route_message)
