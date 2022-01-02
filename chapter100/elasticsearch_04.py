from datetime import datetime
from threading import Thread, Lock
from elasticsearch import helpers, Elasticsearch

start = datetime.now()

client = Elasticsearch("http://username:password@127.0.0.1:9200", timeout=60)

client.indices.create("index_name")

threads_count = 0
lock = Lock()
package = []
_id = 0


def send(p):
    global threads_count

    with lock:
        threads_count += 1

    helpers.bulk(client, p, max_retries=20)

    with lock:
        threads_count -= 1


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
            while threads_count >= 4:
                pass
            Thread(target=send, args=(package[:],), daemon=True).start()
            package.clear()

if package:
    helpers.bulk(client, package, max_retries=10)

while threads_count != 0:
    pass

print(client.count(index="index_name"))

client.indices.delete("index_name")

print(datetime.now() - start)
