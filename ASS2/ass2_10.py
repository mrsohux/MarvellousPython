''''
10. Write a program which accept number from user and return addition of digits in that number.
Input : 5187934 Output : 37
'''

def add(x):
    j=0
    while x>0:
        j+=x%10
        x=x//10
    return j

x=int(input("enter a number"))
y=add(x)
print("Additiomn of digit",y)