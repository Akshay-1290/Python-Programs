def pld(num=7):
 for t in range (1,num):
   for a in range(1,t):
    print(f"{a}",end="")
   for b in range(t,0,-1):
    print(b,end="")
   print("")
 return ""
print(pld())