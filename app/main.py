from handlers.message_router import route_message
from services.twilio import poll_messages
from app.services.news_api import NewsAPI

if __name__ == '__main__':
    print("Starting WhatsApp News Bot...")
    poll_messages(route_message)


category_map = {
    "1": "sports",
    "2": "business",
    "3": "entertainment",
    "4": "general",
    "5": "health",
    "6": "science",
    "7": "technology"
}

def build_news_response(user_text):
    if user_text not in category_map:
        return "Ungültige Auswahl. Bitte sende eine Zahl zwischen 1 und 7."

    category = category_map[user_text]
    articles = NewsAPI(category).get_top_articles()

    message = ""
    for i, article in enumerate(articles, start=1):
        message += f"{i}. {article['title']}\n{article['url']}\n\n"

    return message.strip()

print(build_news_response("4"))
