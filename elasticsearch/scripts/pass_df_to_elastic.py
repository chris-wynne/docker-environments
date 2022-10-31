import pandas as pd
import elasticsearch
from elasticsearch import Elasticsearch
from elasticsearch import helpers
es_client = Elasticsearch(http_compress=True, http_auth=('elastic', 'harp'))
import json

df = pd.read_csv('input_data') #change to desired processed data source

def filterKeys(document):
    use_these_keys = ['uuid', 'id', 'file', 'content', 'extension', 'metadata'] #change this to match desired df values
    return {key: document[key] for key in use_these_keys }

def doc_generator(df):
    df_iter = df.iterrows()
    for index, document in df_iter:
        yield {
                "_index": f"{document['uuid']}",
                "_type": f"{document['extension']}",
                "_id" : f"{document['id']}", #elastic unique id
                "_source": filterKeys(document),
            }
    raise StopIteration
helpers.bulk(es_client, doc_generator(df))