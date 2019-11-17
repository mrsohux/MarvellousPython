#
# 1.Design python application which creates two thread named as even and odd. Even
# thread will display first 10 even numbers and odd thread will display first 10 odd
# numbers.

import threading
from os import *

def even():
    for i in range(1,11):
        if i%2==0:
            print("even number is",i)
   
def odd():
    for i in range(1,10):
        if i%2!=0:
            print("odd number is",i)

if __name__ == "__main__":
    print("PID is",getpid())
    print("PPID is",getppid())

    t1 = threading.Thread(target=even, args=())
    t2 = threading.Thread(target=odd, args=())

    t1.start()
    t2.start()