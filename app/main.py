from app.handlers.message_router import route_message
from app.services.twilio import poll_messages

def main():
    print("Starting WhatsApp News Bot...")
    poll_messages(route_message)

if __name__ == '__main__':
    main()
