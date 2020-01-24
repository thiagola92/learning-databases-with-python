# Database
> É possível se conectar com o banco de diversas maneiras, utilizando bibliotecas de terceiros ou não.  

* O objetivo deste capítulo envolve fazer 5 tarefas
  * Conectar ao banco
  * Criar tabela/collection/index
  * Inserir informação
  * Buscar informação
  * Destruir tabela/collection/index

# Postgres
```python
import psycopg2

# Connect to database
database = psycopg2.connect(host='127.0.0.1', dbname='postgres', user='postgres', password='postgres')
cursor = database.cursor()

# Create table
sql = """CREATE TABLE produtos(
    sku integer,
    name varchar(255),
    description text,
    category varchar(255)
)"""
cursor.execute(sql)

# Insert information
sql = """INSERT INTO produtos
    VALUES(134218478, 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial', 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Com o Robô Aspirador de Pó Fast Clean RB-01 da Mondial, sua casa fica limpa sem que você precise manusear o aparelho. Esse modelo consegue varrer, aspirar e limpar diversos tipos de superfícies ao circular sozinho pelo ambiente. Tudo isso sem danificar paredes ou móveis. Graças aos seus sensores inteligentes, ele consegue desviar de obstáculos e até mesmo evitar possíveis quedas. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)', 'eletroportáteis'
)"""
cursor.execute(sql)

# Query information
sql = """SELECT * FROM produtos"""
cursor.execute(sql)

products = cursor.fetchall()
print(products)

# Destroy table
sql = """DROP TABLE produtos"""
cursor.execute(sql)

# Close connection (important)
cursor.close()
database.commit()
database.close()
```

# MongoDB
```python
from pymongo import MongoClient

# Connect to database
client = MongoClient(host='172.19.0.2', port=27017)
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
```

# Elasticsearch
```python
from elasticsearch import Elasticsearch

elasticsearch = Elasticsearch({'host': '127.0.0.1', 'port': 9200})
```