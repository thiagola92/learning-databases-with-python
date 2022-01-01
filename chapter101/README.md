# Requirement
Como já vimos como botar os dados no banco, os códigos vão partir do princípio que você já tem no banco de origem os dados e apenas quer move-los para o banco destino.  

# Warning
Eu **não** executei diversas vezes e fiz uma média para ter uma boa aproximação do tempo que demora.  
Eu **não** reservei o computador apenas para está tarefa.  
Por isto não considere estes tempos como certos, apenas servem para dar uma idéia.  

# MongoDB to
| Elasticsearch | Postgres |
| ------------- | -------- |
| -       | -  |

# Elasticsearch to
| Postgres | MongoDB |
| -------- | ------- |
| -  | - |

# Postgres to
| Elasticsearch | MongoDB |
| ------------- | ------- |
| -       | - |

# Hardware
* **Operating System**: Ubuntu 20.04 (64-bit)  
* **Memory**: (4x) 8GB 2400MHz  
* **CPU**: Intel Core i5-7600K @ 3.80GHz x 4  
* **HD**: 1TB 7200RPM SATA 6Gb/S 64MB  

# Details
* **Database**: Docker Local  
* **File Size**: 141,6MB  
* **Documents**: 100001  
* Columns
  * **name**: Conjunto aleatório de caracteres, ou seja, texto aleatório  
  * **description**: Conjunto de textos aleatórios  