import psycopg2
import psycopg2.extras

from datetime import datetime

start = datetime.now()

database = psycopg2.connect("postgres://username:password@127.0.0.1")
cursor = database.cursor()

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
      psycopg2.extras.execute_batch(cursor, insert_sql, package, page_size=len(package))
      package.clear()

if package:
  psycopg2.extras.execute_batch(cursor, insert_sql, package, page_size=len(package))

cursor.execute("""SELECT COUNT(*) FROM table_name""")
print(cursor.fetchone())

cursor.execute("""DROP TABLE table_name""")

cursor.close()
database.commit()
database.close()

print(datetime.now() - start)