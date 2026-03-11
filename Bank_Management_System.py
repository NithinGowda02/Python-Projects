class Account:
    next_id = 1

    def __init__(self, name, balance):
        self.account_id = Account.next_id
        Account.next_id += 1
        self.name = name
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount 
        print("Amount Deposited Successfully.")   
        
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print("Withdrawal Successfull..")
        else:
            print("Insufficient Balance.!")

    def check_balance(self):
        print(f"Bank Balance : {self._balance}")


    def display_account(self):
        print("**********************************")
        print("\t ACCOUNT DETAILS \t")
        print("**********************************")
        print(f"Account ID : {self.account_id}\nName : {self.name}\nBank Balance : {self._balance}") 
        print("**********************************")

class Savings_Account(Account):
    def __init__(self, name, balance, interest_rate = 4):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self._balance * self.interest_rate / 100 
        self._balance += interest   
    
class Current_Account(Account):
    def __init__(self, name, balance, overdraft_limit = 10000):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self._balance + self.overdraft_limit >= amount:
            self._balance -= amount
            print("Withdrawal Successfull..")
        else:
            print("Overdraft limit Exceeds.!")
    
        
class Bank_System:
    def __init__(self):
        self.accounts = []

    def Savings_Account(self):
        name = input("Enter Account Holder Name : ")
        balance = float(input("Enter the Initial Balance : "))
        account = Savings_Account(name, balance)
        self.accounts.append(account)
        print("Savings Account Created Successfully.")

    def Current_Account(self):
        name = input("Enter Account Holder Name : ")
        balance = float(input("Enter the Initial Balance : "))
        account = Current_Account(name, balance)
        self.accounts.append(account)
        print("Current Account Created Successfully.")    
        
    def find_account(self, account_id):
        for acc in self.accounts:
            if acc.account_id == account_id:
                return acc
        return None
        
    def deposit_Money(self):
        account_id = int(input("Enter your Account ID : "))
        amount = float(input("Enter the Amount to Deposit : "))
        acc = self.find_account(account_id)
        if acc:
            acc.deposit(amount)
        else:
            print("Account Not Found") 

    def show_balance(self):
        account_id = int(input("Enter your Account ID : "))
        acc = self.find_account(account_id)
        if acc:
            acc.check_balance()
        else:
            print("Account Not Found")

    def calculate_interest(self):
        for acc in self.accounts:
            if isinstance(acc, Savings_Account):
                acc.calculate_interest()
                print(f"Interest calculated for account {acc.account_id}")


    def withdraw_Money(self):
        account_id = int(input("Enter your Account ID : "))
        amount = float(input("Enter the Amount to Withdraw : "))
        acc = self.find_account(account_id)
        if acc:
            acc.withdraw(amount)
        else:
            print("Account Not Found")        

    def show_account(self):
        if len(self.accounts) == 0:
            print("No Accounts Found") 
        else:
            for acc in self.accounts:
                acc.display_account()   

def main():
    bank = Bank_System()
    while True:
        print("============================================================")
        print("\t BANK MANAGEMENT SYSTEM \t")
        print("============================================================")
        print("1: Create Savings Account")
        print("2: Create Current Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Show Accounts")
        print("6. Check Balance")
        print("7. Calculate Interest")
        print("8. Exit")

        choice = int(input("Enter your Choice : "))

        if choice == 1:
            bank.Savings_Account()

        elif choice == 2:
            bank.Current_Account()

        elif choice == 3:
            bank.deposit_Money()

        elif choice == 4:
            bank.withdraw_Money()

        elif choice == 5:
            bank.show_account()

        elif choice == 6:
            bank.show_balance()

        elif choice == 7:
            bank.calculate_interest()

        elif choice == 8:
            print("Thank you!") 
            break       
                
        else:
            print("Invalid Choice") 

if __name__ == "__main__":
    main()

    



        