import pymongo

from datetime import datetime

start = datetime.now()

client = MongoClient("mongodb://username:password@172.18.0.2")
mongo_database = mongo_client['mongo']
mongo_collection = mongo_database['collection']

with open('trash.csv') as file:
  for line in file.readlines():
    name, description = line.split(',')
    mongo_collection.insert_one({
      'name': name,
      'description': description
    })

print(mongo_collection.count_documents({}))

mongo_collection.drop()
mongo_client.drop_database('mongo')

print(datetime.now() - start)