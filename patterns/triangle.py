def triange(h):
 for t in range(1,h+2,2):
  k=(h-t+2)/2
  k=int(k)
  print(" "*k,"*"*t,end=" \n")

print(triange(7))