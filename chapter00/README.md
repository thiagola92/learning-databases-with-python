# Docker-compose
Baixe o arquivo [docker-compose.yaml](docker-compose.yaml), execute o comando `sudo docker-compose up` no mesmo diretório que o arquivo.  

# Obtendo ip
Docker normalmente utiliza IPs como `172.x.y.z`, para descobrir o IP do seu container utilize:  
`sudo docker inspect CONTAINER_NAME | grep "IPAddress"`  

# GUI
Interfaces gráficas que podem auxiliar na visualização dos dados.  

## Postgres 
Beekeeper Studio: https://www.beekeeperstudio.io/

## Elastic
Kibana: incluso no `docker-compose.yaml`

## MongoDB
Extensão do VSCode: https://marketplace.visualstudio.com/items?itemName=mongodb.mongodb-vscode
