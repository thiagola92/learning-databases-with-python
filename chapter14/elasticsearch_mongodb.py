from pymongo import MongoClient
from datetime import datetime
from elasticsearch import Elasticsearch

start = datetime.now()

elasticsearch_client = Elasticsearch("http://username:password@127.0.0.1:9200")
mongo_client = MongoClient("mongodb://username:password@127.0.0.1")

database = mongo_client['database_name']
collection = database['collection_name']

response = elasticsearch_client.search(
  index='index_name',
  body= {
    'query': {
      'match_all': {}
    },
    'size': 10000
  },
  scroll='10m'
)

while len(response['hits']['hits']) > 0:
  package = [{
      'name': item['_source']['name'],
      'description': item['_source']['description']
  } for item in response['hits']['hits']]

  collection.insert_many(package)
  
  response = elasticsearch_client.scroll(scroll_id=response['_scroll_id'], scroll='10m')

print(collection.count_documents({}))

collection.drop()
mongo_client.drop_database('database_name')

print(datetime.now() - start)