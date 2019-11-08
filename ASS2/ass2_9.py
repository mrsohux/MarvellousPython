''''
9. Write a program which accept number from user and return number of digits in that number.
Input : 5187934 Output : 7
'''
def check(x):
    Count =0
    while (x>0):
        x =x//10
        Count=Count + 1
    print(" %d"%Count)
x=int(input("enter a number"))
check(x)