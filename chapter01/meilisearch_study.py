# pip install meilisearch
from meilisearch import Client

# Connect to database
client = Client("http://127.0.0.1:7700", "password")

# Create index
client.create_index('index_name')

# Insert information
client.index('index_name').add_documents([{
  'id': 1,
  'sku': 134218478,
  'name': 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial',
  'description': 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)',
  'category': 'eletroportáteis'
}])

# Query information
p = client.index('index_name').get_document(1)
print(p)

# Destroy index
client.index('index_name').delete()