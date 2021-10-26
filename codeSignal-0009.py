def allLongestStrings(inputArray):
    longest = 0
    lst = []
    if len(inputArray) == 1:
        return(inputArray)
    else:
        for word in inputArray:
            if len(word) > longest:
                longest = len(word)
        for word in inputArray:
            if len(word) == longest:
                lst.append(word)
        return(lst)

    
inputArray = ["aba","aa","ad","vcd","aba"]

print(allLongestStrings(inputArray))
