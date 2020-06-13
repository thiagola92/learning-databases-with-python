import pymongo

import psycopg2
import psycopg2.extras

from datetime import datetime
from auto_package import AutoPackage

start = datetime.now()

client = MongoClient("mongodb://username:password@172.18.0.2")
mongo_database = mongo_client['mongo']
mongo_collection = mongo_database['collection']

database = psycopg2.connect("postgres://username:password@172.18.0.3/postgres")
cursor = database.cursor()

sql = """CREATE TABLE postgres_destiny(
    name text,
    description text
)"""
cursor.execute(sql)

def send(package):
  sql = """INSERT INTO postgres_destiny
      VALUES(%s, %s
  )"""

  psycopg2.extras.execute_batch(cursor, sql, package, page_size=len(package))

auto_package = AutoPackage(send=send, size=1000)

for item in mongo_collection.find({}):
  auto_package.add((item['name'], item['description']))
  
auto_package.send_package()

sql = """SELECT COUNT(*) FROM postgres"""
cursor.execute(sql)
print(cursor.fetchone())

sql = """DROP TABLE postgres_destiny"""
cursor.execute(sql)

cursor.close()
database.commit()
database.close()

print(datetime.now() - start)