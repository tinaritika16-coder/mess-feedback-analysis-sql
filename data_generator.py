# Generates synthetic mess feedback and stores in SQLite
import sqlite3
import random

def generate_data(n=300, db_name="mess_feedback.db"):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS mess_feedback (
            Food_Quality TEXT,
            Cleanliness TEXT,
            Menu_Variety TEXT,
            Waiting_Time_Rating TEXT,
            Staff_Behavior TEXT,
            Overall_Satisfaction TEXT
        )
    """)

    for _ in range(n):
        row = (
            random.choice(["Poor", "Average", "Good"]),
            random.choice(["Poor", "Average", "Good"]),
            random.choice(["Poor", "Average", "Good"]),
            random.choice(["Long", "Medium", "Short"]),
            random.choice(["Bad", "Okay", "Good"]),
            random.choice(["Satisfied", "Not Satisfied"])
        )
        cur.execute("INSERT INTO mess_feedback VALUES (?, ?, ?, ?, ?, ?)", row)

    conn.commit()
    conn.close()
    print("Data inserted into SQL database!")

generate_data()
