''''
3.Write a program which accept N numbers from user and store it into List. Return Minimum
number from that List.
Input : Number of elements : 4
Input Elements : 13 5 45 7
Output : 5
'''
list1 = []

num = int(input("Enter number of elements in list: "))
for i in range(num):

    ele = int(input("Enter elements: "))
    list1.append(ele)

print("small element is:", min(list1))
