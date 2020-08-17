import psycopg2

from datetime import datetime

start = datetime.now()

database = psycopg2.connect("postgres://username:password@127.0.0.1")
cursor = database.cursor()

cursor.execute("""
  CREATE TABLE table_name(
    name text,
    description text
  )
""")

with open('utils/trash.csv') as file:
  for line in file.readlines():
    name, description = line.split(',')

    cursor.execute(f"""
      INSERT INTO table_name
        VALUES('{name}', '{description}')
    """)

    database.commit()

cursor.execute("""SELECT COUNT(*) FROM table_name""")
print(cursor.fetchone())

cursor.execute("""DROP TABLE table_name""")

cursor.close()
database.commit()
database.close()

print(datetime.now() - start)