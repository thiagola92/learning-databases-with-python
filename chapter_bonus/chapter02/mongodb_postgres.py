import pymongo

import psycopg2
import psycopg2.extras

from datetime import datetime
from auto_package import AutoPackage

start = datetime.now()

mongo_client = pymongo.MongoClient(host='172.19.0.2', port=27017)
mongo_database = mongo_client['mongo']
mongo_collection = mongo_database['collection']

database = psycopg2.connect(host='127.0.0.1', dbname='postgres', user='postgres', password='postgres')
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

cursor.execute("""SELECT * FROM postgres_destiny LIMIT 1""")
p = cursor.fetchone()
print(p)

sql = """DROP TABLE postgres_destiny"""
cursor.execute(sql)

cursor.close()
database.commit()
database.close()

print(datetime.now() - start)