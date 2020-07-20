from pymongo import MongoClient
from datetime import datetime

start = datetime.now()

client = MongoClient("mongodb://username:password@127.0.0.1")
database = client['database_name']
collection = database['collection_name']

with open('utils/trash.csv') as file:
  for line in file.readlines():
    name, description = line.split(',')
    collection.insert_one({
      'name': name,
      'description': description
    })

print(collection.count_documents({}))

collection.drop()
client.drop_database('database_name')

print(datetime.now() - start)