import pymongo

from datetime import datetime
from auto_package import AutoPackage

start = datetime.now()

mongo_client = pymongo.MongoClient(host='172.19.0.2', port=27017)
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

print(mongo_collection.find({}).count())

mongo_client.drop_database('mongo')

print(datetime.now() - start)