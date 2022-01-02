import psycopg

client = psycopg.connect("postgres://username:password@127.0.0.1")
cursor = client.cursor()

cursor.execute(
    """
    CREATE TABLE table_name(
        sku integer PRIMARY KEY,
        name varchar(255),
        description text,
        category varchar(255)
    )
    """
)

cursor.execute(
    """
    INSERT INTO table_name
        VALUES(134218478, 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial', 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)', 'eletroportáteis')
    ON CONFLICT(sku)
        DO UPDATE SET
        name = EXCLUDED.name
    """
)

# Update information
cursor.execute(
    """
    INSERT INTO table_name(sku, name)
        VALUES('134218478', 'Rb-01 - Robô Aspirador De Pó SUPER Fast Clean Bivolt - Mondial')
    ON CONFLICT(sku)
        DO UPDATE SET
        name = EXCLUDED.name
    """
)

cursor.execute("SELECT * FROM table_name")
print(cursor.fetchone())

cursor.execute("DROP TABLE table_name")

cursor.close()
client.commit()
client.close()
