from datetime import datetime
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
      helpers.bulk(client, package, max_retries=10)
      package.clear()

if package:
  helpers.bulk(client, package, max_retries=10)

print(client.count(index='index_name'))

client.indices.delete('index_name')

print(datetime.now() - start)