# first one this is for just basic arithmetic operationss
print("Enter the two numbers:")
x = float(input('Num 1 '))
y = float(input('Num 2 '))
print("Choose the Operation " \
"1=Addition" \
" 2=Subtration" \
" 3=Division" \
" 4=Multiplication" \
" 5=Power")
Opr = int(input("Operation"))

if Opr == 1 :
 print(f"The answer is {x+y}")
elif Opr == 2 :
 print(f"The answer is {x-y}")
elif Opr == 3:
 print(f"The answer is {x/y}")
elif Opr == 4 :
 print(f"The answer is {x*y}")
elif Opr == 5 :
 print(f"The answer is {x ** y}")
else :
 print("muehehehe")
