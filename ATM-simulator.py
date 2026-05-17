print("Secret...!!! Your pin is 159")

for attempt in range(3):
    pin = int(input("Enter your PIN: "))

    if pin == 159:
        print("Access Granted")
        Opr=int(input("Choose operation(1-3) 1=Balance check ,2=Deposit,3=Withdrawl :"))
        while Opr < 1 or Opr > 3 :
         print("Invalid operation")
         Opr=int(input("Choose operation(1-3) 1=Balance check ,2=Deposit,3=Withdrawl :"))
        if Opr == 1 :
         print("Your available balance in unavailable")
        elif Opr == 2 :
         print("Insufficient money found to deposit")
        else :
         print("Withdrawl successfull")
        break
    else:
        print("Re-try")
        print(f"Attempts left",2 -attempt)
else:
    print("Access Denied")
    
print("THANKYOU FOR USING OUR SERVICES")