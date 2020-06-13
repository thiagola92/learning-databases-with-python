import elasticsearch

from datetime import datetime

start = datetime.now()

elasticsearch = Elasticsearch("http://username:password@172.18.0.4:9200")

elasticsearch_client.indices.create('elastic')

with open('trash.csv') as file:
  i = 0
  for line in file.readlines():
    name, description = line.split(',')
    elasticsearch_client.create(index='elastic', doc_type='type', id=i, body={
      'name': name,
      'description': description
    })
    i += 1

print(elasticsearch_client.count(index='elastic', doc_type='type'))

elasticsearch_client.indices.delete('elastic')

print(datetime.now() - start)