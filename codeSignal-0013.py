# input: string with or without nested letters in parenthesis
# output: string with parenthesis removed and any letters previously inside 
#         parenthesis reversed

def findIndices(s,c):
    """Takes the inputString, finds 'c', adds index to list and returns list"""
    lst = list()
    for index,item in enumerate(s):
        if item == c:
            lst.append(index)


def reverseInParentheses(inputString):
    if len(inputString) < 3: 
        return ''
    elif inputString.find('(') == -1:
        return inputString
    else:
    # get indexes of open and closing parenthesis in string
        openParIndexes = findIndices(inputString, '(')
        closeParIndexes = findIndices(inputString, ')')
        


inputString = "foo(bar)baz"
print(reverseInParentheses(inputString))

"""create empty stack list.
   for loop through inputString.
   iterate and append element to stack until ')' is found.
   while loop iterate from end of inputString, appending each time to  until reach '('.
   for item in tmp append to stack
   """