# Kibana
* `sudo docker pull kibana:7.5.1`  
* `sudo docker run --name="kibana" --network="elasticsearch_network" -p 5601:5601 --detach kibana:7.5.1`  
* http://localhost:5601/  

# Error

## Kibana não fica pronto
Ao acessar http://localhost:5601/, a seguinte mensagem aparecia:  
`Kibana server is not ready yet`  
Mesmo após minutos, ela persistia.  

**Solução**: Utilizei a mesma versão para o kibana e elasticsearch (7.5.1)  