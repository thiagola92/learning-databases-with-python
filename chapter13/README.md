# Single insert VS package insert
Comparação entre enviar um documento por vez e enviar vários documentos de uma vez.  

# Warning
Eu **não** executei diversas vezes e fiz uma média para ter uma boa aproximação do tempo que demora.  
Eu **não** reservei o computador apenas para está tarefa.  
Por isto não considere estes tempos como certos, apenas servem para dar uma idéia.  

# MongoDB
| 1       | 10000   |
| ------- | ------- |
| 0:07:35 | 0:00:33 |

# Elasticsearch
| 1       | 10000   |
| ------- | ------- |
| 4:32:51 | 0:13:51 |

# Postgres
| 1       | 10000   |
| ------- | ------- |
| ? | 0:01:56 |

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