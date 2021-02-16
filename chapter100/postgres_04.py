import psycopg2
import psycopg2.extras

from datetime import datetime
from threading import Thread

start = datetime.now()

client = psycopg2.connect("postgres://username:password@127.0.0.1")
cursor = client.cursor()

cursor.execute("""
  CREATE TABLE table_name(
    name text,
    description text
  )
""")

package = []
insert_sql = """
  INSERT INTO table_name
    VALUES(%s, %s)
"""

with open('utils/trash.csv') as file:
  for line in file.readlines():
    name, description = line.split(',')
    
    package.append((name, description))

    if len(package) >= 10000:
      t1 = Thread(target=psycopg2.extras.execute_batch, args=(cursor, insert_sql, package[:2500]), kwargs={'page_size': len(package[:2500])})
      t2 = Thread(target=psycopg2.extras.execute_batch, args=(cursor, insert_sql, package[2500:5000]), kwargs={'page_size': len(package[2500:5000])})
      t3 = Thread(target=psycopg2.extras.execute_batch, args=(cursor, insert_sql, package[5000:7500]), kwargs={'page_size': len(package[5000:7500])})
      t4 = Thread(target=psycopg2.extras.execute_batch, args=(cursor, insert_sql, package[7500:]), kwargs={'page_size': len(package[7500:])})

      t1.start()
      t2.start()
      t3.start()
      t4.start()

      t1.join()
      t2.join()
      t3.join()
      t4.join()

      client.commit()
      package.clear()

if package:
  psycopg2.extras.execute_batch(cursor, insert_sql, package, page_size=len(package))
  client.commit()

cursor.execute("""SELECT COUNT(*) FROM table_name""")
print(cursor.fetchone())

cursor.execute("""DROP TABLE table_name""")

cursor.close()
client.commit()
client.close()

print(datetime.now() - start)