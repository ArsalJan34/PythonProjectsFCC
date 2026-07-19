class BankAccount:
  def __init__(self,owner_name,starting_balace):
    self.onwer = owner_name
    self.balance = starting_balace

  def deposit(self,amount):
    self.balance += amount
    print(f"${amount} has been deposited in {self.onwer} account. new balance is {self.balance}")
  def withdraw(self,amount):
    if amount > self.balance:
      print(f"Declined: {self.onwer} has insufficient funds. ")
    else:
      self.balance -= amount
      print(f"An withdrawl of ${amount} has been made. Reamaing balance is {self.balance}")
      if amount > 1000:
        tax = 50
        self.balance -= tax
        print(f" Tax ${tax} has been deducted for large withdrawal.")
        print(f" Final Remaining Balance is ${self.balance}.\nThank you for using the ATM!")
      else:
        print("Thank you for usign ATM")

account_details = {
  "Sara" : BankAccount("Sara", 50000),
  "Tara" : BankAccount("Tara", 40000),
  "Ali" : BankAccount("Ali", 10000)
}
print("--------Welcome To MCB-----------")

username = input("Enter Your Name : ").capitalize().strip()

if username in account_details:
  current_account = account_details[username]
  print(f"\n Welcome Mr/Mrs.{current_account.onwer}!")
  print(f"\nYour current balance is: ${current_account.balance: .2f}")

  action = input("Do you want to (D)esposit or (W)ithdraw : ").upper()
  if action == "W":
    amount_to_get = float(input("Enter amount you want to withdraw: " ))
    current_account.withdraw(amount_to_get)
  elif action == "D":
    amount_to_add = float(input("Enter amount you want to deposit:  "))
    current_account.deposit(amount_to_add)
  else:
    print("Invalid option selected")
else:
  print(f"Error! Account name {username} not found in our database.")
