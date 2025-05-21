import time
from app.handlers.news_dispatch import send_scheduled_news

while True:
    send_scheduled_news()
    time.sleep(3600)  # Every hour