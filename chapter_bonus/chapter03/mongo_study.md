# Mongo-express
* `sudo docker pull mongo-express`  
* `sudo docker run --name="mongo-express" --network="mongo_network" -e ME_CONFIG_MONGODB_SERVER=mongo -p 8081:8081 --detach mongo-express`  
* http://0.0.0.0:8081/  