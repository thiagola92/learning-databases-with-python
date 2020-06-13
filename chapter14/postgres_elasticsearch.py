import psycopg2
import psycopg2.extras

import elasticsearch
from elasticsearch import helpers

from datetime import datetime
from auto_package import AutoPackage

start = datetime.now()

database = psycopg2.connect("postgres://username:password@172.18.0.3/postgres")
cursor = database.cursor()

elasticsearch = Elasticsearch("http://username:password@172.18.0.4:9200")

elasticsearch_client.indices.create('elastic_destiny')

def send(package):
  action = [i for i in package]
  helpers.bulk(elasticsearch_client, action)

auto_package = AutoPackage(send=send, size=1000)

cursor.execute("""SELECT * FROM postgres""")
many = cursor.fetchmany(1000)
i = 0
while many:
  for name, description in many:
    auto_package.add({
      '_index': 'elastic_destiny',
      '_type': 'type',
      '_id': i,
      '_source': {
        'name': name,
        'description': description
      }
    })
    i += 1
  many = cursor.fetchmany(1000)
  
auto_package.send_package()

print(elasticsearch_client.count(index='elastic', doc_type='type'))

elasticsearch_client.indices.delete('elastic_destiny')

cursor.close()
database.close()

print(datetime.now() - start)