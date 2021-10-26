ef almostIncreasingSequence(sequence):
    #Take out the edge cases
    if len(sequence) < 2:
        return True
    def listTest(sequence):
        for i in range(len(sequence)):
            if sequence[i] >= sequence[i+1]:
                return False

    for i, item in list(enumerate(sequence)):
        if sequence[i] >= sequence[i+1]:
            del sequence[i]
            if listTest(sequence) == True:
                return True
            else:
                return False
        


sequence = [1,3,2,4]


print(almostIncreasingSequence(sequence))
