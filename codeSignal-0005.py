##find the area of a polygon
##1 => 1
##2 => 5
##3 => 13
##so on...

def shapeArea(n):
    area = n**2 + (n-1)*(n-1)
    return area

print(shapeArea(2))
