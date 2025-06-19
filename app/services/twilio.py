import os
import time
from datetime import datetime, timedelta, timezone
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
API_KEY_SID = os.getenv("API_KEY_SID")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
CHAT_SERVICE_ID = os.getenv("CHAT_SERVICE_ID")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

client = Client(API_KEY_SID, API_KEY_SECRET, ACCOUNT_SID)

# Messages history
_seen_messages = set()


def send_whatsapp_message(user_number: str, message: str):
    """ It sends messsage to users. """
    conv = get_or_create_conversation(user_number)
    client.conversations.v1.services(CHAT_SERVICE_ID).conversations(conv).messages.create(
        author="system", body=message)


def get_or_create_conversation(user_number: str):
    """
    It gets all conversations and participant and
    :param user_number: user's whatsapp number
    :return: conversation sid
    """

    conversations = client.conversations.v1.services(CHAT_SERVICE_ID).conversations.list()
    for conv in conversations:
        participants = client.conversations.v1.services(CHAT_SERVICE_ID).conversations(conv.sid).participants.list()
        for p in participants:
            if p.messaging_binding and p.messaging_binding.get("address") == user_number:
                return conv.sid

    conv = client.conversations.v1.services(CHAT_SERVICE_ID).conversations.create(
        friendly_name=f"chat_with_{user_number}")
    conv_sid = conv.sid

    client.conversations.v1.services(CHAT_SERVICE_ID).conversations(conv_sid).participants.create(
        messaging_binding_address=user_number,
        messaging_binding_proxy_address=TWILIO_WHATSAPP_NUMBER)

    return conv_sid


def poll_messages(callback):
    """
    As soon as it receives new messages, Creates a unique key for each message, and it
    records them in a set called _seen_messages.it always checks that the messages sent
    by the bot itself and the messages from users are not stored duplicated due to the continuous loop.
    :param callback: a function
    """
    #  Ignore all existing messages
    conversations = client.conversations.v1.services(CHAT_SERVICE_ID).conversations.list()
    for conv in conversations:
        messages = client.conversations.v1.services(CHAT_SERVICE_ID).conversations(conv.sid).messages.list(limit=10)
        for msg in messages:
            _seen_messages.add(msg.sid)

    while True:
        conversations = client.conversations.v1.services(CHAT_SERVICE_ID).conversations.list()
        now = datetime.now(timezone.utc)

        for conv in conversations:
            messages = client.conversations.v1.services(CHAT_SERVICE_ID).conversations(conv.sid).messages.list(order='desc')
            for msg in messages:
                if msg.date_created and msg.date_created > now - timedelta(seconds=30):
                    key = msg.sid
                    if key not in _seen_messages:
                        _seen_messages.add(key)
                        if msg.author == "system" or msg.author == TWILIO_WHATSAPP_NUMBER:
                            continue
                        print(f"New message detected: {msg.body}")
                        callback(msg.author, msg.body)
        time.sleep(0.5)