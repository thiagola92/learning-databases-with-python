from elasticsearch import Elasticsearch

# Connect to database
elasticsearch = Elasticsearch("http://username:password@172.18.0.4:9200")

# Create index
elasticsearch.indices.create('elastic')

# Insert information
product = {
    'sku': 134218478,
    'name': 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial',
    'description': 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Com o Robô Aspirador de Pó Fast Clean RB-01 da Mondial, sua casa fica limpa sem que você precise manusear o aparelho. Esse modelo consegue varrer, aspirar e limpar diversos tipos de superfícies ao circular sozinho pelo ambiente. Tudo isso sem danificar paredes ou móveis. Graças aos seus sensores inteligentes, ele consegue desviar de obstáculos e até mesmo evitar possíveis quedas. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)',
    'category': 'eletroportáteis'
}
elasticsearch.create(index='elastic', id=1, body=product)

# Query information
p = elasticsearch.get(index='elastic', id=1)
print(p)

# Destroy index
elasticsearch.indices.delete('elastic')