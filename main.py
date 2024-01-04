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


def documents_retrieve(search_client, subject_matter = ''): #hard-code subject matter to be more general for this demonstrator
    results = search_client.search(search_text=subject_matter)

    genai_content = ''
    for result in results:
        genai_content = genai_content + '\n Document: ' + result['content']
    
    return genai_content


def generate_report(subject_matter, driver, prompt_text_path = 'prompt.txt'):

    with open("prompt.txt","r") as f:
        prompt = f.read()

    prompt = prompt.replace('__SUBJECT_MATTER__', subject_matter).replace('__DRIVER__', driver)
    response = client.chat.completions.create(
        model="turbo16k", # model = "deployment_name".
        messages=[
            {"role": "system", "content": "You are an assistant who helps people write briefing notes. You can only use information provided below. " + genai_content},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content

genai_content = documents_retrieve(search_client)
output = generate_report(subject_matter, driver)

print(output)
