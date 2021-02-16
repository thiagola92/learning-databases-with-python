from pymongo import MongoClient
from datetime import datetime
from threading import Thread 

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
      t1 = Thread(target=collection.insert_many, args=(package[:2500],))
      t2 = Thread(target=collection.insert_many, args=(package[2500:5000],))
      t3 = Thread(target=collection.insert_many, args=(package[5000:7500],))
      t4 = Thread(target=collection.insert_many, args=(package[7500:],))

      t1.start()
      t2.start()
      t3.start()
      t4.start()

      t1.join()
      t2.join()
      t3.join()
      t4.join()

      package.clear()

if package:
  collection.insert_many(package)

print(collection.count_documents({}))

collection.drop()
client.drop_database('mongo')

print(datetime.now() - start)