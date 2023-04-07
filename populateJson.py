import json

newLine = False
line9 = ''

questions = []

with open('./text-files/example.txt', 'r') as file:
    for line in file:
        line = line.strip()
        
        if line.startswith("9."):
            flag = True

        if flag:
            line9 += line
        

questions.append(line9)
print(questions)

with open('questions.json', 'w') as file:
    json.dump({"Questions": questions}, file)