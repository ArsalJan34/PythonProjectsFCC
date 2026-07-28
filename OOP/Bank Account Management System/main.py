class BankAccount:
  def __init__(self, account_holder: str, initial_balance: float):
    self.account_holder = account_holder
    self.__balance = initial_balance

  def deposit(self,amount: float) ->None:
    if amount > 0:
      self.__balance += amount
      print(f"Successfully desposited ${amount:.2f}")
    else:
      print("Error: Deposit amount should be greater than 0")
  def withdraw(self,amount: float) -> None:
      if amount <= 0:
        print("Error the withdraw amount shoulde be greater than 0")
      elif self.__balance < amount:
        print(f"Your account balance is less than ${amount:.2f} ")
      else:
        self.__balance -= amount
        print(f"Successfully Withdrawn: ${amount:.2f}. \n Remaining Balance is: ${self.__balance:.2f} ")
  def get_balance(self) -> float:
    return self.__balance

  def displayAccount(self) -> None:
    print("-" * 35)
    print(f"Account Holder: {self.account_holder}")
    print(f"Current Balance: ${self.__balance:.2f}")
    print("-" * 35)

if __name__ == "__main__":
    my_account = BankAccount(account_holder="Arsal", initial_balance=500000.0)
    my_account.displayAccount()

    my_account.deposit(500.0)
    my_account.withdraw(10000.0)

    print(f"Updated Balance: ${my_account.get_balance():.2f}")

    my_account.withdraw(1000.0)
    my_account.deposit(40000.0)

    my_account.displayAccount()
