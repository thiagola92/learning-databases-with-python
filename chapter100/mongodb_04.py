import time
from pymongo import MongoClient
from datetime import datetime
from threading import Thread, Lock

start = datetime.now()

client = MongoClient("mongodb://username:password@127.0.0.1")
database = client['database_name']
collection = database['collection_name']

threads_count = 0
lock = Lock()
package = []

def send(p):
  global threads_count

  lock.acquire()
  threads_count += 1
  lock.release()

  collection.insert_many(p)

  lock.acquire()
  threads_count -= 1
  lock.release()

with open('utils/trash.csv') as file:
  for line in file.readlines():
    name, description = line.split(',')

    package.append({
      'name': name,
      'description': description
    })

    if len(package) >= 10000:
      while threads_count >= 4: time.sleep(0)
      Thread(target=send, args=(package[:],), daemon=True).start()
      package.clear()

if package:
  collection.insert_many(package)

while threads_count != 0:
  pass

print(collection.count_documents({}))

collection.drop()
client.drop_database('mongo')

print(datetime.now() - start)