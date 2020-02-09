import elasticsearch

import psycopg2
import psycopg2.extras

from datetime import datetime
from auto_package import AutoPackage

start = datetime.now()

elasticsearch_client = elasticsearch.Elasticsearch([{'host': '172.20.0.2', 'port': 9200}, {'host': '172.20.0.2', 'port': 9300}])

database = psycopg2.connect(host='127.0.0.1', dbname='postgres', user='postgres', password='postgres')
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

response = elasticsearch_client.search(index='elastic',
                                      doc_type='type',
                                      body= {
                                        'query': {
                                          'match_all': {}
                                        },
                                        'size': 1000
                                      },
                                      scroll='10m')

while len(response['hits']['hits']) > 0:
  for item in response['hits']['hits']:
    auto_package.add((item['_source']['name'], item['_source']['description']))
  
  response = elasticsearch_client.scroll(scroll_id=response['_scroll_id'], scroll='10m')

cursor.execute("""SELECT * FROM postgres_destiny LIMIT 1""")
p = cursor.fetchone()
print(p)

sql = """DROP TABLE postgres_destiny"""
cursor.execute(sql)

cursor.close()
database.commit()
database.close()

print(datetime.now() - start)