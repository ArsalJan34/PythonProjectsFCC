class BankAccount:
  # contructor method
  # parameters: self,owner_name, starting_balance
  def __init__(self,onwer_name, starting_balance):
    # attributes
    self.onwer = onwer_name
    self.balance = starting_balance

  # method 1 despositing money
  # parameter : amount
  def deposit(self,amount):
    self.balance += amount
    print(f"Deposited ${amount}. New balance: ${self.balance}")
  def withdraw(self,amount):
    if amount > self.balance:
      print(f"Declined! {self.owner} has insufficient funds")
    else:
      self.balance -= amount
      print(f"\n${amount}. Has been withdrawn. Remaining Balance is ${self.balance}")
      if amount > 1000:
        tax = 50
        self.balance -= tax
        print(f"\ntax ${tax} has been deducted for withdrawl.\n Remaining Balance is ${self.balance}. Thank for using atm")
      else:
        print("\nThank you for using atm")




sara_acc = BankAccount("Sara", 50000)
sara_acc.deposit(500)
sara_acc.withdraw(10000)
sara_acc.withdraw(5000)
