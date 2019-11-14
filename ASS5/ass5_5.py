'''
5. Write a recursive program which accept number from user and return its
factorial.
Input : 5
Output : 120
'''
def fact(n):
    if(n==1):
        return n
    else:
        return (n*fact(n-1))
def main():
    X=int(input("enter number"))
    print("factorial is",fact(X))
if __name__=="__main__":
    main()