# 2.Design python application which creates two threads as evenfactor and oddfactor.
# Both the thread accept one parameter as integer. Evenfactor thread will display
# addition of even factors of given number and oddfactor will display addition of odd
# factors of given number. After execution of both the thread gets completed main
# thread should display message as “exit from main”.
import threading

def Evenfactor(X):
    sum=0
    for i in range(1,X):
        if X%i==0 and i%2==0:
            sum=sum+i
    print("Addition of even factor is",sum)

def Oddfactor(X):
    sum=0
    for i in range(1, X):
        if X % i == 0 and i % 2 != 0:
            sum = sum + i
    print("Addition of odd factor is",sum)


if __name__ == "__main__":
    X = int(input("enter a number"))
    T1 = threading.Thread(target=Evenfactor, args=(X,))
    T2 = threading.Thread(target=Oddfactor, args=(X,))

    T1.start()
    T2.start()

    print(" exit fom main.")