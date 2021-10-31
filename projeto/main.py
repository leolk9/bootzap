from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
import json
from modulos import *

# email = str(input("informe o email do usuario: "))
# password = str(input("informe a senha do usuario: "))


if __name__ == '__main__':
    t  = Token
    j = Json_manager
    primeiroToken = t.primeiro_token()
    segundoToken = t.segundo_token(primeiroToken)
    doc = documentos(segundoToken)
    j.create_json()

   #tratando json pegando campos especificos
    for chave in doc:
        contatos =  doc[chave]  

    navegador = webdriver.Chrome()
    navegador.get("https://web.whatsapp.com/")
    time.sleep(10)

    #já estamos com o login feito no whatsapp web
    for contato in contatos:
        url = contato["Link"]
        numero = "55"+ contato["Celular"]
        mensagem = contato["Mensagem"] 
        texto = urllib.parse.quote(f"Oi, {mensagem}! {url}")
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
        navegador.get(link)
        while len(navegador.find_elements_by_id("side")) < 1:
            time.sleep(1)
        navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
        time.sleep(10)
        
            