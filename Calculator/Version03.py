#quadratic quation 
a = float(input("Enter value of a with sign :"))
b = float(input("Enter value of b with sign :"))
c = float(input("Enter value of c with sign :"))
D = (b**2-4*a*c) 
r1 = (-b+D**0.5)/2*a
r2= (-b-D**0.5)/2*a 

if D<0 : 
    print("No real solution")
else: 
   
 print("Roots are ",{r1})
 print(r2)