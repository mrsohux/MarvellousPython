''''
3.Write a recursive program which display below pattern.
Input : 5
Output : 5 4 3 2 1
'''

def fun(n):
    if n>0:
        print(n,end=" ")
        n=n-1
        fun(n)
x=int(input("Enter a Number"))
fun(x)