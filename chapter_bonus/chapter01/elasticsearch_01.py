import elasticsearch

from datetime import datetime

start = datetime.now()

elasticsearch_client = elasticsearch.Elasticsearch([{'host': '172.20.0.2', 'port': 9200}, {'host': '172.20.0.2', 'port': 9300}])

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

p = elasticsearch_client.get(index='elastic', doc_type='type', id='1')
print(p)

elasticsearch_client.indices.delete('elastic')

print(datetime.now() - start)