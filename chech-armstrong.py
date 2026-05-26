def armstrg(num):
 dig=len(str(num))
 try:
   p=num
   total=0
   while (num/10)>0 :
    total+=(num%10)**(dig)
    num=int(num/10)
   if total == p:
    print("Your num is armstrg")
   else :
    print("This aint armstrg shii")
 except ValueError:
  print(f"{num} is invalid ")
 except TypeError:
  print('YOO enter nums only')
 
armstrg(153)
armstrg(154)
armstrg(9474)
armstrg("n")