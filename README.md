# WhatsUp
```text
    whatsapp-news-bot/
    │
    ├── app/                      # main logic
    │   ├── main.py               # Start point
    │   ├── handlers/             # Messages handler
    │   │   ├── message_router.py     # Deciding what to do with user input
    │   │   ├── register.py           # Logic Registration
    │   │   ├── preferences.py        # Select category, time, and frequency
    │   │   └── news_dispatch.py      # Sending news at the right time
    │   └── services/
    │       ├── twilio.py         # Send WhatsApp message
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

