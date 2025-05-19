import os
import requests
from dotenv import load_dotenv

load_dotenv()

class NewsAPI:
    def __init__(self, category):
    
        self.api_key = os.getenv("NEWS_API_KEY")                # Note: Create a ".env" file and add: NEWS_API_KEY=your_api_key
        self.base_url = "https://newsapi.org/v2/top-headlines"
        self.country = "us"
        self.category = category
        self.params = {
            "country": self.country,
            "category": self.category,
            "apiKey": self.api_key
        }

    def get_top_articles(self, limit=3):
        '''Returns the top 3 newest articles.'''

        response = requests.get(self.base_url, params=self.params)
        data = response.json()

        results = []

        for article in data["articles"][:limit]:
            results.append({
                "name": article["source"]["name"],
                "title": article["title"],
                "url": article["url"]})
            
        return results
