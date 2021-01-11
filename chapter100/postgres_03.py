import asyncio
import psycopg3

from datetime import datetime

start = datetime.now()

async def main():
  client = await psycopg3.AsyncConnection.connect("postgres://username:password@127.0.0.1")
  cursor = await client.cursor()

  await cursor.execute("""
    CREATE TABLE table_name(
      name text,
      description text
    )
  """)

  package = []
  insert_sql = """
    INSERT INTO table_name
      VALUES(%s, %s)
  """

  with open('utils/trash.csv') as file:
    for line in file.readlines():
      name, description = line.split(',')
      
      package.append((name, description))

      if len(package) >= 10000:
        await asyncio.gather(
          cursor.executemany(insert_sql, package[:2500]),
          cursor.executemany(insert_sql, package[2500:5000]),
          cursor.executemany(insert_sql, package[5000:7500]),
          cursor.executemany(insert_sql, package[7500:])
        )
        await client.commit()
        package.clear()

  if package:
    await cursor.executemany(insert_sql, package)
    await client.commit()

  await cursor.execute("""SELECT COUNT(*) FROM table_name""")
  print(await cursor.fetchone())

  await cursor.execute("""DROP TABLE table_name""")

  await cursor.close()
  await client.commit()
  await client.close()

asyncio.run(main())

print(datetime.now() - start)