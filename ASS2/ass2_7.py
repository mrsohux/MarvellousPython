'''''
Write a program which accept one number and display below pattern.
Input : 5
Output : 1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''



def disp(x):
    for i in range(x):
        j=1
        while j<=x:
            print(j,end=" ")
            j+=1
        print("\n")

x=int(input("enter a number"))
disp(x)