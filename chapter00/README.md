# Docker

## Postgres
[Postgres instruction](postgres_study.md)  

## MongoDB
[Docker instruction](mongodb_study.md)  

## Elastic
[Docker instruction](elasticsearch_study.md)  

# Obtendo ip
Docker normalmente utiliza IPs como `172.x.y.z`, para descobrir o IP do seu container utilize:  
`sudo docker inspect CONTAINER_NAME | grep "IPAddress"`  

# Text Editor
Normalmente todo container inclui o editor **Vi**, mas caso seja necessário instalar um de sua preferência utilize o package tool do sistema operacional.  
Por exemplo:  
`apt update`  
`apt install neovim`  
`nvim file_name`  