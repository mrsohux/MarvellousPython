'''
Write a recursive program which display below pattern.
Input : 5
Output : 1 2 3 4 5
'''
def fun(no):
    if no>=1:

        no = no - 1
        fun(no)
        print(no, end=" ")
def main():

    val=int(input("Enter a Number"))
    fun(val)
    print(" ")

if __name__=="__main__":
    main()
