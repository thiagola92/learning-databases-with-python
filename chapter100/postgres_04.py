import psycopg2
import psycopg2.extras

from datetime import datetime
from threading import Thread, Lock

start = datetime.now()

client = psycopg2.connect("postgres://username:password@127.0.0.1")
cursor = client.cursor()

cursor.execute("""
  CREATE TABLE table_name(
    name text,
    description text
  )
""")

threads_count = 0
lock = Lock()
package = []
insert_sql = """
  INSERT INTO table_name
    VALUES(%s, %s)
"""

def send(p):
  global threads_count

  with lock:
    threads_count += 1

  psycopg2.extras.execute_batch(cursor, insert_sql, p, page_size=len(p))
  client.commit()

  with lock:
    threads_count -= 1

with open('utils/trash.csv') as file:
  for line in file.readlines():
    name, description = line.split(',')
    
    package.append((name, description))

    if len(package) >= 10000:
      while threads_count >= 4: pass
      Thread(target=send, args=(package[:],), daemon=True).start()
      package.clear()

if package:
  psycopg2.extras.execute_batch(cursor, insert_sql, package, page_size=len(package))
  client.commit()

while threads_count != 0:
  pass

cursor.execute("""SELECT COUNT(*) FROM table_name""")
print(cursor.fetchone())

cursor.execute("""DROP TABLE table_name""")

cursor.close()
client.commit()
client.close()

print(datetime.now() - start)