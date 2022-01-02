# Comparasion
Comparação entre diversas maneiras de enviar documento para o banco.  
- Um documento por vez
- Um lote de 10 mil documentos por vez
- Utilizando async
- Utilizando thread

Em alguns bancos é necessário esperar processarem para os documentos estarem disponíveis e essa espera é inclusa no código.  

# Warning
Eu **não** executei diversas vezes e fiz uma média para ter uma boa aproximação do tempo que demora.  
Eu **não** reservei o computador apenas para está tarefa.  
Por isto não considere estes tempos como certos, apenas servem para dar uma idéia.  

# MongoDB
| 1       | 10000   | async   | thread  |
| ------- | ------- | ------- | ------- |
| 0:01:10 | 0:00:03 | - | - |

## requirements
`pip install motor`  

# Elasticsearch
| 1       | 10000   | async   | thread  |
| ------- | ------- | ------- | ------- |
| 0:22:55 | 0:00:32 | - | - |

# Meilisearch
| 1       | 10000   | async   | thread  |
| ------- | ------- | ------- | ------- |
| - | 0:21:19 | - | - |

## requirements
`pip install elasticsearch[async]`  

# Postgres
| 1       | 10000   | async   | thread  |
| ------- | ------- | ------- | ------- |
| 0:07:04 | 0:00:22 | - | - |

# Hardware
* **Operating System**: Ubuntu 20.04 (64-bit)  
* **Memory**: (4x) 8GB 2400MHz  
* **CPU**: Intel Core i5-7600K @ 3.80GHz x 4  
* **HD**: 1TB 7200RPM SATA 6Gb/S 64MB  

# Details
* **Database**: Docker Local  
* **File Size**: 175 MB  
* **Documents**: 100001  
* Columns
  * **name**: Conjunto aleatório de caracteres, ou seja, texto aleatório  
  * **description**: Conjunto de textos aleatórios  