import psycopg2
import psycopg2.extras
from datetime import datetime
from elasticsearch import Elasticsearch

start = datetime.now()

elasticsearch_client = Elasticsearch("http://username:password@127.0.0.1:9200")
postgres_client = psycopg2.connect("postgres://username:password@127.0.0.1")

cursor = postgres_client.cursor()

cursor.execute("""
  CREATE TABLE table_name(
    name text,
    description text
  )
""")

insert_sql = """
  INSERT INTO table_name
      VALUES(%s, %s)
"""

response = elasticsearch_client.search(
  index='index_name',
  body= {
    'query': {
      'match_all': {}
    },
    'size': 10000
  },
  scroll='10m'
)

while len(response['hits']['hits']) > 0:
  package = [(
      item['_source']['name'],
      item['_source']['description']
   ) for item in response['hits']['hits']]

  psycopg2.extras.execute_batch(cursor, insert_sql, package, page_size=len(package))
  
  response = elasticsearch_client.scroll(scroll_id=response['_scroll_id'], scroll='10m')

cursor.execute("""SELECT COUNT(*) FROM table_name""")
print(cursor.fetchone())

# cursor.execute("""DROP TABLE table_name""")

cursor.close()
postgres_client.commit()
postgres_client.close()

print(datetime.now() - start)