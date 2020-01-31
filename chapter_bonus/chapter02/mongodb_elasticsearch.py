import pymongo

import elasticsearch
from elasticsearch import helpers

from datetime import datetime
from auto_package import AutoPackage

start = datetime.now()

mongo_client = pymongo.MongoClient(host='172.19.0.2', port=27017)
mongo_database = mongo_client['mongo']
mongo_collection = mongo_database['collection']

elasticsearch_client = elasticsearch.Elasticsearch([{'host': '172.20.0.2', 'port': 9200}, {'host': '172.20.0.2', 'port': 9300}])

elasticsearch_client.indices.create('elastic_destiny')

def send(package):
  action = [i for i in package]
  helpers.bulk(elasticsearch_client, action)

auto_package = AutoPackage(send=send, size=1000)

i = 0
for item in mongo_collection.find({}):
  auto_package.add({
    '_index': 'elastic_destiny',
    '_type': 'type',
    '_id': i,
    '_source': {
      'name': item['name'],
      'description': item['description']
    }
  })
  i += 1

p = elasticsearch_client.get(index='elastic_destiny', doc_type='type', id=1)
print(p)

elasticsearch_client.indices.delete('elastic_destiny')

print(datetime.now() - start)