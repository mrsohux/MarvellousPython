''''
2.Write a program which contains one lambda function which accepts two parameters and return
its multiplication.
Input : 4 3 Output : 12
Input : 6 3 Output : 18
'''
s = lambda no1,no2 : no1*no2


def main():
    value1=int(input("enter first number"))
    value2 = int(input("enter second number"))
    result = s(value1,value2)
    print(result)

if __name__=='__main__':
    main();
