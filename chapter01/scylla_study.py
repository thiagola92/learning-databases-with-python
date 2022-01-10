# pip install scylla-drive
from cassandra.cluster import Cluster

cluster = Cluster(["127.0.0.1"])
session = cluster.connect()

# TODO
session.execute(
    """
    CREATE TABLE table_name(
        sku integer,
        name text
    )
    """
)