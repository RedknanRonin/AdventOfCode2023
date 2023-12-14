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


def check_for_symbol(topRow, index, bottomRow):
    tbr = False
    if topRow[index] != ".":
        tbr = True
    if bottomRow[index] != ".":
        tbr = True

    if index != 0:
        if topRow[index - 1] != ".":
            tbr = True
        if bottomRow[index - 1] != ".":
            tbr = True

    if index != len(topRow) - 1:

        if topRow[index + 1] != ".":
            tbr = True

        if bottomRow[index + 1] != ".":
            tbr = True

    return tbr

def amountOfDigits(string):
    digits=0
    for i in string:
        if i!=".":
            digits+=1

    return digits

def check_for_numbers(topRow, index, bottomRow):
    first = 0
    second = 0
    tbr = False
    amountOfIntsInTop=amountOfDigits(topRow)
    amountOfIntsInBottom=amountOfDigits(bottomRow)

    indexOfTop=len(topRow)-amountOfIntsInTop
    indexOfBottom=len(bottomRow)-amountOfIntsInBottom
    if indexOfTop<0: indexOfTop=0
    if indexOfBottom<0: indexOfBottom=0

    topRowAsList=topRow.split(".")
    bottomRowAsList=bottomRow.split(".")
    print(topRowAsList[indexOfTop])
    print(bottomRowAsList)
    print(amountOfIntsInBottom)
    print(indexOfBottom)
   # print(bottomRowAsList[indexOfBottom])

    if index != len(topRow) - 1:
        if topRow[index + 1] == int:
            tbr = True
        if bottomRow[index + 1] == int:
            tbr = True

    if topRow[index] == int:
        tbr = True
    if bottomRow[index] == int:
        tbr = True



    if index != 0:
        if topRow[index - 1] == int:
            tbr = True
        if bottomRow[index - 1] == int:
            tbr = True



    return tbr


emptyLine = "............................................................................................................................................"
for i in range(len(lines)):
    d = dict((m.start(), (m.group())) for m in re.finditer(r'\*', lines[i]))
  #  print(d)
    if len(d) != 0:
        indices = list(d)
        for each in indices:
            addToSum = False

            if lines[i][each - 1] != ".": addToSum = True
            if each + len(str(d[each])) != len(lines[i]):
                if lines[i][each + len(str(d[each]))] != ".":
                    addToSum = True

            for ind in range(len(str(d[each]))):
                if i == 0:
                    if (check_for_numbers(emptyLine, each + ind, lines[i + 1])):
                        addToSum = True

                elif i == len(lines) - 1:
                    if (check_for_numbers(lines[i - 1], each + ind, emptyLine)):
                        addToSum = True


                else:
                    if (check_for_numbers(lines[i - 1], each + ind, lines[i + 1])):
                        addToSum = True

        # if addToSum:

        #  sum+=int(d[each])

print(sum)
