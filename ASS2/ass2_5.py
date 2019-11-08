''''
Write a program which accept one number for user and check whether number is prime or not.
Input : 5 Output : It is Prime Number
'''

def check(x):
    if x>1:
        for i in range(2,x):
            if(x%2)==0:
                print(x,"is not a prime number")
                break
        else:
            print(x,"is prime Number")
    else:
        print("It is not prime number")



x=int(input("enter a number"))
check(x)