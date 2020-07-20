from pymongo import MongoClient
from datetime import datetime

start = datetime.now()

client = MongoClient("mongodb://username:password@127.0.0.1")
database = client['database_name']
collection = database['collection_name']

package = []

with open('utils/trash.csv') as file:
  for line in file.readlines():
    name, description = line.split(',')

    package.append({
      'name': name,
      'description': description
    })

    if len(package) >= 10000:
      collection.insert_many(package)
      package.clear()

if package:
  collection.insert_many(package)

print(collection.count_documents({}))

collection.drop()
client.drop_database('mongo')

print(datetime.now() - start)