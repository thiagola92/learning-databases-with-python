import psycopg
import psycopg.extras
from pymongo import MongoClient
from datetime import datetime

start = datetime.now()

postgres_client = psycopg.connect("postgres://username:password@127.0.0.1")
mongo_client = MongoClient("mongodb://username:password@127.0.0.1")

cursor = postgres_client.cursor()

database = mongo_client['database_name']
collection = database['collection_name']

cursor.execute("""SELECT * FROM table_name""")
many = cursor.fetchmany(10000)

while many:
  package = [{
    'name': name,
    'description': description
  } for name, description in many]

  collection.insert_many(package)

  many = cursor.fetchmany(10000)

print(collection.count_documents({}))

collection.drop()
mongo_client.drop_database('database_name')

cursor.close()
postgres_client.close()

print(datetime.now() - start)