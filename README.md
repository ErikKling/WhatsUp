# 📲 WhatsUpp News Bot

A smart, interactive news delivery bot for WhatsApp, built using Twilio Conversations API and FastAPI.  
It registers users, collects their preferences, and sends them tailored news updates on a recurring schedule.

---

## 🚀 Features

- ⌛ **User Registration**: Greets new users and stores their name and preferences.
- ✅ **Topic Preferences**: Lets users select favorite topics, delivery days, and times.
- ⌛ **Smart Conversations**: Handles follow-up messages and user state transitions.
- ⌛ **News Delivery Scheduler**: Sends periodic messages based on preferences (polling-based).
- ✅ **Settings Management**: Users can update preferences or unsubscribe via conversation.
- ✅ **Data Persistence**: SQLite-powered lightweight database.
- ✅ **Modular Codebase**: Clean architecture with separation of concerns.

---

## 🏗️ Project Structure

```text
whatsapp-news-bot/
│
├── app/
│   ├── main.py                   # Entry point (starts polling)
│   ├── handlers/
│   │   ├── message_router.py     # Message routing logic
│   │   ├── register.py           # User registration flow
│   │   ├── preferences.py        # Collecting preferences
│   │   └── news_dispatch.py      # Scheduled news delivery logic
│   └── services/
│       └── twilio.py             # Twilio WhatsApp integration
│
├── db/
│   ├── database.py               # SQLite operations
│   └── users.db                  # User database (auto-created)
│
├── scripts/
│   └── scheduler.py              # Cron-like runner for news delivery
│
├── .env                          # Twilio credentials and config
├── requirements.txt              # Python dependencies
├── .gitignore
└── README.md                     # You're here!
```
## 🛠️ Setup Instructions

1. Clone the repo
```bash
    git clone https://github.com/your-username/whatsapp-news-bot.git
    cd whatsapp-news-bot
```
2. Create a virtual environment
```bash
    python -m venv .venv
    source .venv/bin/activate      # or .venv\Scripts\activate on Windows
```
3. Install dependencies
```bash
    pip install -r requirements.txt
```
4. Configure environment variables
Create a .env file:
```env
    ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    API_KEY_SID=SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    API_KEY_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    CHAT_SERVICE_ID=ISxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    TWILIO_WHATSAPP_NUMBER=whatsapp:+1234567890
```
5. Run the bot
```bash
    python app/main.py 
```

---

## 💡 How It Works
- When a new user sends a message, the bot:
- Registers them
- Asks for topic, delivery day(s), and time
- All preferences are stored in a SQLite database.
- Messages are sent using Twilio’s Conversations API and polling-based logic.

---

## 🔐 Security
- Uses .env to store credentials
- Avoids using Twilio Auth Token directly
- Handles duplicate users gracefully

---

## 📅 TODO / Ideas

- 🔄 Migrate to webhook-based architecture
- 🌍 Add multi-language support
- 🧠 Integrate a real news API (e.g., NewsAPI, Gemini, etc.)
- 📊 Admin dashboard to monitor users and preferences

---

## 📜 License

MIT License. See LICENSE for details.

---

## 🤝 Contributors

### ErikKling & ehsanmehrali

Feel free to fork, contribute, and make this better. PRs are welcome!
