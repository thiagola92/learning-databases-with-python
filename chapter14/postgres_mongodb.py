import psycopg2
import psycopg2.extras

import pymongo

from datetime import datetime
from auto_package import AutoPackage

start = datetime.now()

database = psycopg2.connect("postgres://username:password@172.18.0.3/postgres")
cursor = database.cursor()

client = MongoClient("mongodb://username:password@172.18.0.2")
mongo_database = mongo_client['mongo_destiny']
mongo_collection = mongo_database['collection']

def send(package):
  mongo_collection.insert_many(package)

auto_package = AutoPackage(send=send, size=1000)

cursor.execute("""SELECT * FROM postgres""")
many = cursor.fetchmany(1000)
while many:
  for name, description in many:
    auto_package.add({
      'name': name,
      'description': description
    })
  many = cursor.fetchmany(1000)
  
auto_package.send_package()

print(mongo_collection.count_documents({}))

mongo_collection.drop()
mongo_client.drop_database('mongo_destiny')

cursor.close()
database.close()

print(datetime.now() - start)