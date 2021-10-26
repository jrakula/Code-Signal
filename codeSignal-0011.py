def isLucky(n):
    count1 = 0
    count2 = 0
    stringNum = str(n)
    if len(stringNum) % 2 != 0:
        return False
    else:
        firstHalf = stringNum[:len(stringNum)//2]
        secondHalf = stringNum[len(stringNum)//2:]
    for i in firstHalf:
        count1 += int(i)
    for i in secondHalf:
        count2 += int(i)
    if count1 == count2:
        return True
    else:
        return False
    



n = 134008
print(isLucky(n))
