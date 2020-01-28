import elasticsearch

from datetime import datetime
from auto_package import AutoPackage
from elasticsearch import helpers

start = datetime.now()

elasticsearch_client = elasticsearch.Elasticsearch([{'host': '172.20.0.2', 'port': 9200}, {'host': '172.20.0.2', 'port': 9300}])

elasticsearch_client.indices.create('elastic')

def send(package):
  action = [i for i in package]
  helpers.bulk(elasticsearch_client, action)

auto_package = AutoPackage(send=send, size=1000)

with open('trash.csv') as file:
  for line in file.readlines():
    name, description = line.split(',')
    auto_package.add({
      'name': name,
      'description': description
    })

p = elasticsearch_client.get_alias('*')
print(p)

elasticsearch_client.indices.delete('elastic')

print(datetime.now() - start)