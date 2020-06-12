from elasticsearch import Elasticsearch

elasticsearch = Elasticsearch([{'host': '172.18.0.2', 'port': 9200}, {'host': '172.18.0.2', 'port': 9300}])
# elasticsearch = Elasticsearch("http://172.18.0.4:9200") # Using URL

elasticsearch.indices.create('elastic')

elasticsearch.create(index='elastic', doc_type='produtos', id=1, body={
    'sku': 134218478,
    'name': 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial',
    'description': 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Com o Robô Aspirador de Pó Fast Clean RB-01 da Mondial, sua casa fica limpa sem que você precise manusear o aparelho. Esse modelo consegue varrer, aspirar e limpar diversos tipos de superfícies ao circular sozinho pelo ambiente. Tudo isso sem danificar paredes ou móveis. Graças aos seus sensores inteligentes, ele consegue desviar de obstáculos e até mesmo evitar possíveis quedas. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)',
    'category': 'eletroportáteis'
})

elasticsearch.update(index='elastic', id=1, body={
    'name': 'super robô'
})

p = elasticsearch.get(index='elastic', doc_type='produtos', id=1)
print(p)

elasticsearch.indices.delete('elastic')