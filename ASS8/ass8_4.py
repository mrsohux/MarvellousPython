# 4.Design python application which creates three threads as small, capital, digits. All the
# threads accepts string as parameter. Small thread display number of small characters,
# capital thread display number of capital characters and digits thread display number of
# digits. Display id and name of each thread.
import threading

def small(str):
    small=[i for i in str if i.islower()]
    print("length of small letter is",len(small))
    print("small letters are",small)


def capital(str):
    capital=[i for i in str if i.isupper()]
    print("length of capital letter is",len(capital))
    print("Capital letters are",capital)

def digit(str):

    cnt=0

    for i in range(0,len(str)):
        if str[i].isdigit():
            cnt+=1
            print("Digits are", str[i])
    print("length of Digit",cnt)

if __name__ == "__main__":
    str=input("enter values")

    T = threading.Thread(target=small, args=(str,))
    T1 = threading.Thread(target=capital, args=(str,))
    T2 = threading.Thread(target=digit, args=(str,))

    T.start()
    T1.start()
    T2.start()
