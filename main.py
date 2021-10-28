import json
from modulos import *
email = str(input("informe o email do usuario: "))
password = str(input("informe a senha do usuario: "))


if __name__ == '__main__':
    t  = Token
    primeiroToken = t.primeiro_token()
    segundoToken = t.segundo_token(primeiroToken)
    doc = documentos(segundoToken)
    print(doc)
    with open("clientes.json","w+") as f:
        json.dump(doc,f)
        
