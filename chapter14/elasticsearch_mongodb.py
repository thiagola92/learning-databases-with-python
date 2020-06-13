import elasticsearch

import pymongo

from datetime import datetime
from auto_package import AutoPackage

start = datetime.now()

elasticsearch = Elasticsearch("http://username:password@172.18.0.4:9200")

client = MongoClient("mongodb://username:password@172.18.0.2")
mongo_database = mongo_client['mongo_destiny']
mongo_collection = mongo_database['collection']

def send(package):
  mongo_collection.insert_many(package)

auto_package = AutoPackage(send=send, size=1000)

response = elasticsearch_client.search(
  index='elastic',
  doc_type='type',
  body= {
    'query': {
      'match_all': {}
    },
    'size': 1000
  },
  scroll='10m'
)

while len(response['hits']['hits']) > 0:
  for item in response['hits']['hits']:
    auto_package.add({
      'name': item['_source']['name'],
      'description': item['_source']['description']
    })
  
  response = elasticsearch_client.scroll(scroll_id=response['_scroll_id'], scroll='10m')
  
auto_package.send_package()

print(mongo_collection.count_documents({}))

mongo_collection.drop()
mongo_client.drop_database('mongo_destiny')

print(datetime.now() - start)