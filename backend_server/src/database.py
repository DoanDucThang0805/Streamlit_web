import sqlite3

DB_NAME = "/backend/Models/members.db"

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT,
            birthdate TEXT,
            hometown TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("Suscess create database")

create_table()
