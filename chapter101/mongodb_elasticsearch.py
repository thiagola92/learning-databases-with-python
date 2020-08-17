from pymongo import MongoClient
from datetime import datetime
from elasticsearch import helpers, Elasticsearch

start = datetime.now()

mongo_client = MongoClient("mongodb://username:password@127.0.0.1")
elasticsearch_client = Elasticsearch("http://username:password@127.0.0.1:9200")

database = mongo_client['database_name']
collection = database['collection_name']

elasticsearch_client.indices.create('index_name')

package = []
_id = 0

for item in collection.find({}):
  package.append({
    '_index': 'index_name',
    '_id': (_id := _id + 1),
    '_source': {
      'name': item['name'],
      'description': item['description']
    }
  })

  if len(package) >= 10000:
    helpers.bulk(elasticsearch_client, package, max_retries=10)
    package.clear()

if package:
  helpers.bulk(elasticsearch_client, package, max_retries=10)

print(elasticsearch_client.count(index='index_name'))

elasticsearch_client.indices.delete('index_name')

print(datetime.now() - start)