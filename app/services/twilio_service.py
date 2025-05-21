import os
import time
from twilio.rest import Client
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
API_KEY_SID = os.getenv("API_KEY_SID")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
CHAT_SERVICE_ID = os.getenv("CHAT_SERVICE_ID")

client = Client(API_KEY_SID, API_KEY_SECRET, ACCOUNT_SID)

# The last index read for each conversion.
last_read_index = {}

def poll_messages():
    conversations = client.conversations.v1.services(CHAT_SERVICE_ID).conversations.list()

    for conv in conversations:
        conv_sid = conv.sid
        messages = client.conversations.v1.services(CHAT_SERVICE_ID).conversations(conv_sid).messages.list(order='asc')

        # Check the latest new messages
        for message in messages:
            if conv_sid not in last_read_index or message.index > last_read_index[conv_sid]:
                print(f"[{message.date_created}] From {message.author}: {message.body}")
                last_read_index[conv_sid] = message.index


def main():
    """ Infinity loop for polling every 2 seconds. """
    print("Polling for new messages... (Press CTRL+C to stop)")
    try:
        while True:
            poll_messages()
            time.sleep(2)  # Check every 5 seconds
    except KeyboardInterrupt:
        print("Stopped polling.")


if __name__ == "__main__":
    main()
