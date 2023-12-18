hands=open("txt").read().split("\n")

dictOfHandsAndBids={}
listOfHands=[]
for each in hands:
    var=each.split(" ")
    dictOfHandsAndBids.update({var[0]:var[1]})
    listOfHands.append(var[0])



symbols=["A","K", "Q", "J", "T", "9", "8","7", "6", "5", "4", "3","2"]

# hands are given values from 1 to 7 with 7 being the highest, meaning 5 of a kind.

def flatten_list(nested_list):
    flattened_list = []
    for element in nested_list:
        if isinstance(element, list):
            flattened_list.extend(flatten_list(element))
        else:
            flattened_list.append(element)
    return flattened_list

def checkHand(hand):
    hand="".join(sorted(hand))
    values=[1]
    for card in symbols:

        if card*5 in hand: values.append(7)
        if card*4 in hand: values.append(6)
        if card*3 in hand:
            subHand=hand.lstrip(card*3)
            if len(subHand) >= 2 and subHand[0] == subHand[1]:
                values.append(5)

            else:
               values.append(4)
        if card * 2 in hand:
            subHand2 = hand.lstrip(card * 2)
            if len(subHand2) >= 2 and (subHand2[0] == subHand2[1] or len(subHand2) >= 3 and (subHand2[0] == subHand2[2] or subHand2[1] == subHand2[2])):
                values.append(3)
            else:
                values.append(2)
    return max(values)

handValues={}
for hand in listOfHands:
    if checkHand(hand) in handValues.keys():
        handValues[checkHand(hand)].append(hand)
    else:
        handValues.update({checkHand((hand)):[hand]})
#print(handValues)


def replaceHandWithIndexes(hand):
    replacement=[]
    for each in hand:
        replacement.append(str(symbols.index(each)))
    return (replacement)

def compareSameValueHands(hands): #places lists in ascending order
    handsAsIndeces=[]
    joinedListToSortableListDict={}
    result=[]
    for each in hands:
        asIndeces=replaceHandWithIndexes(each)
        joinedListToSortableListDict.update({"".join(asIndeces):each})
        handsAsIndeces.append(asIndeces)
    handsAsIndeces.sort(reverse=True)

    for each in handsAsIndeces:
        result.append(joinedListToSortableListDict["".join(each)])
    return result

result=[]
handValuesAsKeys=[]



for handValueGroup in sorted(handValues.keys()):

    result.append(compareSameValueHands(handValues[handValueGroup]))
result=(flatten_list(result))
print(result)
sum=0
for i in range(len(result)):
    print("hand {}  place {}  as indeces {}".format(result[i],i+1,replaceHandWithIndexes(result[i])))
    sum+=(i+1)*int(dictOfHandsAndBids[result[i]])

print(sum)

