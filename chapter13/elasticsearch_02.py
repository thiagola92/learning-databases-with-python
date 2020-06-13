import elasticsearch

from datetime import datetime
from auto_package import AutoPackage
from elasticsearch import helpers

start = datetime.now()

elasticsearch = Elasticsearch("http://username:password@172.18.0.4:9200")

elasticsearch_client.indices.create('elastic')

def send(package):
  action = [i for i in package]
  helpers.bulk(elasticsearch_client, action)

auto_package = AutoPackage(send=send, size=1000)

with open('trash.csv') as file:
  i = 0
  for line in file.readlines():
    name, description = line.split(',')
    auto_package.add({
      '_index': 'elastic',
      '_type': 'type',
      '_id': i,
      '_source': {
        'name': name,
        'description': description
      }
    })
    i += 1

print(elasticsearch_client.count(index='elastic', doc_type='type'))

elasticsearch_client.indices.delete('elastic')

print(datetime.now() - start)