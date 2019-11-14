'''
3. Write a program which contains one class named as Arithmetic.
Arithmetic class contains three instance variables as Value1 ,Value2.
Inside init method initialise all instance variables to 0.
There are three instance methods inside class as Accept(), Addition(), Subtraction(),
Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects.
'''

class Arithmatic:

    def __init__(self):
        self.value1=0
        self.value2=0
    def Accept(self):
        print("enter 1st number")
        self.value1=int(input())
        print("enter 2nd number")
        self.value2 = int(input())
    def Addition(self):
        return self.value1+self.value2
    def Subtraction(self):
        return self.value1-self.value2
    def multiplication(self):
        return self.value1*self.value2
    def division(self):
        return self.value1 / self.value2



def main():
    Obj1 = Arithmatic()
    Obj2 = Arithmatic()

    Obj1.Accept()
    print("Addition  is:{0} \n subtraction is:{1} \n multiplication is:{2} \n Division is:{3}".format(Obj1.Addition(),Obj1.Subtraction(),Obj1.multiplication(),Obj1.division()))

    Obj2.Accept()
    print("Addition  is:{0} \n subtraction is:{1} \n multiplication is:{2} \n Division is:{3}".format(Obj2.Addition(),Obj2.Subtraction(),Obj2.multiplication(),Obj2.division()))


if __name__=="__main__":
    main()