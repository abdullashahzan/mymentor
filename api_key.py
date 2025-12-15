import requests
import os

url = "https://myportfolioshahzan.pythonanywhere.com/bs/"
response = requests.get(url)
key = response.json()['bs'].replace("'", "").replace(" ", "").replace("bs", "")

if os.path.exists(".env"):
	print("File already exists")
else:
	with open(".env", "a") as f:
		f.write(f'API_TOKEN = "{key}"')

print("API file created!")
