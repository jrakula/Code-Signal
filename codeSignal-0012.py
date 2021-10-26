def sortByHeight(a):
    treeIndex = list()
    heightList = list()
    for index, item in enumerate(a):
        if item == -1:
            treeIndex.append(index)
        else:
            heightList.append(item)
    heightList.sort()
    for i in treeIndex:
        heightList.insert(i, -1)
    return heightList


a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(a))
