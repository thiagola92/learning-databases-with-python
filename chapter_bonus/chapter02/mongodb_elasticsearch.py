import pymongo

import psycopg2
import psycopg2.extras

from datetime import datetime
from auto_package import AutoPackage

start = datetime.now()

mongo_client = pymongo.MongoClient(host='172.19.0.2', port=27017)
mongo_database = mongo_client['mongo']
mongo_collection = mongo_database['collection']

def send(package):
  pass

auto_package = AutoPackage(send=send, size=1000)

for i in mongo_collection.find({}):
  auto_package.add((i['name'], i['description']))

print(datetime.now() - start)