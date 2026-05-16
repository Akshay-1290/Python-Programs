# To solve Pair of linear equation in two variable 
#only for single digit cofficients according to my current knowledge
Eq1 = input("Enter the first equation in the format (+or-)ax(+or-)by(+or-)c=0 :")
Eq2 = input("Enter the second equation in the format (+or-)ax(+or-)by(+or-)c=0 :")
a1 = int(Eq1[1])
a2 = int(Eq2[1])
b1 = int(Eq1[4])
b2 = int(Eq2[4])
c1 = int(Eq1[7])
c2 = int(Eq2[7])
if Eq1[0] == "-":
 a1 = -a1 
else :
 a1 
if Eq1[3] == "-":
 b1=-b1
else :
 b1
if Eq1[6] == "-":
 c1=-c1
else:
 c1
if Eq2[0] == "-":
 a2=-a2
else:
 a2
if Eq2[3] == "-":
 b2=-b2
else:
 b2
if Eq2[6] ==  "-":
 c2=-c2
else :
 c2
det = (a1*b2)-(a2*b1)

if det == 0:
 print("No unique solution")
else:
 x = (b1*c2)-(b2*c1)/det
 y = (c1*a2)-(c2*a1)/det
 print(f"x=",x)
 print(f"y=",y)