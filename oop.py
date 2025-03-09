#A class that handles an account that allows depositing, withdrawing, and viewing account blance
class Account:
    #initializing the class and its attributes
    def __init__(self, account_number: str, account_balance: float, account_holder: str):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder


    def deposit(self, amount: float):
        # Validate that the deposit amount is non-negative
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self.account_balance += amount
        print(f"{amount} has been deposited into your account.")
        print(f"Your new account balance is {self.account_balance}.\n")



    def withdraw(self, amount: float):
        # Validate that the withdrawal amount is non-negative
        if amount < 0:
            raise ValueError("Withdrawal amount must be non-negative.")
        # Check if there are sufficient funds to perform the withdrawal
        if amount > self.account_balance:
            print("You don't have sufficient funds to make this withdrawal.")
        else:
            self.account_balance -= amount
            print(f"{amount} has been withdrawn from your account.")
            print(f"Your new account balance is {self.account_balance}.\n")



    def check_balance(self) -> float:
        # Return the current account balance
        return self.account_balance



    # def menu(self):
    #     while True:
    #         print("\nHello. What would you like to do: ")
    #         print("1. Deposit")
    #         print("2. Withdraw")
    #         print("3. Chcek balance")
    #         print("4. Exit")

    #         choice = input("Enter your choice: ")

    #         if choice == '1':
    #             self.deposit()
    #         elif choice == '2':
    #             self.withdraw()
    #         elif choice == '3':
    #             self.check_balance()
    #         elif choice == '4':
    #             print('Exiting the program')
    #             break
    #         else:
    #             print("Invalid choice. Please try again.")





# create an instance of the class

my_account = Account("123456", 100.0, "John Doe")
my_account.deposit(50.0)   
my_account.withdraw(20.0) 
print("Current Balance:", my_account.check_balance())


my_account = Account("7891011", 50.0, "Jane Coffee")
my_account.withdraw(70.0) 
print("Current Balance:", my_account.check_balance())
