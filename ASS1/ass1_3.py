'''''
Write a program which contains one function named as Add() which accepts two numbers
from user and return addition of that two numbers.
Input : 11 5 Output : 16
'''

x = int(input("Enter First Number"))
y = int(input("Enter Second Number"))
def Add():
     sum =x+y
     print ("sum of {0} and {1} is {2}".format(x,y,sum))

if __name__=='__main__':
    Add()