# Mongo-express
* `sudo docker pull mongo-express`  
* `sudo docker run --name="mongo-express" --network="mongo_network" -e ME_CONFIG_MONGODB_SERVER=mongo -p 8081:8081 --detach mongo-express`  
* http://127.0.0.1:8081/  

# Error

## Mongo-express exit after creating
É necessário que você passe um banco de mongo com qual ele vai se conectar.  
No caso eu aproveitei que já possuia um banco de mongo criado.  