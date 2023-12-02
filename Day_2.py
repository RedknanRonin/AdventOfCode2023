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

lines=read_lines_to_list("txt_for_d2")
sum=0
for each in lines:
    collector=bool
    game_number=re.search(r'\d+',each).group()

    cleaned=re.sub(r'^.*?:', ':',each )
    cubes_by_comma=cleaned.split(",")
    cubes=[]
    for each in cubes_by_comma:
        cubes+=each.split(";")

    cubes_required=[0,0,0] #red,blue,green
    for i in cubes:

        if "red" in i:
            if int(re.search(r'\d+',i).group())>cubes_required[0]:
                cubes_required[0]=int(re.search(r'\d+',i).group())
        elif "blue" in i:
            if int(re.search(r'\d+',i).group())>cubes_required[1]:
                cubes_required[1]=int(re.search(r'\d+',i).group())
        elif "green" in i:
            if int(re.search(r'\d+',i).group())>cubes_required[2]:
                cubes_required[2]=int(re.search(r'\d+',i).group())

   # if collector:
#        sum+=int(game_number)

    power=1
    for  i in cubes_required:
        power=i*power


    sum+=int(power)

print(sum)

