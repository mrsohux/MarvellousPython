'''''
Write a program which contains one class named as Circle.
Circle class contains three instance variables as Radius ,Area, Circumference.
That class contains one class variable as PI which is initialise to 3.14.
Inside init method initialise all instance variables to 0.0.
There are three instance methods inside class as Accept(), CalculateArea(),
CalculateCircumference(), Display().
Accept method will accept value of Radius from user.
CalculateArea() method will calculate area of circle and store it into instance variable Area.
CalculateCircumference() method will calculate circumference of circle and store it into instance
variable Circumference.
And Display() method will display value of all the instance variables as Radius , Area,
Circumference.
After designing the above class call all instance methods by creating multiple objects
'''

class Circle:
    PI=3.14
    def __init__(self):
        self.r=0.0
        self.a=0.0
        self.c=0.0
    def Accept(self):
        print("enter value of radius")
        self.r=float(input())
    def CalculateArea(self):
        self.a= self.PI* self.r**2
    def Calculatecircumference(self):
        self.c= self.PI*self.r*2
    def Display(self):
        print("area is:{0} \n circumference is:{1}".format(self.a,self.c))


def main():
    Obj1 = Circle()
    Obj2 = Circle()
    Obj3 = Circle()
    Obj4 = Circle()

    Obj1.Accept()
    Obj1.CalculateArea()
    Obj1.Calculatecircumference()
    Obj1.Display()

    Obj2.Accept()
    Obj2.CalculateArea()
    Obj2.Calculatecircumference()
    Obj2.Display()

    Obj3.Accept()
    Obj3.CalculateArea()
    Obj3.Calculatecircumference()
    Obj3.Display()

    Obj4.Accept()
    Obj4.CalculateArea()
    Obj4.Calculatecircumference()
    Obj4.Display()

if __name__=="__main__":
    main()