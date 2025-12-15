# Client.py
from groq import Groq
from dotenv import load_dotenv
import os

# Configuring API key
load_dotenv()
api_key = os.getenv("API_TOKEN")

# Client
client = Groq(api_key=api_key)

try:
	with open("models.txt", "r") as f:
		AVAILABLE_MODELS = f.read().split(" -- ")
except:
	print("File models.txt could not be opened.")
#AVAILABLE_MODELS = [
#    'meta-llama/llama-4-scout-17b-16e-instruct',
#]

RULES = """
Rules you must follow to avoid penalty!
1) You are a very smart, intelligent and helpful AI assistant.
2) You must make sure to help user with any of their query.
3) Severe penalty will be issued on failing to obey the rules. 
"""

current_model = 'meta-llama/llama-4-scout-17b-16e-instruct'

def ai_response(user_query, current_model=current_model):
	prompt = f"User query: {user_query}"

	chat_completion = client.chat.completions.create(
		messages=[
		{"role": "system", "content": "You are sincere, smart and intelligent AI assistant"},
		{"role": "user", "content": prompt}
		],
		max_tokens=1000,
		temperature=0.7,
		model=current_model,
	)
	response = chat_completion.choices[0].message.content.strip()
	print(f"{response}")

try:
	while True:
		user_query = input("=> ")
		if user_query == "hi":
		    print("Service ran successfully!")
		    print("Commands: current model, change model, exit")
		elif user_query == "exit":
			break
		elif "print" in user_query:
			print(user_query.split("(")[1].replace(")", "").split('"')[1])
		elif user_query == "change model":
			try:
				for i in AVAILABLE_MODELS:
					print(i)
			except:
				print("File models.txt could not be opened!")
			selected_model = input("Select model: ")
			current_model = selected_model
			print(f"Current model: {current_model}")
		elif user_query == "current model":
			print(current_model)
		else:
		    ai_response(user_query)
except KeyboardInterrupt:
	pass