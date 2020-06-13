import psycopg2
import psycopg2.extras

from datetime import datetime
from auto_package import AutoPackage

start = datetime.now()

database = psycopg2.connect("postgres://username:password@172.18.0.3/postgres")
cursor = database.cursor()

sql = """CREATE TABLE postgres(
    name text,
    description text
)"""
cursor.execute(sql)

def send(package):
  sql = """INSERT INTO postgres
      VALUES(%s, %s
  )"""

  psycopg2.extras.execute_batch(cursor, sql, package, page_size=len(package))

auto_package = AutoPackage(send=send, size=1000)

with open('trash.csv') as file:
  for line in file.readlines():
    name, description = line.split(',')
    auto_package.add((name, description))

sql = """SELECT COUNT(*) FROM postgres"""
cursor.execute(sql)
print(cursor.fetchone())

sql = """DROP TABLE postgres"""
cursor.execute(sql)

cursor.close()
database.commit()
database.close()

print(datetime.now() - start)