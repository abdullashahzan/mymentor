import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_TOKEN")
url = "https://api.groq.com/openai/v1/models"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
data = response.json()

while True:
    user_query = input("Collect models or Show data? [1/2]: ")
    if user_query == "1":
        with open('models.txt', 'w') as f:
            models = []
            for i in data['data']:
                models.append(i['id'])
            f.write(" -- ".join(models))

        print("List updated successfully!")
        break
    elif user_query == "2":
        for i in data['data']:
            print(i)
        break
    else:
        break