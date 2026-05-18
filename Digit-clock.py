import time
sec=int(input("Enter your time in seconds :"))
for tem in reversed(range(0,sec+1)):
 second = tem%60
 minute = int(second/60)%60
 hour = int(tem/3600)
 print(f"{hour:02}:{minute:02}:{second:02}")
 time.sleep(1)
print("time's up")