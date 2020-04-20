# Docker-compose file
Crie um arquivo chamado `docker-compose.yaml` com o seguinte conteúdo:  

```yaml
version: '3'

services:
        mongo:
                container_name: mongo
                image: mongo
                restart: always
                ports:
                        - "27017:27017"
                environment:
                        MONGO_INITDB_ROOT_USERNAME: catalog
                        MONGO_INITDB_ROOT_PASSWORD: catalog
        postgres:
                container_name: postgres
                image: postgres
                restart: always
                environment:
                        POSTGRES_PASSWORD: catalog
                        POSTGRES_USER: catalog
                ports:
                        - "5432:5432"
        elasticsearch:
                container_name: elasticsearch
                image: elasticsearch:7.5.1
                ports:
                        - "9200:9200"
                        - "9300:9300"
                environment:
                        discovery.type: single-node
```

Abra o terminal no diretório do arquivo e use `sudo docker-compose up`  