# 5.Design python application which contains two threads named as thread1 and thread2.
# Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
# screen. After execution of thread1 gets completed then schedule thread2
import threading

def ascending ():
    for i in range(51):
        print(i)
def descending ():
    for i in range(50,-1,-1):
        print(i)

if __name__ == "__main__":

    thread1 = threading.Thread(target=ascending , args=())
    thread2 = threading.Thread(target=descending , args=())
    print("ascending order of numbers are in below")
    thread1.start()
    thread1.join()
    print("Reverser order of numbers are in below")
    thread2.start()