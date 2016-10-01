def remove_duplicates(uInput):
    newList = []
    for i in uInput:
        if i not in newList:
            newList.append(i)
    return newList

print remove_duplicates([1,2,3,4,5,5,6,6,6,6,7])