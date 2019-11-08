'''''
Write a program which accept number from user and print that number of “*” on screen.
Input : 5 Output : * * * * *
'''

def pattern(x):
    for i in range(x):
        print("*",end=" ")


x=int(input("How many time you want to print *"))
pattern(x)