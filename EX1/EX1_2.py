def area(a,h):
    '''
(float)*(float) -> float
this function, will evaluate the area of the triangle by giving the base and the height.
'''
    A=(a*h)/2
    return A
a=float(input("enter the base of the triangle:"))
h= float(input("rnter the height of the triangle:"))
print("the area of the triangle is:", area(a,h))
