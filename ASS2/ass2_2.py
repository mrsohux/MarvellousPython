'''''
2. Write a program which accept one number and display below pattern.
Input : 5
Output : * * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

def disp(x):
    for i in range(x):
        for j in range(x):
            print("*",end=" ")
        print("\n")


x=int(input("Enter a Number"))
disp(x)
