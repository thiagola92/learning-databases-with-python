from datetime import datetime
from threading import Thread
from elasticsearch import helpers, Elasticsearch

start = datetime.now()

client = Elasticsearch("http://username:password@127.0.0.1:9200")

client.indices.create('index_name')

package = []
_id = 0

with open('utils/trash.csv') as file:
  for line in file.readlines():
    name, description = line.split(',')

    package.append({
      '_index': 'index_name',
      '_id': (_id := _id + 1),
      '_source': {
        'name': name,
        'description': description
      }
    })

    if len(package) >= 10000:
      t1 = Thread(target=helpers.bulk, args=(client, package[:2500]), kwargs={'max_retries': 10})
      t2 = Thread(target=helpers.bulk, args=(client, package[2500:5000]), kwargs={'max_retries': 10})
      t3 = Thread(target=helpers.bulk, args=(client, package[5000:7500]), kwargs={'max_retries': 10})
      t4 = Thread(target=helpers.bulk, args=(client, package[7500:]), kwargs={'max_retries': 10})

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
  helpers.bulk(client, package, max_retries=10)

print(client.count(index='index_name'))

client.indices.delete('index_name')

print(datetime.now() - start)