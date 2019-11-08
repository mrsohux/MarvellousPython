'''''

1.Write a program which contains one lambda function which accepts one parameter and return
power of two.
Input : 4 Output : 16
Input : 6 Output : 64
'''

fp = lambda no1 : no1**2


def main():
    value1=int(input("enter 1 no"))
    ret = fp(value1)
    print(ret)

if __name__=='__main__':
    main();