
''''
5.Write a program which accept N numbers from user and store it into List. Return addition of all
prime numbers from that List. Main python file accepts N numbers from user and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum. Name of the function from main python file should be ListPrime().
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 32 (13 + 5 + 7 +2 + 5)
'''
from MarvellousNum import *
def listprime(num):
    lst = []
    for n in range(1,num+1):
        numbers = int(input('Enter Input number '))
        lst.append(numbers)
    print("list is",lst)
    ChkPrime(lst)

num=int(input("Number of Elements"))
listprime(num)
