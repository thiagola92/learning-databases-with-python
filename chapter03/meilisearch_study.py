from meilisearch import Client

client = Client("http://127.0.0.1:7700", "password")

client.create_index('index_name')

client.index('index_name').update_documents([{
  'id': 1,
  'sku': 134218478,
  'name': 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial',
  'description': 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)',
  'category': 'eletroportáteis'
}])

# Upsert information
#
# It's already the default behaviour
client.index('index_name').update_documents([{
    'id': 1,
    'name': 'super robô'
}])

p = client.index('index_name').get_document(1)
print(p)

client.index('index_name').delete()