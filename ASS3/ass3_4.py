''''
4.Write a program which accept N numbers from user and store it into List. Accept one another
number from user and return frequency of that number from List.
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3
'''
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

def frequency(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count

x =int(input("Element to search"))
print(frequency(lst, x))