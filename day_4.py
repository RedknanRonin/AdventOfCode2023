import re


def read_lines_to_list(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]  # Remove leading and trailing whitespaces
            return lines
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


lines = read_lines_to_list("txt")
sum = 0
copiesOfACard=[1]*len(lines)

cardsWithoutStart=[]
for each in lines:
    cardsWithoutStart.append(re.sub(r'^.*?:', ':', each))


def howManyCorrect(winning,your):
    correct=0
    for each in winning:
        if each in your:
            if each!="":
                correct+=1
    return correct

def evaluateLine(lineNumber,winning,your):
    for i in range (howManyCorrect(winning,your)):

        copiesOfACard[lineNumber+i+1]+=copiesOfACard[lineNumber]


lineCount=0
for line in cardsWithoutStart:
    row=line.split("|")
    winningNumbers=row[0].split(" ")
    yourNumbers=row[1].split(" ")
    evaluateLine(lineCount,winningNumbers,yourNumbers)
    lineCount+=1


for each in copiesOfACard: sum+=each
print(sum)