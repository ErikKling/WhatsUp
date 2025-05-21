import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "users.db")

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    phone_number TEXT PRIMARY KEY,
    name TEXT,
    topic TEXT,
    days TEXT,
    time TEXT
)''')
conn.commit()


def insert_user(phone_number: str, name: str):
    try:
        cursor.execute("INSERT INTO users (phone_number, name) VALUES (?, ?)", (phone_number, name))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def update_preferences(phone_number: str, field: str, value):
    cursor.execute(f"UPDATE users SET {field} = ? WHERE phone_number = ?", (value, phone_number))
    conn.commit()


def get_user_by_number(phone_number: str):
    cursor.execute("SELECT * FROM users WHERE phone_number = ?", (phone_number,))
    return cursor.fetchone()


def get_preferences(phone_number: str):
    cursor.execute("SELECT topic, days, time FROM users WHERE phone_number = ?", (phone_number,))
    row = cursor.fetchone()
    return {"topic": row[0], "days": row[1], "time": row[2]} if row else {}


def delete_user(phone_number: str):
    cursor.execute("DELETE FROM users WHERE phone_number = ?", (phone_number,))
    conn.commit()


def get_all_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    return [
        {"phone_number": r[0], "name": r[1], "topic": r[2], "days": r[3], "time": r[4]}
        for r in rows
    ]