##Given an array of integers, find the pair of adjacent elements
##that has the largest product and return that product.

def adjacentElementsProduct(inputArray):
    largestProduct = -1000000000
    for i in range(0, len(inputArray) - 1):
        if inputArray[i] * inputArray[i+1] > largestProduct:
            largestProduct = inputArray[i] * inputArray[i+1]
    return largestProduct

print(adjacentElementsProduct([1,2,3,4,5,6]))
