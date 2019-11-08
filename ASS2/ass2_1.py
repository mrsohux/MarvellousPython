'''''
1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the
functions from Arithmetic module by accepting the parameters from user.
'''

import Arithmetic

x=int(input("Enter 1st Number"))
y=int(input("Enter 2nd Number"))

print("Addition is",Arithmetic.Add(x,y))
print("Subtraction is",Arithmetic.sub(x,y))
print("Multiplication is",Arithmetic.mult(x,y))
print("Division is",Arithmetic.div(x,y))
