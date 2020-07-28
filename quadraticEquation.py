#Solve quadratic equation taking user input
import cmath
a = float(input("a ="))
b = float(input("b = "))
c = float(input("c = ")) 

d = (b**2) - (4*a*c)  
x1 = (-b+cmath.sqrt(d))/(2*a)
x2 = (-b-cmath.sqrt(d))/(2*a)  
print('the value of x1={0} and x2={1}'.format(x1,x2))