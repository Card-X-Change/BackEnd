import requests
import json

url = "http://iotcardxchange2.mybluemix.net/testcard5/"
payload1 = {
 'id':'1',
 'firstName':'Michelle',
 'lastName':'Chang',
}
payload2 = {
 'id':'2',
 'firstName':'Brian',
 'lastName':'Quock',
}
payload3 = {
 'id':'3',
 'firstName':'Albert',
 'lastName':'Vo',
}
payload4 = {
 '!yoda':'4',
 'firstName':'!yoda',
 'lastName':'Vo',
}
mypayload = json.dumps(payload4)
myResponse = requests.post(url, mypayload)
print myResponse.text

