'''
(integar) -> string
in this function, when you give the age of a person, the output of this code will be the class of the age.
'''
n=int(input(" enter the age:"))
if 0<n<=1:
    print ("Infant")
elif 1<n<13:
     print ("Child")
elif 13<=n<20:
    print ("Teenager")
else:
    print ("Adult")

