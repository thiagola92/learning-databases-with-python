import psycopg2
import psycopg2.extras
from pymongo import MongoClient
from datetime import datetime

start = datetime.now()

mongo_client = MongoClient("mongodb://username:password@127.0.0.1")
postgres_client = psycopg2.connect("postgres://username:password@127.0.0.1")

cursor = postgres_client.cursor()
database = mongo_client['database_name']
collection = database['collection_name']

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

for item in collection.find({}):
  package.append((item['name'], item['description']))

  if len(package) >= 10000:
    psycopg2.extras.execute_batch(cursor, insert_sql, package, page_size=len(package))
    package.clear()
  
if package:
  psycopg2.extras.execute_batch(cursor, insert_sql, package, page_size=len(package))

cursor.execute("""SELECT COUNT(*) FROM table_name""")
print(cursor.fetchone())

cursor.execute("""DROP TABLE table_name""")

cursor.close()
postgres_client.commit()
postgres_client.close()

print(datetime.now() - start)