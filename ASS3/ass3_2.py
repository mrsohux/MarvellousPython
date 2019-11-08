"""""
2.Write a program which accept N numbers from user and store it into List. Return Maximum
number from that List.
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56
"""

list1 = []

num = int(input("Enter number of elements in list: "))
for i in range(1, num + 1):

    ele = int(input("Enter elements: "))
    list1.append(ele)

print("Largest element is:", max(list1))
