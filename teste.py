import requests as req
values = '{"email":"marcio@pollocontabil.com.br","senha":"1"}'
response = req.post("https://api.hunno.com.br/api/login",data=values)
if response.status_code >=  200 and  response.status_code <= 299:
    token = (response.json()["token"])
    print(token)
    print(response.status_code)
else:
     print(response.text)
     print(response.status_code)
