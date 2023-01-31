import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch import helpers

indexname = 'name_of_your_index'

es_client = Elasticsearch(
    "http://localhost:9200",
    http_auth=("elastic", "harp")
)

#es_client.info() #test connection

#delete existing index
es_client.indices.delete(index=indexname, ignore=[400, 404])

df = pd.read_pickle("datasource.pkl") #change to desired processed data source

def filterKeys(document):
    use_these_keys = ['uuid', 'id', 'path', 'content', 'extension'] #change this to match desired df values
    return {key: document[key] for key in use_these_keys }

def doc_generator(df):
    df_iter = df.iterrows()
    for index, document in df_iter:
        yield {
                "_index": "conf",
                "_id" : f"{document['id']}", #elastic unique id
                "_source": filterKeys(document),
            }
    raise StopIteration
helpers.bulk(es_client, doc_generator(df))