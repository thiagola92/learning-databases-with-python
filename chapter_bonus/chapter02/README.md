# Requirement
Como já vimos como botar os dados no banco, os códigos vão partir do princípio que você já tem no banco de origem os dados e apenas quer move-los para o banco destino.  

# AutoPackage
AutoPackage é uma classe minha criada justamente para armazenar uma quantidade de item antes de envia-los, ela apenas recebe a função responsável por enviar o lote que ela está armazenando no momento.  

# Warning
Eu **não** executei diversas vezes e fiz uma média para ter uma boa aproximação do tempo que demora.  
Eu **não** reservei o computador apenas para está tarefa.  
Por isto não considere estes tempos como certos, apenas servem para dar uma idéia.  

# MongoDB to
| Elasticsearch | Postgres |
| ------------- | -------- |
| 0:13:05       | 0:02:21  |

# Elasticsearch to
| Postgres | MongoDB |
| -------- | ------- |
| 0:02:52  | 0:01:42 |

# Postgres to
| Elasticsearch | MongoDB |
| ------------- | ------- |
| 0:13:13       | 0:01:06 |

# Information
* **Operating System**: Ubuntu 19.10  
* **Memory**: (2x) 8GB 2400MHz  
* **CPU**: Intel Core i5-7600K @ 3.80GHz x 4  
* **HD**: 1TB 7200RPM SATA 6Gb/S 64MB  
* **File Size**: 2,1GB  
* **Database**: Docker Local  
* Columns
  * **name**: Conjunto aleatório de caracteres, ou seja, texto aleatório  
  * **description**: Conjunto de textos aleatórios  