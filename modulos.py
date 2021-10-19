
from abc import get_cache_token
import requests as req
from os.path import dirname,realpath
import json

from requests.models import Response



def __init__(self):
     self.path = dirname(realpath(__file__))+ '/'


 
def login(mail, password):
    payload = {
        'email':mail,
        'password': password
    }
    response = req.session().post('https://api.hunno.com.br/api/login',json=payload)
    response.headers.update({'authorization':json.loads(response.content)['token']})
    if response.status_code>=200 and response.status_code<=300:
        print(response.json())
        return response.status_code
       
    else:
        print(response.status_code)
        print(response.text)

def gettoken(headers):
    headers = '{"Authorization": "Bearer {token}'
    response2 = req.post("https://app.hunno.com.br/api/update/token/selected",headers=headers)
    
    if response2.status_code >=  200 and  response2.status_code <= 299:
        return response2.json()["token"]
        
    else:
        return response2.text 


def documentos(token):  
    url = "https://api.hunno.com.br:2004/dp/hunno/file/DocIncluidos"
    responseApi = req.get(url=url)

    
    if responseApi.status_code >=200 and responseApi.status_code <=299:
        return responseApi.json()
        
    else:
        print(responseApi.status_code)
        return responseApi.text

            
if __name__ == '__main__':
    session = login('marcio@pollocontabil.com.br','1')
    token = gettoken('bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJub21lIjoiTWFyY2lvIENvc3RhIFNpbHZhIiwiY3BmX2NucGoiOiI2MDYwMTk4MTU1MyIsImNvbnRyYWN0b3JfaWQiOiIxIiwiY29udHJhY3Rvcl9jbnBqIjoiMTEzNzgwMDQwMDAxMjQiLCJpZCI6IjEiLCJwZXJzb25faWQiOiIzMzEiLCJlbWFpbCI6Im1hcmNpb0Bwb2xsb2NvbnRhYmlsLmNvbS5iciIsInBob25lX2NlbGwiOiI3NTk5MTg2NDY5NiIsInR5cGVfdXNlciI6IkMiLCJwZXJmaWxfdXNlciI6IkQiLCJhY3RpdmUiOnRydWUsInVzZXJfaWRfc3VwZXJ2aXNvciI6IjEiLCJ1c2VyX3Bhc3N3b3JkIjoiJDJhJDEwJDJ6aDZjTHg0WjlkenVFUWVxNHd6Vi56ZzdkTTNEVXBlZ3Rpa0NONDg4bm5ac0RqbjJOUE1PIiwiZGVwYXJ0bWVudF9pZCI6IjciLCJzaW1wbGVfbmFtZSI6Ik3DoXJjaW8gQ29zdGEiLCJjYW1pbmhvX2ZvdG8iOm51bGwsImNvbnRyYWN0b3IiOlt7ImlkIjoiMSIsInBlcnNvbl9pZCI6IjExNyIsIm5vbWUiOiJQT0xMTyBDT05TVUxUT1JJQSBDT05UQUJJTCBFIFNJU1RFTUFTIExUREEiLCJjcGZfY25waiI6IjExMzc4MDA0MDAwMTI0IiwiZG9jX2Zvcm1hdCI6IjExLjM3OC4wMDQvMDAwMS0yNCIsInRpcG9faW5zY3JpY2FvIjoiMSIsInRpcG8iOiJKIiwiY2FtaW5ob19mb3RvIjoiaHR0cHM6Ly9pLmltZ3VyLmNvbS9TU25pRm9ELnBuZyIsImNydCI6IjEiLCJjcmNfc3Vic2NyaXB0aW9uIjoiMDE4MzkyIiwiZW1haWwiOiJtYXJjaW9AcG9sbGNvbnRhYmlsLmNvbS5iciIsIndoYXRzYXBwX2J1c2luZXNzIjoiNzU5OTE4NjQ2OTYiLCJpbnN0YWdyYW0iOm51bGwsImZhY2Vib29rIjpudWxsLCJ5b3V0dWJlIjpudWxsLCJsaW5rZWRpbiI6bnVsbCwiZ29vZ2xlX2FjY291bnQiOm51bGwsImRhdGVfcmVnaXN0ZXIiOiIyMDE5LTA3LTE0VDE0OjU2OjI0LjAwMFoiLCJkYXRlX2luaXRpYWxfY29udHJhY3QiOiIyMDE5LTA3LTE0VDE0OjU2OjI5LjAwMFoiLCJkYXRlX2xhc3RfY29udHJhY3QiOiIyMDE5LTA3LTE0VDE0OjU2OjM0LjAwMFoiLCJhY3RpdmVfY29udHJhY3QiOm51bGwsImRlcGFydGFtZW50b19pZCI6IjciLCJkZXBhcnRhbWVudG9fdXNlcl9yZXNwIjoiMSIsImRlcGFydGFtZW50b19ub21lIjoiQWRtaW5pc3RyYXRpdm8iLCJkZXBhcnRhbWVudG9fdGlwbyI6bnVsbH1dLCJjbGllbnRzIjpbXSwiaWF0IjoxNjM0NjczNDg1LCJleHAiOjE2MzQ3NTk4ODV9.J69dIGlu1n8z7P2hd38m_GkPku73JCQ5cjBVBMYdyPI')
    
    
  
     
    
    





    
