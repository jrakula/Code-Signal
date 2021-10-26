##input:  array of distinct non-negative integers
##output: minimum number of statues needed to have one of
##        every size between min(array) and max(array) incremented by 1 

##def makeArrayConsecutive2(statues):
##    lst = []
##    for i in range(min(statues),max(statues)):
##        if i not in statues:
##            lst.append(1)
##    return(sum(lst))

def makeArrayConsecutive2(statues):
    statues.sort()
    largest = statues[-1]
    smallest = statues[0]
    middle = largest - smallest
    missing = middle - len(statues) + 1
    return(missing)
    
    

print(makeArrayConsecutive2([6, 2, 3, 8]))
