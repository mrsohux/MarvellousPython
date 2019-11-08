'''
6. Write a program which accept one number and display below pattern.
Input : 5
* * * * *
* * * *
* * *
* *
*
'''

def disp(x):
    for i in range(x):
        j=i+1
        while j<=x:
            print("*",end=" ")
            j+=1
        print("\n")



x=int(input("Enter a number"))
disp(x)
