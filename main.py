import requests
import json
import openpyxl
import os
from dotenv import load_dotenv

load_dotenv()

# the api key
api_key = "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"

workbook = openpyxl.Workbook();
worksheet = workbook.active;
result = [
    ['Question', 'Answer']
]

# API endpoint URL
url = "https://api.openai.com/v1/chat/completions"


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

with open('questions.json', 'r') as file:
    # Load the JSON data from the file
    questions = json.load(file)




for question in questions["Questions"]: 
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": question["question"]}]
        }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        response_json = json.loads(response.text)
        answer = response_json['choices'][0]['message']['content']
        result.append([question["question"], answer])
        print(answer)

    else:
        print("API request failed with status code:", response.json())



for row in result:
    worksheet.append(row)

workbook.save("result.xlsx")

