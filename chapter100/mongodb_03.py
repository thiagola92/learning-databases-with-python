import asyncio
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient

start = datetime.now()


async def main():
    client = AsyncIOMotorClient("mongodb://username:password@127.0.0.1")
    database = client["database_name"]
    collection = database["collection_name"]

    package = []

    with open("utils/trash.csv") as file:
        for line in file.readlines():
            name, description = line.split(",")

            package.append({"name": name, "description": description})

            if len(package) >= 10000:
                await asyncio.gather(
                    collection.insert_many(package[:2500]),
                    collection.insert_many(package[2500:5000]),
                    collection.insert_many(package[5000:7500]),
                    collection.insert_many(package[7500:]),
                )
                package.clear()

    if package:
        await collection.insert_many(package)

    print(await collection.count_documents({}))

    await collection.drop()
    await client.drop_database("mongo")


asyncio.run(main())

print(datetime.now() - start)
