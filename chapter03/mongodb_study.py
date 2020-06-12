from pymongo import MongoClient

client = MongoClient(host='172.18.0.3', port=27017)
# client = MongoClient("mongodb://172.18.0.2/admin?ssl=false") # Using URI
database = client['mongo']
collection = database['produtos']

product = {
    'sku': 134218478,
    'name': 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial',
    'description': 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Com o Robô Aspirador de Pó Fast Clean RB-01 da Mondial, sua casa fica limpa sem que você precise manusear o aparelho. Esse modelo consegue varrer, aspirar e limpar diversos tipos de superfícies ao circular sozinho pelo ambiente. Tudo isso sem danificar paredes ou móveis. Graças aos seus sensores inteligentes, ele consegue desviar de obstáculos e até mesmo evitar possíveis quedas. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)',
    'category': 'eletroportáteis',
    'price': {
        'normal': 200,
        'promotion': 150
    }
}
collection.insert_one(product)

collection.update_one(
    {'sku': 134218478},
    {'$set': {
        'name': 'super robô',
        'price.normal': 300}
    }
)

for i in collection.find({'sku': 134218478}):
    print(i)

client.drop_database('mongo')