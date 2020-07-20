from pymongo import MongoClient

client = MongoClient("mongodb://username:password@127.0.0.1")
database = client['database_name']
collection = database['collection_name']

collection.insert_one({
    'sku': 134218478,
    'name': 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial',
    'description': 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Com o Robô Aspirador de Pó Fast Clean RB-01 da Mondial, sua casa fica limpa sem que você precise manusear o aparelho. Esse modelo consegue varrer, aspirar e limpar diversos tipos de superfícies ao circular sozinho pelo ambiente. Tudo isso sem danificar paredes ou móveis. Graças aos seus sensores inteligentes, ele consegue desviar de obstáculos e até mesmo evitar possíveis quedas. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)',
    'category': 'eletroportáteis'
})