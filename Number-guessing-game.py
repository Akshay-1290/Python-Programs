import random
d = int(input("Enter the difficulty you want to play \nEnter 1 for Easy \nEnter 2 for Medium \nEnter 3 for Hard \nOR enter 4 to exit game :"))
while d>4 or d<1:
    print("Please enter a valid input :")
    d = int(input("Enter the difficulty you want to play \nEnter 1 for Easy \nEnter 2 for Medium \nEnter 3 for Hard \nOR enter 4 to exit game :"))
if d==1:
   print("You have choosed Easy difficulty")
   r = random.randint(1,100)
   print(r)
   g = int(input("Guess the number between 1-100 :"))
   while g<1 or g>100:
     print("Choosed integer must lie between 1 and 100 :")
     g = int(input("Guess the number between 1-100 :"))
   while g != r:
     if (r-g)>75 and (r-g)<=99 :
       print("Number you guessed is very-very low")
       g = int(input("Guess the number between 1-100 :"))
     elif (g-r)>75 and (g-r)<=99:
       print("Number you guessed is very very high")
       g = int(input("Guess the number between 1-100 :"))
     elif (r-g)>50 and (r-g)<76 :
       print("Number you guessed is too low")
       g = int(input("Guess the number between 1-100 :"))
     elif (g-r)>50 and (g-r)<76 :
       print("Number you guessed is too high")
       g = int(input("Guess the number between 1-100 :"))
     elif(r-g)>25 and (r-g)<51:
       print("Number you guessed is low")
       g = int(input("Guess the number between 1-100 :"))
     elif (g-r)>25 and (g-r)<51:
       print("Number you guessed is high")
       g = int(input("Guess the number between 1-100 :"))
     elif(r-g)>10 and (r-g)<26:
       print("Close but low")
       g = int(input("Guess the number between 1-100 :"))
     elif (g-r)>10 and (g-r)<26:
       print("Close but high")
       g = int(input("Guess the number between 1-100 :"))
     elif(r-g)>0 and (r-g)<11:
       print("Extremly close but low")
       g = int(input("Guess the number between 1-100 :"))
     elif (g-r)>0 and (g-r)<11:
       print("Extremly close but high")
       g = int(input("Guess the number between 1-100 :"))
   else :
     print("You guessed it right")
       
