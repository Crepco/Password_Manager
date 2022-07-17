import sqlite3

def init_database(): # function for initializing database
    with sqlite3.connect("password_tijori.db") as db:
        cursor = db.cursor() # create cursor
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS master(
            id INTEGER PRIMARY KEY,
            password TEXT NOT NULL);
            """) # create master table

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS vault(
            id INTEGER PRIMARY KEY,
            platform TEXT NOT NULL,
            userid TEXT NOT NULL,
            password TEXT NOT NULL);
            """) # create vault table
    return db, cursor # return database and cursor