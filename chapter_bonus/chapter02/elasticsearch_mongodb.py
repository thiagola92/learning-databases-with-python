import elasticsearch
from elasticsearch import helpers

import pymongo

from datetime import datetime
from auto_package import AutoPackage

elasticsearch_client = elasticsearch.Elasticsearch([{'host': '172.20.0.2', 'port': 9200}, {'host': '172.20.0.2', 'port': 9300}])

response = elasticsearch_client.search(index='elastic',
                                      doc_type='type',
                                      body= {
                                        'query': {
                                          'match_all': {}
                                        },
                                        size = 1000
                                      },
                                      scroll='10m')

while len(response['hits']['hits']) > 0:
  response = elasticsearch_client.scroll(scroll_id=response['_scroll_id'], scroll='10m')