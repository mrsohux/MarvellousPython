'''
5.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
return Maximum number from that numbers. (You can also use normal functions instead of
lambda functions).
Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62
'''

from functools import reduce
def is_prime(num):
   for j in range(2, num):
      if num % j == 0:
         return False
   else:
      return True

def main():

    arr=[int(x) for x in input("enter space saperated numeric value").split()]

    pArr = list(filter(is_prime, arr))
    print(pArr)
    ModArray = list(map(lambda no: no*2, pArr))
    print(ModArray)
    sum = reduce(lambda x,y: x if x > y else y, ModArray)
    print(sum)


if __name__=='__main__':
    main();