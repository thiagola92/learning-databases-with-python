from pymongo import MongoClient

# Connect to database
client = MongoClient("mongodb://username:password@172.18.0.2")
database = client['mongo']
collection = database['produtos']

# Insert information
product = {
    'sku': 134218478,
    'name': 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial',
    'description': 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Com o Robô Aspirador de Pó Fast Clean RB-01 da Mondial, sua casa fica limpa sem que você precise manusear o aparelho. Esse modelo consegue varrer, aspirar e limpar diversos tipos de superfícies ao circular sozinho pelo ambiente. Tudo isso sem danificar paredes ou móveis. Graças aos seus sensores inteligentes, ele consegue desviar de obstáculos e até mesmo evitar possíveis quedas. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)',
    'category': 'eletroportáteis'
}
collection.insert_one(product)

# Query information
for i in collection.find({'sku': 134218478}):
    print(i)

# Destroy table
client.drop_database('mongo')