# pip install pymongo
from pymongo import MongoClient

# Connect to database
#
# NOTICE: Databases and Collections are only created
# when the first document is inserted
client = MongoClient("mongodb://username:password@127.0.0.1")
database = client["database_name"]
collection = database["collection_name"]

# Insert information
collection.insert_one(
    {
        "sku": 134218478,
        "name": "Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial",
        "description": "Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)",
        "category": "eletroportáteis",
    }
)

# Query information
for doc in collection.find({"sku": 134218478}):
    print(doc)

# Destroy table
client.drop_database("database_name")
