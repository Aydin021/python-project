def maxedge(a,b):
   '''
(integar),(integar) -> integar
this function, will give you the maximum edge of the triangle by give it the other edges.
'''
   Max=(a+b)-1
   return Max

a=int(input("enter the first edge:"))
b=int(input("enter the second edge:"))
if a<=0 or b<=0:
    print("ERROR")
else:
    print("the third and the maximum edge of the triangle is:", maxedge(a,b))
