# Postgres
`sudo docker pull postgres:11`  
`sudo docker network create postgres_network`  
`sudo docker run --name="postgres" --network="postgres_network" --env="POSTGRES_PASSWORD=postgres" --publish 5432:5432 --detach postgres:11`  