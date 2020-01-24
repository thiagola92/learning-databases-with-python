# Mongo
`sudo docker pull mongo`  
`sudo docker network create mongo_network`  
`sudo docker run --name="mongo" --network="mongo_network" --detach mongo`  

## Obtendo ip
`sudo docker inspect mongo | grep "IPAddress"`  