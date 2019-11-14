''''
1. Write a recursive program which display below pattern.
Input : 5
Output : * * * * *
'''

def fun(n):
    if n>0:
        print("*",end=" ")
        n=n-1
        fun(n)
x=int(input("Enter a Number"))
fun(x)