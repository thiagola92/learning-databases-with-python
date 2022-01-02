from elasticsearch import Elasticsearch

client = Elasticsearch("http://username:password@127.0.0.1:9200")

client.indices.create(index="index_name")

client.update(
    index="index_name",
    id=1,
    doc_as_upsert=True,
    doc={
        "sku": 134218478,
        "name": "Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial",
        "description": "Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)",
        "category": "eletroportáteis",
    },
)

# Upsert information
client.update(
    index="index_name",
    id=1,
    doc_as_upsert=True,
    doc={"name": "Rb-01 - Robô Aspirador De Pó SUPER Fast Clean Bivolt - Mondial"},
)

# Alternative
# client.update(index='index_name', id=1, script={
#   'source': "ctx._source.name = 'super robô'"
# })

p = client.get(index="index_name", id=1)
print(p)

client.indices.delete(index="index_name")
