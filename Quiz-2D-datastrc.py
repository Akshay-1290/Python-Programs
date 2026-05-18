import time 
Questions = ("What is the capital of Japan?",
             "Which planet is known as the Red Planet?",
             "What is 12 times 8?",
             "Which gas do plants absorb from the atmosphere?")


Options = (('A-Seoul' ,'B-Tokyo','C-Beijing' ,'D-Donald J Trump'),
           ('A-Venus' ,'B-Jupiter','C-Mars' ,'D-America'),
           ('A-86' ,'B-96','C-92' ,'D-6 7'),
           ('A-Oxygen' ,'B-Nitrogen','C-Carbondioxide' ,'D-Crude oil'))
correct = 0
q = 0
answer = ["B","C","B","C"]
guess = []
score = 4

print ("\n")
print("-----Welcome to National Trustworthy Agency(NTA)-----")
time.sleep(2)

for Question in Questions :
    print("\n"+ Question)
    time.sleep(1)
    for Option in Options[q]:
     print(Option) 
     time.sleep(1)
    ans = input("Choose among option A,B,C,D \n :").upper()
    guess.append(ans)

    if ans == answer[q]:
      correct +=1
      time.sleep(2)
      print("\n7 crore ,Correct :")
      q+=1
      score += 4
    else:
      time.sleep(2)
      print("\nWrong.KO :")
      q+=1
      score -=1
    
time.sleep(1)   
print(f"{correct} Correct out of 4 question")
time.sleep(1)
print("___________________________________")
time.sleep(1)
print(f"Your total score is {score}")
time.sleep(1)
print("___________________________________")
time.sleep(1)
print(f"Your choosen option were {guess}")
time.sleep(1)
print("___________________________________")
time.sleep(1)
print(f"The correct answers are{answer}")
time.sleep(1)
print("___________________________________")
time.sleep(1)
print("4 EXTRA MARKS FOR TRUSTING NTA ")


      