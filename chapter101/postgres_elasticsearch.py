import psycopg
import elasticsearch
import psycopg.extras
from datetime import datetime
from elasticsearch import helpers, Elasticsearch

start = datetime.now()

postgres_client = psycopg.connect("postgres://username:password@127.0.0.1")
elasticsearch_client = Elasticsearch("http://username:password@127.0.0.1:9200")

cursor = postgres_client.cursor()

elasticsearch_client.indices.create('index_name')

def send(package):
  action = [i for i in package]
  helpers.bulk(elasticsearch_client, action)

_id = 0

cursor.execute("""SELECT * FROM table_name""")
many = cursor.fetchmany(10000)

while many:
  package = [{
    '_index': 'index_name',
    '_id': (_id := _id + 1),
    '_source': {
      'name': name,
      'description': description
    }
  } for name, description in many]

  helpers.bulk(elasticsearch_client, package, max_retries=10)
  
  many = cursor.fetchmany(1000)

print(elasticsearch_client.count(index='index_name'))

elasticsearch_client.indices.delete('index_name')

cursor.close()
postgres_client.close()

print(datetime.now() - start)