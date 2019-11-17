# 3.Design python application which creates two threads as evenlist and oddlist. Both the
# threads accept list of integers as parameter. Evenlist thread add all even elements
# from input list and display the addition. Oddlist thread add all odd elements from input
# list and display the addition.

import threading

def evenlist(num):
    num=list(num)
    sum=0
    for i in range(len(num)):
        if  num[i]%2==0:
            sum=sum+num[i]
    print("even",sum)

def oddlist(num):
    num = list(num)
    sum=0
    for i in range(len(num)):
        if num[i] % 2 != 0:
            sum = sum + num[i]
    print("odd",sum)
if __name__ == "__main__":
    num = [int(x) for x in input("enter numbers separated by space ").split()]
    T1 = threading.Thread(target=evenlist, args=(num,))
    T2 = threading.Thread(target=oddlist, args=(num,))

    T1.start()
    T2.start()
