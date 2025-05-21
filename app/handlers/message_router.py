from app.services.twilio import send_whatsapp_message
from app.services.news_api import NewsAPI

category_map = {
    "1": "sports",
    "2": "business",
    "3": "entertainment",
    "4": "general",
    "5": "health",
    "6": "science",
    "7": "technology"
}

user_states = {} #global user status

def route_message(user_number: str, message_text: str):

    text = message_text.strip().lower()

    
    if text == "thanks": #thanks to reset
        send_whatsapp_message(user_number, "You’re welcome! Send a new message to start again.")
        user_states.pop(user_number, None)
        return

    # If user is not registered – start new conversation
    if user_number not in user_states:
        user_states[user_number] = "awaiting_category"
        send_whatsapp_message(user_number, "Please choose a category:\n1. sports\n2. business\n3. entertainment\n4. general\n5. health\n6. science\n7. technology")
        return

    # User sent a category
    if user_states[user_number] == "awaiting_category":
        if text in category_map:
            category = category_map[text]
            articles = NewsAPI(category).get_top_articles()

            if not articles:
                send_whatsapp_message(user_number, "Sorry, no articles found. Please choose another number.")
                return

            response = ""
            for i, article in enumerate(articles, start=1):
                response += f"{i}. {article['title']}\n{article['url']}\n\n"

            send_whatsapp_message(user_number, response.strip())
            send_whatsapp_message(user_number, "Want more? Send a new message or type ‘Thanks’.")
            user_states.pop(user_number)  # Reset status
        else:
            send_whatsapp_message(user_number, "Invalid choice. Please send a number between 1 and 7.")