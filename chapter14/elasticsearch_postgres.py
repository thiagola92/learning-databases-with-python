import elasticsearch

import psycopg2
import psycopg2.extras

from datetime import datetime
from auto_package import AutoPackage

start = datetime.now()

elasticsearch = Elasticsearch("http://username:password@172.18.0.4:9200")

database = psycopg2.connect("postgres://username:password@172.18.0.3/postgres")
cursor = database.cursor()

sql = """CREATE TABLE postgres_destiny(
    name text,
    description text
)"""
cursor.execute(sql)

def send(package):
  sql = """INSERT INTO postgres_destiny
      VALUES(%s, %s
  )"""

  psycopg2.extras.execute_batch(cursor, sql, package, page_size=len(package))

auto_package = AutoPackage(send=send, size=1000)

response = elasticsearch_client.search(
  index='elastic',
  doc_type='type',
  body= {
    'query': {
      'match_all': {}
    },
    'size': 1000
  },
  scroll='10m'
)

while len(response['hits']['hits']) > 0:
  for item in response['hits']['hits']:
    auto_package.add((item['_source']['name'], item['_source']['description']))
  
  response = elasticsearch_client.scroll(scroll_id=response['_scroll_id'], scroll='10m')
  
auto_package.send_package()

sql = """SELECT COUNT(*) FROM postgres"""
cursor.execute(sql)
print(cursor.fetchone())

sql = """DROP TABLE postgres_destiny"""
cursor.execute(sql)

cursor.close()
database.commit()
database.close()

print(datetime.now() - start)