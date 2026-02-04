import sys
Balance=100000
correct_pin=8076
wrong_pin=0
print("---- WELCOME ----")
while wrong_pin <3:
    Atm_pin=int(input("ENTER YOUR ATM PIN : "))
    print("-"*30)
    if (Atm_pin==correct_pin):
        print("Access Granted! ✅")
        print("-"*30)
        print("1.WITHDRAW")
        print("2.DEPOSITE")
        print("3.CHECK BALANCE")
        print("4.EXIT")
        print("="*30)
        while True:
            choice=int(input("ENTER YOUR CHOICE : "))
            print("-"*30)
            if (choice==1):
                while True:
                    print(" ----- Multiple of Note ----- ")
                    print(" 1.500 ")
                    print(" 2.200 ")
                    print(" 3.100 ")
                    print(" Enter 0 to Exixt ")
                    Amount=int(input("ENTER WITHDRAW AMOUNT : ₹"))
                    print("="*30)
                    if Amount==0:
                        print("1.WITHDRAW")
                        print("2.DEPOSITE")
                        print("3.CHECK BALANCE")
                        print("4.EXIT")
                        print("="*30)
                        break
                    if Amount % 100 != 0:
                        print(" PLEASE ENTER AMOUNT MULTIPLE OF NOTE ")
                        print("---- TRY AGAIN ----")
                        continue
                    elif Balance<Amount:
                        print(" TRANSACTION DECLINED ")
                        print("DUE TO LOW BALANCE")
                        print("---- TRY AGAIN ----")
                    else:
                        print("WITHDRAWAL : ",Amount)
                        Balance = Balance-Amount
                        print("="*30)
                        if Balance < 1000:
                            print(" ALERT : LOW BALANCE!")
                            print(" PLEASE DEPOSITE MONEY. ")
                            print("="*30)
                        print("1.WITHDRAW")
                        print("2.DEPOSITE")
                        print("3.CHECK BALANCE")
                        print("4.EXIT")
                        print("="*30)
                        break
            elif (choice==2):
                Deposite=int(input("ENTER DEPOSITE AMOUNT : ₹"))
                print("DEPOSITE : ",Deposite)
                Balance = Balance+Deposite
                print("="*30)
                print("1.WITHDRAW")
                print("2.DEPOSITE")
                print("3.CHECK BALANCE")
                print("4.EXIT")
                print("="*30)
            elif (choice==3):
                print("BANK BALANCE : ₹",Balance)
                print("="*30)
                print("1.WITHDRAW")
                print("2.DEPOSITE")
                print("3.CHECK BALANCE")
                print("4.EXIT")
                print("="*30)
            elif (choice==4):
                print("WITHDRAW NOW YOUR CARD")
                print("THANK YOU")
                print("-"*30)
                sys.exit()
            else:
                print("PLEASE ENTER NUMBER 1 TO 4  : ")
    else:
        wrong_pin+=1
        limits = 3 - wrong_pin
        if limits>0:
            print("PLEASE ENTER VALID ATM PIN.❌")
        else:
            print(" YOUR CARD HAS BEEN BLOCKED DUE TO 3 TIME WRONG PIN ATTEMPTS ")
            print(" YOUR CARD BLOCKED FOR 24 HOURS. ")
        
    
