# AutoPackage
AutoPackage é uma classe minha criada justamente para armazenar uma quantidade de item antes de envia-los, ela apenas recebe a função responsável por enviar o lote que ela está armazenando no momento.  

# Warning
Eu **não** executei diversas vezes e fiz uma média para ter uma boa aproximação do tempo que demora.  
Eu **não** reservei o computador apenas para está tarefa.  
Por isto não considere estes tempos como certos, apenas servem para dar uma idéia.  

# MongoDB
| 1       | 1000    | speed up |
| ------- | ------- | -------- |
| 0:06:14 | 0:01:22 | 78%      |

# Elasticsearch
| 1       | 1000    | speed up |
| ------- | ------- | -------- |
| 3:47:50 | 0:11:59 | 94%      |

# Postgres
| 1       | 1000    | speed up |
| ------- | ------- | -------- |
| 0:02:39 | 0:02:09 | 18%      |

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