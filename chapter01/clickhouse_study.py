from clickhouse_driver import Client

# Connect to database
client = Client.from_url("clickhouse://127.0.0.1")

# Create table
client.execute(
    """
    CREATE TABLE table_name(
        sku UInt32,
        name String,
        description String,
        category String
    )
    ENGINE = MergeTree()
    ORDER BY sku
    PRIMARY KEY sku
    """
)

# Insert information
client.execute(
    """
    INSERT INTO table_name
    VALUES(134218478, 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial', 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)', 'eletroportáteis')
    """
)

# Query information
print(client.execute("SELECT * FROM table_name"))

# Destroy table
client.execute("DROP TABLE table_name")
