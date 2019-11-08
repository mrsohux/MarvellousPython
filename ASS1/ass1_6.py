'''''
6.Write a program which accept number from user and check whether that number is positive or
negative or zero.
Input : 11 Output : Positive Number
Input : -8 Output : Negative Number
Input : 0 Output : Zero
'''''



def check(x):
    if x > 0:
        print("{0} is positive Number".format(x))
    elif x < 0:
        print("{0} is negative number".format(x))
    elif x == 0:
        print("{0} is always  zero".format(x))


x = (int(input("Enter the  number")))
check(x)