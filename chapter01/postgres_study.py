# pip install psycopg
import psycopg

# Connect to database
client = psycopg.connect("postgres://username:password@127.0.0.1")
cursor = client.cursor()

# Create table
cursor.execute("""
  CREATE TABLE table_name(
    sku integer,
    name varchar(255),
    description text,
    category varchar(255)
  )
""")

# Insert information
cursor.execute("""
  INSERT INTO table_name
    VALUES(134218478, 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial', 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)', 'eletroportáteis')
""")

# Query information
cursor.execute("""SELECT * FROM table_name""")
p = cursor.fetchone()
print(p)

# Destroy table
cursor.execute("""DROP TABLE table_name""")

# IMPORTANT: Close connection
#
# Is dangerous to live a connection open,
# it could block access from other users to tables
cursor.close()
client.commit()
client.close()