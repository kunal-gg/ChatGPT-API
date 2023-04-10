import json

newLine = False
index = 0

questions = []

question = ""

with open('./text-files/example.txt', 'r', encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if line.startswith('Q.'):
            newLine = True
            question = ""

        if newLine:
            question = question + " " + line

        if line.startswith("(D)"):
            newLine = False
            question = question + line
            questions.append(question)
            question = ""        



questionsJson= {}
questionsJson["Questions"] = []

for question in questions:
    questionsJson["Questions"].append({
        "question": question
    })

with open('questions.json', 'w') as file:
    json.dump(questionsJson, file, indent=4)


