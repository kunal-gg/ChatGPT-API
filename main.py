import requests
import json
import environ

env = environ.Env()
environ.Env.read_env()


# API endpoint URL
url = "https://api.openai.com/v1/chat/completions"

# API request parameters
data = {
  "model": "gpt-3.5-turbo",
  "messages": [{"role": "user", "content": "What is the value of 2 + 2?"}]
}
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {env('API_KEY')}"
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
        print(response_json['choices'][0]['message']['content'])

    else:
        print("API request failed with status code:", response.status_code)




