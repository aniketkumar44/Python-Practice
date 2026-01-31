Balance=100000
correct_pin=8076
print("***** WELCOME *****")
while True:
     Atm_pin= int(input("Enter your PIN: "))
     if correct_pin==Atm_pin:
        print("Bank Balance : ", Balance)
        break
     else:
         print("Wrong PIN! Try Again.")
