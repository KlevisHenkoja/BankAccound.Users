from bankAccoundt import BankAccount
class User:
    def __init__(self,name):
        self.name=name
        self.account={
            "checking": BankAccount(0.1,1000),
            "saving": BankAccount(0.5,100)
        }
    def print_balance(self):
        print(f"savings balanc is {self.account['saving'].balance} and Checking is {self.account['checking'].balance} ")

    def trransfert(self,account2,amount):
        self.account["checking"].withdraw(amount)
        account2.account["checking"].deposit(amount)
        return self

account1=User("Klevis")
account2=User("John")
account1.trransfert(account2,3).print_balance()
