import psycopg2

database = psycopg2.connect(host='127.0.0.1', dbname='postgres', user='postgres', password='postgres')
cursor = database.cursor()

sql = """CREATE TABLE produtos(
    sku integer,
    name varchar(255),
    description text,
    category varchar(255)
)"""
cursor.execute(sql)

sql = """INSERT INTO produtos
    VALUES(134218478, 'Rb-01 - Robô Aspirador De Pó Fast Clean Bivolt - Mondial', 'Use a tecnologia a seu favor para aproveitar a vida longe da faxina. Com o Robô Aspirador de Pó Fast Clean RB-01 da Mondial, sua casa fica limpa sem que você precise manusear o aparelho. Esse modelo consegue varrer, aspirar e limpar diversos tipos de superfícies ao circular sozinho pelo ambiente. Tudo isso sem danificar paredes ou móveis. Graças aos seus sensores inteligentes, ele consegue desviar de obstáculos e até mesmo evitar possíveis quedas. Conheça mais essa facilidade para o seu lar e deixe tuuuudo limpinho :)', 'eletroportáteis'
)"""
cursor.execute(sql)

sql = """UPDATE produtos
SET name = 'super robô'
WHERE sku = 134218478
"""
cursor.execute(sql)

sql = """SELECT * FROM produtos"""
cursor.execute(sql)

p = cursor.fetchone()
print(p)

sql = """DROP TABLE produtos"""
cursor.execute(sql)

cursor.close()
database.commit()
database.close()