# WhatsUp
```text
    whatsapp-news-bot/
    │
    ├── app/                      # main logic
    │   ├── main.py               # Start point
    │   ├── routes.py             # Twilio Webhook entries and other endpoint
    │   ├── handlers/             # Messages handler
    │   │   ├── message_router.py     # Deciding what to do with user input
    │   │   ├── register.py           # Logic Registration
    │   │   ├── preferences.py        # Select category, time, and frequency
    │   │   └── news_dispatch.py      # Sending news at the right time
    │   └── services/
    │       ├── twilio.py         # Send WhatsApp message
    │       ├── news_api.py       # Calling the News API and filtering news
    │       └─
    │
    ├── models/
    │   ├── user.py               # User model and preferences
    │   └─
    │
    ├── db/
    │   ├── database.py           # Connecting to SQLite or Postgres
    │   └── schema.sql            # Table creation script (optional)
    │
    ├── tests/
    │   ├── test_register.py
    │   ├── test_news_api.py
    │   └── ...
    │
    ├── scripts/
    │   └── scheduler.py          # Implementing scheduled news sending
    │
    ├── .env                      # Tokens (Twilio, NewsAPI, Gemini)
    ├── .gitignore
    ├── requirements.txt
    └── README.md
    

```

