import time
from datetime import datetime
from meilisearch import Client

start = datetime.now()

client = Client("http://127.0.0.1:7700", "password")

client.create_index("index_name")

package = []
_id = 0

with open("utils/trash.csv") as file:
    for line in file.readlines():
        name, description = line.split(",")

        package.append(
            {
                "id": (_id := _id + 1),
                "name": name,
                "description": description,
            }
        )

        if len(package) >= 10000:
            client.index("index_name").add_documents(package)
            package.clear()

if package:
    client.index("index_name").add_documents(package)

while True:
    stats = client.index("index_name").get_stats()

    if stats["numberOfDocuments"] == _id:
        break

    time.sleep(1)

print(client.index("index_name").get_stats())

client.index("index_name").delete()

print(datetime.now() - start)
