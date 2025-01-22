from algoliasearch_django import algolia_engine
from rest_framework.response import Response

def get_client(): 
    return algolia_engine.client

def get_index(index_name='cfe_Product'):
    client = get_client()
    index = client.init_index(index_name)
    return index

def perform_search(query,*args, **kwargs):
    index = get_index()
    results = index.search(query)
    return results