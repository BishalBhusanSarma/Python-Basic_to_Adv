import psycopg2

hostname = "localhost"
database = "students"
username = "postgres"
pw = "1234"
port = 5432
conn = None
cur = None


conn = psycopg2.connect(host = hostname,
                                dbname = database,
                                user = username,
                                password = pw,
                                port = port)

cur = conn.cursor()


table = cur.execute('''CREATE TABLE IF NOT EXISTS notes (
                            id SERIAL PRIMARY KEY,
                            task TEXT NOT NULL,
                            description TEXT NOT NULL)''')

conn.commit()

# insert_script = 'INSERT INTO notes (task, description) VALUES(%s,%s)'
# insert_values = [
#     ("python","need to learn python"),
#     ("java","i hate java"),
#     ("c","Its okay to learn C"),
#     ("cpp","idk man")
# ]


# for listt in insert_values:
#     cur.execute(insert_script, listt)
conn.commit()


