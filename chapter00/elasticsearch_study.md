# Elastic
* `sudo docker pull elasticsearch:7.5.1`  
* `sudo docker network create elasticsearch_network`  
* `sudo docker run --name="elasticsearch" --network="elasticsearch_network" --publish 9200:9200 --publish 9300:9300 --env="discovery.type=single-node" --env="ELASTIC_USERNAME=username" --env="ELASTIC_PASSWORD=password" --detach elasticsearch:7.5.1`  