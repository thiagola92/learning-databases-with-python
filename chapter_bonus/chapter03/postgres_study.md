# Pgadmin
* `sudo docker pull dpage/pgadmin4`  
* `sudo docker run --name="pgadmin" --network="postgres_network" -p 15432:80 --env="PGADMIN_DEFAULT_EMAIL=thiagola92@gmail.com" --env="PGADMIN_DEFAULT_PASSWORD=pgadmin" --detach dpage/pgadmin4`  
* http://localhost:15432/  