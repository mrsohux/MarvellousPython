
''''
4.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which are even. Map function will calculate its square.
Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204
'''
from functools import reduce

def main():

    arr=[int(x) for x in input("enter space saperated numeric value").split()]

    evenArr = list(filter(lambda no:  no%2==0, arr))
    print(evenArr)

    ModArray = list(map(lambda no: no**2, evenArr))
    print(ModArray)
    sum = reduce(lambda a, b: a + b, ModArray)
    print(sum)


if __name__=='__main__':
    main();