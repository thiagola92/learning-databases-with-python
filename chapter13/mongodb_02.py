import pymongo

from datetime import datetime
from auto_package import AutoPackage

start = datetime.now()

client = MongoClient("mongodb://username:password@172.18.0.2")
mongo_database = mongo_client['mongo']
mongo_collection = mongo_database['collection']

def send(package):
  mongo_collection.insert_many(package)

auto_package = AutoPackage(send=send, size=1000)

with open('trash.csv') as file:
  for line in file.readlines():
    name, description = line.split(',')
    auto_package.add({
      'name': name,
      'description': description
    })

print(mongo_collection.count_documents({}))

mongo_collection.drop()
mongo_client.drop_database('mongo')

print(datetime.now() - start)