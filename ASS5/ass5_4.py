''''
4.Write a recursive program which accept number from user and return
summation of its digits.
Input : 879
Output : 24
'''

def sumDigits(no):
    return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10))


no=int(input("Enter a number"))
print(sumDigits(no))