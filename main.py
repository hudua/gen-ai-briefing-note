import os
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

service_endpoint = ''
index_name = 'km'
key = ''

search_client = SearchClient(service_endpoint, index_name, AzureKeyCredential(key))

client = AzureOpenAI(
  azure_endpoint = '', 
  api_key='',  
  api_version="2023-05-15"
)

subject_matter = ''
driver = 'needing to provide a public media briefing.'
