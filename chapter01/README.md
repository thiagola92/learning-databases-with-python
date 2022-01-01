# Database
> É possível se conectar com o banco de diversas maneiras, utilizando bibliotecas de terceiros ou não.  

* O objetivo deste capítulo envolve fazer 5 tarefas
  * Conectar ao banco
  * Criar tabela/collection/index
  * Inserir informação
  * Buscar informação
  * Destruir tabela/collection/index
# Postgres
Importante fechar o cursor após toda interação sua com o banco. Deixar um cursor aberto pode travar o acesso para outras pessoas.  
Quando não especificado o banco de dados na URI, o default é ir para o nome do usuário.  
É possível especificar o nome do banco no final da URI: `postgres://username:password@127.0.0.1/database_name`  

Caso o banco não exista, é possível criar ele se conectando como admin. Exemplo:  
```python
client = psycopg2.connect("postgres://username:password@127.0.0.1")
client.autocommit = True
cursor = client.cursor()

cursor.execute("CREATE DATABASE database_name")

cursor.close()
client.close()
```

## requirements
`pip install psycopg`  

# MongoDB
As collections só existem apartir do momento que você insere nelas algum documento.  

## requirements
`pip install pymongo`  

# Elasticsearch
Pode se testar se conectou com o banco com `elasticsearch.ping()`, retorna `True` se conectou com sucesso.  

## requirements
`pip install elasticsearch`  


# Meilisearch  

## requirements
`pip install meilisearch`  