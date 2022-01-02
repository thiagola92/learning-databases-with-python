import time
from clickhouse_driver import Client

client = Client.from_url("clickhouse://127.0.0.1")

client.execute("""
  CREATE TABLE table_name(
    sku UInt32,
    name String,
    description String,
    category String
  )
  ENGINE = MergeTree()
  ORDER BY sku
  PRIMARY KEY sku
""")

client.execute("""
  INSERT INTO table_name
    VALUES(134218478, 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial', 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)', 'eletroportáteis')
""")

# Update information
#
# It's an expensive operation and shouldn't be frequently,
client.execute("""
  ALTER TABLE table_name
    UPDATE name = 'super robô'
    WHERE sku = 134218478
""")

# Wait update
while True:
  rows = client.execute('SELECT * FROM table_name LIMIT 1')
  first_row = rows[0]

  if first_row[1] == 'super robô':
    break
  
  time.sleep(1)

print(client.execute('SELECT * FROM table_name LIMIT 1'))

client.execute("""DROP TABLE table_name""")
