# Database
> É possível se conectar com o banco de diversas maneiras, utilizando bibliotecas de terceiros ou não.  

* O objetivo deste capítulo envolve fazer 5 tarefas
  * Conectar ao banco
  * Criar tabela/collection/index
  * Inserir informação
  * Buscar informação
  * Destruir tabela/collection/index

# Postgres
[[Postgres code](postgres.py)]  

Importante fechar o cursor após toda interação sua com o banco. Deixar um cursor aberto pode travar o acesso para outras pessoas.  

# MongoDB
[[MongoDB code](mongodb.py)]  

As collections só existem apartir do momento que você insere nelas algum documento.  

# Elasticsearch
[[Elasticsearch code](mongo.py)]  
