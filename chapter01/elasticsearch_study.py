from elasticsearch import Elasticsearch

# Connect to database
client = Elasticsearch("http://username:password@127.0.0.1:9200")

# Create index
client.indices.create(index='index_name')

# Insert information
client.create(index='index_name', id=1, document={
  'sku': 134218478,
  'name': 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial',
  'description': 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)',
  'category': 'eletroportáteis'
})

# Query information
p = client.get(index='index_name', id=1)
print(p)

# Destroy index
client.indices.delete(index='index_name')