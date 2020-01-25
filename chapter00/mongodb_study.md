# MongoDB
`sudo docker pull mongo`  
`sudo docker network create mongo_network`  
`sudo docker run --name="mongo" --network="mongo_network" --detach mongo`  

# Error
Erros com os quais esbarrei durante o aprendizado  

## Banco não inicializava
O comando `sudo docker start -i mongo` retornava:  

```bash
...
2020-01-25T05:31:41.676+0000 E  NETWORK  [initandlisten] Failed to unlink socket file /tmp/mongodb-27017.sock Operation not permitted
2020-01-25T05:31:41.676+0000 F  -        [initandlisten] Fatal Assertion 40486 at src/mongo/transport/transport_layer_asio.cpp 693
```

**Solução adotada**: Deletei o container e criei um novo  