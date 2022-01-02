import asyncio
from datetime import datetime
from elasticsearch import helpers, AsyncElasticsearch

start = datetime.now()


async def main():
    client = AsyncElasticsearch("http://username:password@127.0.0.1:9200", timeout=60)

    await client.indices.create("index_name")

    package = []
    _id = 0

    with open("utils/trash.csv") as file:
        for line in file.readlines():
            name, description = line.split(",")

            package.append(
                {
                    "_index": "index_name",
                    "_id": (_id := _id + 1),
                    "_source": {"name": name, "description": description},
                }
            )

            if len(package) >= 10000:
                await asyncio.gather(
                    helpers.async_bulk(client, package[:2500], max_retries=10),
                    helpers.async_bulk(client, package[2500:5000], max_retries=10),
                    helpers.async_bulk(client, package[5000:7500], max_retries=10),
                    helpers.async_bulk(client, package[7500:], max_retries=10),
                )
                package.clear()

    if package:
        await helpers.async_bulk(client, package, max_retries=10)

    print(await client.count(index="index_name"))

    await client.indices.delete("index_name")

    await client.close()


asyncio.run(main())

print(datetime.now() - start)
