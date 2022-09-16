import random

class ATM:
    def __init__(self, acc_num, name,  balance = 0):
        self.acc_num = acc_num
        self.name = name
        self.balance = balance
    
    #method
    # Check account details 
    def acc_details(self):
        print(f"------Account Detail------\
        \n Account Holder: {self.name}\
        \n Account Number: {self.acc_num}\
        \n Available balance: {self.balance} THB.")

    # Check balance
    def balance_check(self):
          print(f"------ Your balance ------\n Account Number : {self.acc_num} \n Available balance: {self.balance} THB.")

    # Deposit
    def deposit(self, dep_amount):
        self.balance += dep_amount
        print(f"::::: Deposit Successful ::::: \nCurrent account balance : {self.balance} THB.")

    # Withdraw
    def withdraw(self, with_amount):
        if with_amount > self.balance:
            print("Insufficient fund!")
            print("Try with lesser amount than balance.")
        else:
            self.balance -= with_amount
            print(f"----- Withdraw Successful-----\n Current account balance : {self.balance} THB.")


    def transaction(self):
            print("""
                TRANSACTION 
            *********************
                Menu:
                1. Account Details
                2. Check Balance
                3. Deposit
                4. Withdraw
                5. Exit
            *********************
            """)
            
            while True:
                try:
                    option = int(input("Enter 1, 2, 3, 4, 5: "))
                except:
                    print("Error: Enter 1, 2, 3, 4, 5  only!\n")
                    continue
                else:
                    if option == 1:
                        ATM.acc_details()
                    elif option == 2:
                        ATM.balance_check()
                    elif option == 3:
                        amount = int(input("How much you want to deposit(THB.):"))
                        ATM.deposit(amount)
                    elif option == 4:
                        amount = int(input("How much you want to withdraw(THB.):"))
                        ATM.withdraw(amount)
                    elif option == 5:
                        print(f"""
                    printing receipt..............
            ------------------------------------------
                Transaction is now complete.                         
                Transaction number: {random.randint(10000, 1000000)} 
                Account holder: {self.name.upper()}                  
                Account number: {self.acc_num}                
                Available balance: THB.{self.balance}                    
    
                Thanks for choosing us as your bank
            ------------------------------------------                      
            """)
                        break
print("-------WELCOME TO BANK OF ANONYMOUS-------")
print("___________________________________________________________\n")
print("----------ACCOUNT CREATION----------")
name = input("Enter your name: ")
acc_num = input("Enter your account number: ")
print("Congratulations! Account created successfully......\n")

ATM = ATM(name, acc_num)

while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        ATM.transaction()
    elif trans == "n":
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
    -------------------------------------
        """)
        break
    else:

        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")
