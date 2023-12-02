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

file_path = 'txt_for_d1'
lines_list = read_lines_to_list(file_path)
sum=0
for i in lines_list:
    i=i.replace("one","o1ne")
    i=i.replace("two","t2wo")
    i=i.replace("three","thr3ee")
    i=i.replace("four","f4our")
    i=i.replace("five","fi5ve")
    i=i.replace("six","s6ix")
    i=i.replace("seven","se7ven")
    i=i.replace("eight","eig8ht")
    i=i.replace("nine","ni9ne")
    i=i.replace("zero","ze0ro")





    first=re.search(r'\d+',i).group()[0]
    last=re.search(r'\d+',i[::-1]).group()[0]
    sum+=int(first+last)
    print(i)


print(sum)