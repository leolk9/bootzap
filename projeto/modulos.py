import requests as req
import json
from os.path import dirname,realpath,isfile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

class Token:

    def __init__(self,email,password):
        self.email = email
        self.password = password
        
        

    def primeiro_token():
        values = {
        "email": "marcio@pollocontabil.com.br",
        "password": "1"
        }
        response = req.post("https://api.hunno.com.br/api/login",data = values)
        if response.status_code >=  200 and  response.status_code <= 299:
            print(response.status_code)
            return response.json()["token"]
        else:
            print(response.status_code)
            return response.text


    def segundo_token(token):
        headers = {
            'Authorization': 'Bearer {}'.format(token)
            }
        response = req.post("https://app.hunno.com.br/api/update/token/selected",headers=headers)
        print(response.status_code)
        if response.status_code >=  200 and  response.status_code <= 299:
            return response.json()["token"]
        else:
            print(response.status_code)
            return response.text  
            

def documentos(token):  
    cabecalho = {'Authorization': 'Bearer {}'.format(token) }
    url = "https://api.hunno.com.br:2004/dp/hunno/file/DocIncluidos"
    global responseApi
    responseApi = req.get(url=url,headers=cabecalho)
    
    

    if responseApi.status_code >=200 and responseApi.status_code <=299:
        print(responseApi.status_code)
        return responseApi.json()
        
        
    else:
        print(responseApi.status_code)
        return responseApi.text


class Json_manager(Token): 


    def __init__(self):
        super().__init__(responseApi)
        self.path = dirname(realpath(__file__))+'/'
        self.dados = json.dumps(responseApi.json())
    
    def create_json():
        with open('cliente.json','w') as f:
            json.dump(responseApi.json(),f,indent=2)

    


# def mandar_mensagem(numero,link):
#     navegador = webdriver.Chrome()
#     navegador = webdriver.Chrome()
#     navegador.get("https://web.whatsapp.com/")

#     while len(navegador.find_elements_by_id("side")) < 1:
#         time.sleep(1)

#     # já estamos com o login feito no whatsapp web
#     for i, mensagem in enumerate(contatos['Mensagem']):
        
#         numero = contatos[i, "Número"]
#         texto = urllib.parse.quote(f"Olá,tudo bem? ! {mensagem}")
#         link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
#         navegador.get(link)
#         while len(navegador.find_elements_by_id("side")) < 1:
#             time.sleep(1)
#         navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
#         time.sleep(10)
        
if __name__ == '__main__':
    t  = Token
    j = Json_manager
    primeiroToken = t.primeiro_token()
    segundoToken = t.segundo_token(primeiroToken)
    doc = documentos(segundoToken)
    j.create_json()
   
    for chave in doc:
       contatos =  doc[chave]  
         
    for contato in contatos:
        email = contato['Email']
        #print(email)

        mensagem = contato["Mensagem"]    
        #print(mensagem)

        link = contato["Email"]    
        #print(link)
        
        numero = contato["Celular"]     
        #print(numero)
    

    navegador = webdriver.Chrome()
    navegador = webdriver.Chrome()
    navegador.get("https://web.whatsapp.com/")

    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)

    # já estamos com o login feito no whatsapp web
    for mensagem in contatos:
        
        numero = mensagem[ "Número"]
        texto = urllib.parse.quote(f"Olá,tudo bem? ! {mensagem}")
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
        navegador.get(link)
        while len(navegador.find_elements_by_id("side")) < 1:
            time.sleep(1)
        navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
        time.sleep(10)
        
        