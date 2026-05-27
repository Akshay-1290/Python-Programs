#only by using loop directories and all stuff if else all 
import random
num=[1,2,3,4,5,6,7,8,9]
def prntboard():
   print("___BOARD___")
   print(f"  {num[0]} | {num[1]} | {num[2]}")
   print("  --+---+--")
   print(f"  {num[3]} | {num[4]} | {num[5]}")
   print("  --+---+--")
   print(f"  {num[6]} | {num[7]} | {num[8]}")
   print()
prntboard()

def change_bd(place,sign):
 if num[place-1]=="X" or num[place-1]=="O":
      return False 
 num[place-1]=sign
 return True
      
    
def win_loss():
    pat = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
    for a,b,c in pat :
       if num[a]==num[b]==num[c]:
          if num[a]=="X":
           return "You won"
          if num[a]=="O":
             return "pc won"
    return 
def is_draw():
   for t in num:
      if t!="X" and t!="O":
         return False 
   return True
def comp_move():
    available = []

    for t in num:
        if t!= "X" and t!= "O":
            available.append(t)

    move = random.choice(available)
    change_bd(move, "O")

       

def main():
   print("You are X ")
   while True:
      prntboard()
      try:
         pos=int(input("Enter position bet (1-9) :"))
      except ValueError:
         print("Enter valid number :")
         continue
      if pos<1 or pos>9:
         print ("Enter number between 1-9 :")
         continue
      if not change_bd(pos,"X"):
         print("Are you blind or smth nga ? ")
         continue
      winner=win_loss()
      if winner:
         prntboard()
         print("You won")
         break
         
      if is_draw():
         prntboard()
         print("It was a draw")
         break
      comp_move()
      winner=win_loss()
    
      if win_loss():
         prntboard()
         print("Pc won")
         break
         
      if is_draw():
         prntboard()
         print("It was a draw")
         break

if __name__=="__main__":
 main() 