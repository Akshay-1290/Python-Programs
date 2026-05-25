#center alligned palidrom rhombus
def pld(num=7):
 for t in range(1,num):
    print(" "*(num-t),end="")
    for k in range(1,t):
     print(k,end="")
    for k in range(t,0,-1):
     print(k,end="")
    print("")
 return ""

pld()

def ipld(num=7):
  for t in range(num,0,-1):
   print(" "*(num-t),end="")
   for k in range(1,t):
    print(k,end="")
   for k in range(t,0,-1):
    print(k,end="")
   print("")
  return ""

ipld()