''''
3. Write a program which accept one number from user and return its factorial.
Input : 5 Output : 120
'''

def fact(n):
    i=1
    while n>0:
              i=i*n
              n=n-1
    return i



n=int(input("Enter a Number"))
print(" ",fact(n))