#center alligned inverted palindrome number trangle
def ipld(num=7):
  for t in range(num,0,-1):
   print(" "*(num-t),end="")
   for k in range(1,t):
    print(k,end="")
   for k in range(t,0,-1):
    print(k,end="")
   print("")
  return ""

print(ipld())