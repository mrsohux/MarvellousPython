'''
Write a program which contains one function named as ChkNum() which accept one
parameter as number. If number is even then it should display “Even number” otherwise
display “Odd number” on console.
Input : 11 Output : Odd Number
Input : 8 Output : Even Number
'''

def chkNum():

    i=int(input("Enter Number"))
    if (i%2) == 0:
        print("{0} is Even Number".format(i))
    else:
        print("{0} is Odd Number".format(i))
if __name__=='__main__':
    chkNum()
