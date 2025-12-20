import pdfplumber
import os

def cloud():
	text = ''
	for i in range(1,10):
		with pdfplumber.open(f"local/CloudFiles/{i}.pdf") as pdf:
			text += ''.join(page.extract_text() for page in pdf.pages)
		print(f"Text extracted from {i}.pdf successfully!")

	with open("cloud.txt", "w") as ref:
		ref.write(text)
	return True

def ai():
	text = ''
	files = os.listdir('./local/AIFiles')
	for file_name in files:
		with open(f"local/AIFiles/{file_name}", "r") as f:
			text += f"{file_name}'s content\n"
			text += f.read()
		print(f"Text extracted from {file_name} successfully!")
	with open("ai.txt", "w") as ref:
		ref.write(text)
	return True

ai()
