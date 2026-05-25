def rhombus(h):
 for t in range(1,h+2,2):
   k=(h-t+2)/2
   k=int(k)
   print(" "*k,"*"*t,end=" \n")
 for u in range(h-2,0,-2):
   k=((h-u)/2)+1
   k=int(k)
   print(" "*k,"*"*u,end=" \n")

print(rhombus(7))