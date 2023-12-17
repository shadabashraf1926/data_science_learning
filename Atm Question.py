class Atm:
    # constructor
    
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
        
    def menu(self):
        user_input =input( '''
                 How would you like to proceed?
                 1. Enter 1 to create pin.
                 2. Enter 2 to deposite.
                 3. Enter 3 to withdraw.
                 4. Enter 4 to check balance.
                 5. Enter 5 to exit.
                
    ''')
        if user_input == "1" :
            self.create_pin()
        elif user_input == "2" :
            self.deposite_amount()
        elif user_input == "3" :
            self.withdraw_amount()
        elif user_input == "4" :
            self.check_balance()
        else:
            print("Good Bye")
            
            
    def create_pin(self):
        self.pin = int(input("Enter your pin:-"))
        print("Pin created successfully")
        
    def deposite_amount(self):
        check_pin = int(input("Enter your pin:-"))
        if check_pin == self.pin:
            amount = int(input("Enter your amount:-"))
            self.balance = self.balance + amount
            print("Amount deposited succeessfully")
            
        else:
            print("Incorrect pin")
            
            
    def withdraw_amount(self):
        check_pin = input("Enter your pin:-")
        if check_pin == self.pin:
                amount = int(input("Enter your amount:-"))
                if amount <= self.balance:
                    self.balance = self.balance - amount
                    print("Amount withdrawn successfully")
                    
                else:
                    print("insufficient funds")
                    
        else:
                print("Incorrect pin")
        
    def check_balance(self):
        check_pin = input("Enter your pin:-")
        if check_pin == self.pin:
            print(self.balance)
            
        else:
            print("Incorrect pin")
            

hdfc = Atm()  
    