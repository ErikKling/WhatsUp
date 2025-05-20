import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
API_KEY_SID = os.getenv("API_KEY_SID")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
CHAT_SERVICE_ID = os.getenv("CHAT_SERVICE_ID")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

client = Client(API_KEY_SID, API_KEY_SECRET, ACCOUNT_SID)


def get_or_create_conversation(user_number: str):
    existing_conversations = client.conversations \
        .v1.services(CHAT_SERVICE_ID) \
        .conversations \
        .list(limit=100)

    for conv in existing_conversations:
        participants = client.conversations \
            .v1.services(CHAT_SERVICE_ID) \
            .conversations(conv.sid) \
            .participants \
            .list()
        for p in participants:
            if p.messaging_binding and p.messaging_binding.get("address") == user_number:
                return conv.sid

    # If the previous conversation is not found
    conv = client.conversations \
        .v1.services(CHAT_SERVICE_ID) \
        .conversations \
        .create(friendly_name=f"chat_with_{user_number}")
    return conv.sid


def participant_exists(conversation_sid: str, user_number: str) -> bool:
    participants = client.conversations \
        .v1.services(CHAT_SERVICE_ID) \
        .conversations(conversation_sid) \
        .participants \
        .list()
    for p in participants:
        if p.messaging_binding and p.messaging_binding.get("address") == user_number:
            return True
    return False


def add_participant(conversation_sid: str, user_number: str):
    if not participant_exists(conversation_sid, user_number):
        participant = client.conversations \
            .v1.services(CHAT_SERVICE_ID) \
            .conversations(conversation_sid) \
            .participants \
            .create(
                messaging_binding_address=user_number,
                messaging_binding_proxy_address=TWILIO_WHATSAPP_NUMBER
            )
        print(participant.account_sid)


def send_message(conversation_sid: str , message: str):
    client.conversations \
        .v1.services(CHAT_SERVICE_ID) \
        .conversations(conversation_sid) \
        .messages \
        .create(author="system", body=message)

