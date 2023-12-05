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


lines=read_lines_to_list("txt")
sum=0

def check_for_symbol(topRow,index,bottomRow):
    tbr=False
    if topRow[index]!=".":
        tbr=True
    if bottomRow[index]!=".":
        tbr=True

    if index!=0:
        if topRow[index-1]!=".":
            tbr=True
        if bottomRow[index-1]!=".":
            tbr=True

    if index!=len(topRow)-1 :

        if topRow[index+1]!=".":
            tbr=True

        if bottomRow[index+1]!=".":
            tbr=True

    return tbr

emptyLine="............................................................................................................................................"
for i in range(len(lines)):
    d = dict((m.start(), int(m.group())) for m in re.finditer(r'\d+', lines[i]))

    if len(d)!=0:
        indices=list(d)
        for each in indices:
            addToSum=False

            if lines[i][each-1]!=".": addToSum=True
            if each+len(str(d[each]))!=len(lines[i]):
                if lines[i][each+len(str(d[each]))]!=".":
                    addToSum=True

            for ind in range(len(str(d[each]))):
                if i==0:
                    if (check_for_symbol(emptyLine,each+ind,lines[i+1])):
                        addToSum=True

                elif i==len(lines)-1:
                    if (check_for_symbol(lines[i-1],each+ind,emptyLine)):
                        addToSum=True


                else:
                    if (check_for_symbol(lines[i-1],each+ind,lines[i+1])):

                        addToSum=True


            if addToSum:

                sum+=d[each]

print(sum)
