# Postgres
* `sudo docker pull postgres`  
* `sudo docker network create postgres_network`  
* `sudo docker run --name="postgres" --network="postgres_network" --env="POSTGRES_PASSWORD=password" --env="POSTGRES_USER=username" --publish 5432:5432 --detach postgres`  