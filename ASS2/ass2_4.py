'''''
4.Write a program which accept one number form user and return addition of its factors.
Input : 12 Output : 16 (1+2+3+4+6)
'''

def acc(x):
    i = 1
    sum = 0
    while x > i:
        if x % i == 0:
            sum = sum + i
        i = i + 1
    return sum


x=int(input("Enter A Number"))
print(" ",acc(x))
