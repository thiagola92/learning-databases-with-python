from pymongo import MongoClient

client = MongoClient("mongodb://username:password@127.0.0.1")
database = client['database_name']
collection = database['collection_name']

collection.update_one(
    {'sku': 134218478},
    {
        '$set': {
            'sku': 134218478,
            'name': 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial',
            'description': 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)',
            'category': 'eletroportáteis'
        }
    },
    upsert=True
)

collection.update_one(
    {'sku': 134218478},
    {
        '$set': {
            'name': 'Rb-01 - Robô Aspirador De Pó SUPER Fast Clean Bivolt - Mondial'
        }
    },
    upsert=True
)

for i in collection.find({'sku': 134218478}):
    print(i)

client.drop_database('database_name')