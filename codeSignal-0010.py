def commonCharacterCount(s1,s2):
    list1 = list()
    list2 = list()
    count = 0
    for letter in s1:
        list1.append(letter)
    for letter in s2:
        list2.append(letter)
    for i in list1:
        if i in list2:
            count += 1
            list2.remove(i)
    return count

s1 = "aabcc"
s2 = "adcaa"

print(commonCharacterCount(s1,s2))
