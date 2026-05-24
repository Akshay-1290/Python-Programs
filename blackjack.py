import random 
import time 
import msvcrt
card={ "A♠": 11, "2♠": 2, "3♠": 3, "4♠": 4, "5♠": 5, "6♠": 6, "7♠": 7,
    "8♠": 8, "9♠": 9, "10♠": 10, "J♠": 10, "Q♠": 10, "K♠": 10,

    "A♥": 11, "2♥": 2, "3♥": 3, "4♥": 4, "5♥": 5, "6♥": 6, "7♥": 7,
    "8♥": 8, "9♥": 9, "10♥": 10, "J♥": 10, "Q♥": 10, "K♥": 10,

    "A♦": 11, "2♦": 2, "3♦": 3, "4♦": 4, "5♦": 5, "6♦": 6, "7♦": 7,
    "8♦": 8, "9♦": 9, "10♦": 10, "J♦": 10, "Q♦": 10, "K♦": 10,

    "A♣": 11, "2♣": 2, "3♣": 3, "4♣": 4, "5♣": 5, "6♣": 6, "7♣": 7,
    "8♣": 8, "9♣": 9, "10♣": 10, "J♣": 10, "Q♣": 10, "K♣": 10
}
def show_instructions():
    print("\n" + "="*40)
    print("      🃏 BLACKJACK GAME 🃏")
    print("="*40)
    time.sleep(3)
    print("\n🎯 OBJECTIVE:")
    print("Get a total as close to 21 as possible")
    print("without going over 21.")
    time.sleep(1)
    print("\n💰 BETTING:")
    print("You start with a balance.")
    print("Place a bet before each round.")
    time.sleep(1)
    print("\n🃏 CARDS VALUE:")
    print("A = 11 or 1")
    print("2-10 = face value")
    print("J, Q, K = 10")
    time.sleep(1)
    print("\n🎮 GAME PLAY:")
    print("- You get 2 cards")
    print("- Dealer gets 2 cards (1 hidden)")
    print("- You choose: Hit (h) or Pass (p)")
    time.sleep(1)
    print("\n✋ ACTIONS:")
    print("Hit → take another card")
    print("Pass → stop drawing cards")
    time.sleep(1)
    print("\n💥 LOSS CONDITION:")
    print("If your total goes over 21 → BUST ❌")
    time.sleep(1)
    print("\n🏆 WIN CONDITION:")
    print("Beat dealer's total without busting")
    time.sleep(1)
    print("\n" + "="*40)
    print("Good luck! 🍀\n")
def draw_cards(i=1):
 
  return [random.choice(list(card.keys())) for _ in range(i)]
def hand_total(x):
 value=[card[c] for c in x ]
 ace=value.count(11)
 total=sum(card[c] for c in x )
 while total>21 and ace>0:
   total-=10
   ace-=1
 return total
def main():
  show_instructions()
  print("Press any key to continue...")
  msvcrt.getch()
  balance=1000
  while True:
    time.sleep(2)
    print(f"You have {balance} ruppess to bet :")
    time.sleep(1)
    bet = input("Enter bet: ")
    time.sleep(2)
    if not bet.isdigit():
     print("Please enter a valid number")
     time.sleep(1)
    elif int(bet) > balance:
     print("Not enough balance")
     time.sleep(1)
    elif int(bet) <= 0:
     print("Invalid bet")
     time.sleep(1)
    else:
     bet = int(bet)
     print("Bet accepted")
     time.sleep(1)
    play=input("Enter p to play or q to quit :")
    if play.lower()=="p":
     dc=draw_cards(2)
     print(dc)
     time.sleep(1)
     print([card[c] for c in dc])
     time.sleep(1)
     total=hand_total(dc)
     print(total)
     time.sleep(1)
     ddc=draw_cards()
     print(f"Dealer's card {ddc},?")
     time.sleep(1)
     ddc.append(draw_cards()[0])
     totald=hand_total(ddc)
     while total<21:
       replay=input("Hit(h) or pass(p)")
       if replay.lower()=="h":
         dc.append(draw_cards()[0])
         print(dc)
         time.sleep(1)
         print([card[c] for c in dc])
         time.sleep(1)
         total=hand_total(dc)
         print(total)
         time.sleep(1)
         if total>21:
           print("Dealer wins")
           time.sleep(1)
           print(f"{ddc},\n{totald}")
           time.sleep(1)
           balance-=bet
           print(f"Your new balance is {balance} " )
           time.sleep(1)
           print("BUSTEDD(sum cant be greater than 21)")
           time.sleep(1)
           break
       elif replay.lower()=="p":
         while totald<17:
           print("Dealer hits")
           time.sleep(1)
           ddc.append(draw_cards()[0])
           totald=hand_total(ddc)
           if totald>21:
             print("You won")
             time.sleep(1)
             print('Dealer busted')
             time.sleep(1)
             print(f"{ddc}, \n{totald}")
             time.sleep(1)
             balance+=bet
             print(f"Your new balance is {balance}")
             time.sleep(1)
             break
         if totald>=17 and totald<22:
           print("Dealer passes")
           time.sleep(1)
           print("Comparing")
           time.sleep(1)
           if totald>total:
            print(f"{ddc},\n{totald}")
            time.sleep(1)
            print("Dealer won")
            time.sleep(1)
            balance-=bet
            print(f"Your new balance is {balance} " )
            time.sleep(1)
            break
           elif totald<total:
            print(f"{ddc},\n{totald}")
            time.sleep(1)
            print("You wonnn")
            time.sleep(1)
            balance+=bet
            print(f"Your new balance is {balance} " )
            time.sleep(1)
            break
           else :
             print("It was a draw")
             time.sleep(1)
             break
       else:
         print("Please enter a valid input")
         time.sleep(1)


     if total<22 and total==totald:
      print(ddc)
      time.sleep(1)
      print("It was a draw")
      time.sleep(1)
      break
     if total==21 and total>totald:
       print("You wonn")
       time.sleep(1)
       balance+=bet
       print(f"Your new balance is {balance} " )
       time.sleep(1)
       break

    elif play.lower()=="q":
     print("Game ended")
     time.sleep(1)

     break
    else :
     print("Please enter a valid input")
     time.sleep(1)

     continue
  
if __name__=="__main__":
  main()