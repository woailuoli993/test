# _*_ coding:utf-8 _*_
from elasticsearch import Elasticsearch
from datetime import datetime

if __name__ == '__main__':
    print 'r'*30
    es = Elasticsearch([{'host': '10.174.93.111', 'port': '9200'}])
    #  es_one = es.get(index='ksxing', doc_type='testqm', id='5545c306f3805c7730c35fad')['_source']
    #  for i in es_one:
    #      print i, es_one.get(i)

    es_search_one = es.search(index='ksxing', doc_type='testqm', body={
        'query': {
            "bool": {
                "must": [
                    {
                        "query_string": {
                            "default_field": "_all",
                            "query": "caonimab"
                        }
                    }
                ],
                "filter": [
                    {"term": {"cop_id": 1}}
                ]
            }
        },
        "size": 5,
        "_source": ["cop_id"]
    })
    print "xixi" if es_search_one['hits']['hits'] is None else "haha"