import psycopg2

from datetime import datetime

start = datetime.now()

database = psycopg2.connect(host='127.0.0.1', dbname='postgres', user='postgres', password='postgres')
cursor = database.cursor()

sql = """CREATE TABLE postgres(
  name text,
  description text
)"""
cursor.execute(sql)

with open('trash.csv') as file:
  for line in file.readlines():
    name, description = line.split(',')
    sql = f"""INSERT INTO postgres
      VALUES('{name}', '{description}'
    )"""
    cursor.execute(sql)

sql = """SELECT COUNT(*) FROM postgres"""
cursor.execute(sql)
print(cursor.fetchone())

sql = """DROP TABLE postgres"""
cursor.execute(sql)

cursor.close()
database.commit()
database.close()

print(datetime.now() - start)