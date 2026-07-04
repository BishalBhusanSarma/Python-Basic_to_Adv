import sqlite3

connect = sqlite3.connect("test.db",check_same_thread=False)
cursor = connect.cursor()

def est_conn():
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS task(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT,
                    status BOOLEAN)


                """)
    connect.commit()

def fetchall():
    all_t = cursor.execute("""
    SELECT * FROM task
    """)
    return (all_t.fetchall())