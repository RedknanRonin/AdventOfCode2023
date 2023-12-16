import re
from itertools import groupby



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

def Merge(dict1, dict2):
	res = dict1 | dict2
	return res

def getRanges(destinationRangeStart,sourceRangeStart,rangeLength):
    dict={}
    for i in range((rangeLength)):
        dict.update({int(sourceRangeStart+i):int(destinationRangeStart+i)})
    return dict




seedRow=lines.pop(0)
seeds=seedRow.split(" ")
seeds.pop(0)
print(seeds)

dictOfDicts={}
#in order of
# seed-to-soil, soil-to-fertilizer, fertilizer-to-water
#water-to-light, light-to-temperature, temperature-to-humidity, humidity-to-location

maps=[list(group) for k, group in groupby(lines,lambda x: x == "") if not k]
count=0
for each in maps:
    each.pop(0)
    for values in each:
        singleValue=values.split(" ")
        new=(getRanges(int(singleValue[0]),int(singleValue[1]),int(singleValue[2])))
        if count in dictOfDicts:
            dictOfDicts[count]=Merge(new,   dictOfDicts[count])
        else:
            dictOfDicts.update({count:new})
            #there are more than two rows, now it just replaces
    count+=1



#print(dictOfDicts)

def getNextValue(row,previousvalue):
    if previousvalue not in row:

        return previousvalue
    else:
      #  print("old:{}  new: {} ".format(previousvalue,row[previousvalue]))
        return row[previousvalue]

endSeed=[]

for each in (seeds):
    print("uere")
    previous=int(each)
    for i in dictOfDicts.keys():
        previous: object=getNextValue(dictOfDicts[i],previous)
      #  print("previous: {}".format(previous))

     #   print(("seed: {} current: {}".format(each,previous)))

        if i==len(dictOfDicts.keys())-1:
            print("working")
            endSeed.append(previous)


print(min(endSeed))

#this whole thing is uhhh, quite computationally expensive, needs rework