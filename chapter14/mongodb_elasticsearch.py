import pymongo

import elasticsearch
from elasticsearch import helpers

from datetime import datetime
from auto_package import AutoPackage

start = datetime.now()

client = MongoClient("mongodb://username:password@172.18.0.2")
mongo_database = mongo_client['mongo']
mongo_collection = mongo_database['collection']

elasticsearch = Elasticsearch("http://username:password@172.18.0.4:9200")

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
  
auto_package.send_package()

print(elasticsearch_client.count(index='elastic', doc_type='type'))

elasticsearch_client.indices.delete('elastic_destiny')

print(datetime.now() - start)