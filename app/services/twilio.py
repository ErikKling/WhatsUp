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

_seen_messages = set()


def send_whatsapp_message(user_number: str, message: str):
    conv = get_or_create_conversation(user_number)
    client.conversations.v1.services(CHAT_SERVICE_ID).conversations(conv).messages.create(
        author="system", body=message)


def get_or_create_conversation(user_number: str):
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
    while True:
        conversations = client.conversations.v1.services(CHAT_SERVICE_ID).conversations.list()
        now = datetime.now(timezone.utc)

        for conv in conversations:
            messages = client.conversations.v1.services(CHAT_SERVICE_ID).conversations(conv.sid).messages.list()
            for msg in messages:
                key = f"{conv.sid}-{msg.index}"
                if key not in _seen_messages and msg.author != "system":
                    if msg.date_created and msg.date_created > now - timedelta(seconds=5):
                        _seen_messages.add(key)
                        print(_seen_messages)
                        callback(msg.author, msg.body)
        time.sleep(3)