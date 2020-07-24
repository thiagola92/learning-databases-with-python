from elasticsearch import Elasticsearch

client = Elasticsearch("http://username:password@127.0.0.1:9200")

client.indices.create('index_name')

client.update(index='index_name', id=1, body={
  'doc': {
    'sku': 134218478,
    'name': 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial',
    'description': 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)',
    'category': 'eletroportáteis'
  },
  'doc_as_upsert': True
})

client.update(index='index_name', id=1, body={
  'doc': {
    'name': 'Rb-01 - Robô Aspirador De Pó SUPER Fast Clean Bivolt - Mondial'
  },
  'doc_as_upsert': True
})

# alternative
client.update(index='index_name', id=1, body={
  'script': {
      'source': "ctx._source.name = 'super robô'"
  },
  'upsert': {}
})

p = client.get(index='index_name', id=1)
print(p)

client.indices.delete('index_name')