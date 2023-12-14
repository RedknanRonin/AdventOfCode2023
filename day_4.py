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


cardsWithoutStart=[]
for each in lines:
    cardsWithoutStart.append(re.sub(r'^.*?:', ':', each))

for line in cardsWithoutStart:
    correct=0
    cardPoints=0
    row=line.split("|")
    winningNumbers=row[0].split(" ")
    yourNumbers=row[1].split(" ")

    for each in winningNumbers:
        if each in yourNumbers:
            if each!="":
                print(each)
                correct+=1


    if correct>=2:
        power=correct-2
        print("{}, correct: {}, added to sum: {}".format(line,correct,pow(2,power)))
        sum+=pow(2,correct-1)
    elif correct==1:
        sum+=correct


print(sum)