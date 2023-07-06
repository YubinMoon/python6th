import psycopg2
from psycopg2 import sql

conn = psycopg2.connect("host=main dbname=library user=user1 password=asdf")
cur = conn.cursor()

# cur.execute(
#     """
# CREATE TABLE test_table (
# id SERIAL PRIMARY KEY,
# name VARCHAR(50))
# """
# )

# conn.commit()

# cur.execute("INSERT INTO test_table (name) VALUES (%s)", ("tset1",))
# cur.execute("INSERT INTO test_table (name) VALUES (%s)", ("test2",))
# conn.commit()

# cur.execute("INSERT INTO test_table (name) VALUES (%s)", ("TEST_NAME",))
# conn.commit()

cur.execute("SHOW ALL;")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
