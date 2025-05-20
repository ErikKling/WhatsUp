from fastapi import FastAPI, Request
from app.services.twilio_service import get_or_create_conversation, add_participant, send_message


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Twilio WhatsApp Bot is running!"}


@app.post("/")
async def webhook(request: Request):
    form = await request.form()
    user_number = form.get("From", "").strip()
    message_text = form.get("Body", "").strip().lower()

    print(f"Received from {user_number}: {message_text}")

    conversation_sid = get_or_create_conversation(user_number)
    add_participant(conversation_sid, user_number)

    if message_text == "hi":
        send_message(conversation_sid, "welcome to WhatsUp")
    else:
        send_message(conversation_sid, f"message received: \"{message_text}\"")

    return {"status": "ok"}
