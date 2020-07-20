# Requirement
Como já vimos como botar os dados no banco, os códigos vão partir do princípio que você já tem no banco de origem os dados e apenas quer move-los para o banco destino.  

# Warning
Eu **não** executei diversas vezes e fiz uma média para ter uma boa aproximação do tempo que demora.  
Eu **não** reservei o computador apenas para está tarefa.  
Por isto não considere estes tempos como certos, apenas servem para dar uma idéia.  

# MongoDB to
| Elasticsearch | Postgres |
| ------------- | -------- |
| 0:15:04       | 0:02:01  |

# Elasticsearch to
| Postgres | MongoDB |
| -------- | ------- |
| 0:02:08  | 0:00:53 |

# Postgres to
| Elasticsearch | MongoDB |
| ------------- | ------- |
| 0:14:24       | 0:00:53 |

# Hardware
* **Operating System**: Ubuntu 20.04 (64-bit)  
* **Memory**: (4x) 8GB 2400MHz  
* **CPU**: Intel Core i5-7600K @ 3.80GHz x 4  
* **HD**: 1TB 7200RPM SATA 6Gb/S 64MB  

# Details
* **Database**: Docker Local  
* **File Size**: 2,1GB  
* **Documents**: 1500001  
* Columns
  * **name**: Conjunto aleatório de caracteres, ou seja, texto aleatório  
  * **description**: Conjunto de textos aleatórios  