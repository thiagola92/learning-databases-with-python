import time
from datetime import datetime
from meilisearch import Client

start = datetime.now()

client = Client("http://127.0.0.1:7700", "password")

client.create_index("index_name")

_id = 0

with open("utils/trash.csv") as file:
    for line in file.readlines():
        name, description = line.split(",")

        client.index("index_name").add_documents(
            [
                {
                    "id": (_id := _id + 1),
                    "name": name,
                    "description": description,
                }
            ]
        )

while True:
    try:
        stats = client.index("index_name").get_stats()
    except Exception:
        continue

    if stats["numberOfDocuments"] == _id:
        break

    time.sleep(1)

print(client.index("index_name").get_stats())

client.index("index_name").delete()

print(datetime.now() - start)
