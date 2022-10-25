'''
this code, will give you the day of the week
'''
n=int(input("enter the number:"))
if 1<=n<=7:
    if n == 1:
        print ("Saturday")
    elif n ==2:
        print ("Sunday")
    elif n == 3:
        print ("Monday")
    elif n == 4:
        print ("Tuesday")
    elif n == 5:
        print ("Wednesday")
    elif n == 6:
        print ("Thursday")
    else:
        print ("Friday")
else:
    print ("ERROR")
