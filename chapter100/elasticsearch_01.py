import time
from datetime import datetime
from elasticsearch import Elasticsearch

start = datetime.now()

client = Elasticsearch("http://username:password@127.0.0.1:9200")

client.indices.create(index="index_name")

_id = 0

with open("utils/trash.csv") as file:
    for line in file.readlines():
        name, description = line.split(",")

        client.create(
            index="index_name",
            id=(_id := _id + 1),
            document={"name": name, "description": description},
        )

while True:
    stats = client.count(index="index_name")

    if stats["count"] == _id:
        break

    time.sleep(1)

print(client.count(index="index_name"))

client.indices.delete(index="index_name")

print(datetime.now() - start)
