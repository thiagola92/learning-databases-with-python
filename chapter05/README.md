# Docker
Diferente bancos utilizam diferentes ferramentas para auxiliar visualmente.  
Escolhi sempre utilizar ferramentas parcialmente/totalmente free e que possuem um imagem docker (por segurança).  

## Postgres
[Pgadmin instruction](postgres_study.md)  

## MongoDB
[Mongo-express instruction](mongo_study.md)

## Elastic
[Kibana instruction](elasticsearch_study.md)  

# Docker-compose

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
        mongo_express:
                container_name: mongo_express
                image: mongo-express
                restart: always
                ports:
                        - "8081:8081"
                environment:
                        ME_CONFIG_MONGODB_ADMINUSERNAME: catalog
                        ME_CONFIG_MONGODB_ADMINPASSWORD: catalog
        postgres:
                container_name: postgres
                image: postgres
                restart: always
                environment:
                        POSTGRES_PASSWORD: catalog
                        POSTGRES_USER: catalog
                ports:
                        - "5432:5432"
        pgadmin:
                container_name: pgadmin
                image: dpage/pgadmin4
                restart: always
                ports:
                        - "15432:80"
                environment:
                        PGADMIN_DEFAULT_EMAIL: catalog
                        PGADMIN_DEFAULT_PASSWORD: catalog
        elasticsearch:
                container_name: elasticsearch
                image: elasticsearch:7.5.1
                ports:
                        - "9200:9200"
                        - "9300:9300"
                environment:
                        discovery.type: single-node
        kibana:
                container_name: kibana
                image: kibana:7.5.1
                ports:
                        - "5601:5601"
```