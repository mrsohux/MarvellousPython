'''
Write a program which display first 10 even numbers on screen.
Output : 2 4 6 8 10 12 14 16 18 20
'''

start, end =2, 20

def even():
    for i in range(start,end+1):
        if i%2 ==0:
            print(i,end=" ")

even()