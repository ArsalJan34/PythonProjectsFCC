class BankAccount:
  def __init__(self,owner_name,starting_balance):
    self.owner = owner_name
    self.balance = starting_balance
  def deposit(self,amount):
    self.balance += amount
    print(f"Desposited ${amount}. New Balance is : ${self.balance}")
  def withdraw(self,amount):
    if amount > self.balance:
      print(f"\n Declined! {self.owner} has insufficient funds !")
    else:
      self.balance -= amount
      print(f"\n ${amount} has been withdrawn . Your remaining balance is {self.balance}")
      if amount > 1000:
        tax = 50
        self.balance -= tax
        print(f"${tax} has been deducted. Remaining Balance is ${self.balance}")
      else:
        print("\n Thank you for using ATM!")

accounts_database = {
    "Sara": BankAccount("Sara", 50000),
    "John": BankAccount("John", 1200)
}
while True:
  print("\n------ Welcome to The Blue Bank Atm -----------")
  print("1. Use Existing Account")
  print('2. Create an new account')
  print(' 3 Exit')

  choice = input("Please select an option (1 or 2 or 3 )")

  if choice == "2":
    new_name = input("Enter your name for new account")
    if new_name in accounts_database:
      print("This name is already taken. Use another name!")
    else:
      starting_cash = float(input("Enter Your Initial deposit amount : $"))
      new_account_object = BankAccount(new_name,starting_cash)

      accounts_database[new_name] = new_account_object
      print(f"Account successfully created for {new_name} with ${starting_cash}")
      print(f"Current database users: {list(accounts_database.keys())}")
      choice2 = input("Please select an option (1 or 2) | 1 to exit | 2 to continue: ")
      if choice2 == "1":
          print("Thank you for using Blue Bank!")
          break # Stops the program completely
      else:
          print("Returning to main menu...")
          continue
  elif choice == "1":
    user_name = input("enter your name : ")
    if user_name in accounts_database:
      current_account  = accounts_database[user_name]
      print(f"welcome back {current_account.owner}!")
      print(f"Your current account balance is ${current_account.balance}")
      action = input("Do you want to (W)ithdraw or (D)eposit? : ").capitalize()
      if action == "W":
        amount_to_get = float(input("Enter the amount you want to withdraw: "))
        current_account.withdraw(amount_to_get)
      elif action == "D":
        amount_to_add = float(input("Enter amount you want to deposit : "))
        current_account.deposit(amount_to_add)
      else:
        print("Invalid option selected.")

    else:
      print("Error : Account name not found in our database.")
  elif choice == "3":
      print("Thank you for using this atm.")
      break
  else:
    print("Invalid menu choice.")
