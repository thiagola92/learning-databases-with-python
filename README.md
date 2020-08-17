# Database
Um repositório para eu explorar rapidamente o básico dos bancos de dados
Os bancos de dados utilizados foram montados utilizando Docker.  

# Chapter

* [Capítulo 0](chapter00/)
  * Para começar a aprender sobre os bancos é recomendado ter o banco na sua máquina local.
    * Utilizaremos o Docker para manter o banco.  
* [Capítulo 1](chapter01/)
  * Mínimo de como utilizar um banco
    * Conectar ao banco
    * Inserir informação
    * Ler informação
    * Deletar o banco
* [Capítulo 2](chapter02/)
  * Visualização do banco (GUI)
* [Capítulo 3](chapter03/)
  * Atualizar um item do banco
* [Capítulo 4](chapter04/)
  * Upsert (update + insert)
    * Atualizar item se ele existir
    * Inserir item se ele não existir
* [Capítulo 100](chapter100/)
  * Inserção de grande quantidade de dados no banco
* [Capítulo 101](chapter101/)
  * Movimentação de grande quantidade de dados entre bancos
  
# Observation
O nome dos arquivos terminam com `_study` para não dar conflito no import das bibliotecas.  
Ex: `import elasticsearch` precisa importar a biblioteca em vez de um arquivo chamado `elasticsearch.py`, por isso mudei o nome para `elasticsearch_study.py`  