import psycopg2
import psycopg2.extras

import pymongo

from datetime import datetime
from auto_package import AutoPackage

start = datetime.now()

database = psycopg2.connect(host='127.0.0.1', dbname='postgres', user='postgres', password='postgres')
cursor = database.cursor()

mongo_client = pymongo.MongoClient(host='172.19.0.2', port=27017)
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