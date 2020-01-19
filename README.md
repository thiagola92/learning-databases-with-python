# Database

## Postgres
`sudo docker network create postgres_network`  
`sudo docker run --name="postgres" --network="postgres_network" --env="POSTGRES_PASSWORD=postgres" --publish 5432:5432 --detach postgres:11`  

## Mongo
`sudo docker network create mongo_network`  
`sudo docker run --name="mongo" --network="mongo_network" --detach mongo`

## Elasticsearch
`sudo docker network create elasticsearch_network`  
`sudo docker run --name="elasticsearch" --network="elasticsearch_network" -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" --detach elasticsearch:7.5.1`  