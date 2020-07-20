# Database
Objetivo deste capítulo é executar um simples **upsert**.  
> Upsert = update OU insert  

Se o documento já existir, então ele será atualizado.  
Se o documento não existir, então ele será inserido.  

# Mongo
Não para esse capítulo...

```python
try:
  collection.insert_many(package, ordered=False)
except errors.BulkWriteError as e:
  print(f'One or more products already exist')
```

Para evitar que produtos com o mesmo id sejam adicionados ao mongo é preciso definir um index.  

```
db.collection_name.createIndex({"id_produto": 1}, {unique: true})
```