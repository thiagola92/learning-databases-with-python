import elasticsearch

import pymongo

from datetime import datetime
from auto_package import AutoPackage

start = datetime.now()

elasticsearch_client = elasticsearch.Elasticsearch([{'host': '172.20.0.2', 'port': 9200}, {'host': '172.20.0.2', 'port': 9300}])

mongo_client = pymongo.MongoClient(host='172.19.0.2', port=27017)
mongo_database = mongo_client['mongo_destiny']
mongo_collection = mongo_database['collection']

def send(package):
  mongo_collection.insert_many(package)

auto_package = AutoPackage(send=send, size=1000)

response = elasticsearch_client.search(index='elastic',
                                      doc_type='type',
                                      body= {
                                        'query': {
                                          'match_all': {}
                                        },
                                        'size': 1000
                                      },
                                      scroll='10m')

while len(response['hits']['hits']) > 0:
  for item in response['hits']['hits']:
    auto_package.add({
      'name': item['_source']['name'],
      'description': item['_source']['description']
    })
  
  response = elasticsearch_client.scroll(scroll_id=response['_scroll_id'], scroll='10m')

for i in mongo_collection.find({}).limit(1):
    print(i)

mongo_client.drop_database('mongo_destiny')

print(datetime.now() - start)