import random
import time

def slot():
 sym=("🙂","😋","🤙","😮","👊")
 return [random.choice(sym) for _ in range(3)]

def check_slot(s,bet):
 if (s[0]==s[1] and s[0]!=s[2]) or (s[1]==s[2] and s[0]!=s[1]) or (s[0]==s[2] and s[0]!=s[1])  : 
   print(f"You won {bet*3}")
   return bet*3
 elif (s[0]==s[1] and s[1]==s[2]):
   print(f"You won {bet*5}")
   return bet*5
 else :
   print("You lost!! ")
   return 0

def main():
  bal = 100
  print("**************************")
  time.sleep(1)
  print("Welcome to Slot game")
  print("symbols-🙂😋🤙😮👊")
  time.sleep(1)
  print("**************************")
  time.sleep(3)
  print("You will win 3 times of your bet when two symbols comes out same and 5 times when all 3 symbols same")
  time.sleep(3)
  while bal>0:
   print(f"Your balance = {bal}")
   time.sleep(1)

   bet=(input("Enter your betting amount(Press Q to quit) :"))
   if bet.upper()=="Q":
    print("Game ended")
    break
   if not bet.isdigit():
    print("Enter a valid input :")
    continue
   bet=int(bet)
   if (bal-bet)<0 or bet<0:
    time.sleep(2)
    print("Cant proceed :error /betting amount cant be nagative or more than balance amount")
   if (bal-bet)>=0:
    bal -= bet
    slott = slot()
    win = check_slot(slott,bet)
    time.sleep(1)
    print(f"{slott},\n {win}")
    if win !="You lost!! ":
     bal+=win
  while bal==0:
   print("Game ended due to low balance")
   break
  
   
  
if __name__ == "__main__":
 main()