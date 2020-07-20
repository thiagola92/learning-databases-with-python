# Docker
Escolha o banco o qual está interessado e monte o container dele

## Postgres
[Postgres instruction](postgres_study.md)  

## MongoDB
[Docker instruction](mongodb_study.md)  

## Elastic
[Docker instruction](elasticsearch_study.md)  

# Docker-compose
Caso esteja interessado em mais que um, você pode utilizar o docker-compose para monta-los.  
Baixe o arquivo [docker-compose.yaml](docker-compose.yaml), execute o comando `sudo docker-compose up` no mesmo diretório que o arquivo.  

# Obtendo ip
Docker normalmente utiliza IPs como `172.x.y.z`, para descobrir o IP do seu container utilize:  
`sudo docker inspect CONTAINER_NAME | grep "IPAddress"`  