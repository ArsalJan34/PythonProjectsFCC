
inventory = {
    "apple" : 1.50,
    "egg" : 0.50,
    "bread" : 1.80,
    "chocolate" : 2.00,
    "coffee" : 5.50,
    "tea" : 2.50,
    "juice" : 3.50,
  }
cart = []
def display_inventory():
  print("-------- Welcome to shop----------")
  for product, cost in inventory.items():
    print(f"{product.capitalize()} : ${cost:.2f}")
  print("----------------------------------")

def add_to_cart():
  while True:
    choice = input("Enter the product name you want to buy or (Type 'done' to checkout ):  ").lower().strip()
    if choice == "done":
      break
    elif choice in inventory:
      cart.append(choice)
      print(f"Added {choice} to cart")
    else:
      print("Sorry the product you entered is not available.")

def delete_product(item_to_remove):
    if item_to_remove in cart:
        cart.remove(item_to_remove)
        print(f"Removed {item_to_remove} from your cart.")
    else:
        print("Sorry, that product wasn't in your cart.")

def show_bill():
    print("\n_____________Your Receipt________")
    if not cart:
        print("Your cart is empty! Total: $0.00")
        return # Stops the function early if cart is empty

    subtotal = 0
    print("Items purchased: ")
    item_time = []
    for item in cart:
        if item in item_time:
           continue
        quantity = cart.count(item)
        price = inventory[item]
        subtotal += price
        print(f"- {quantity}x {item.capitalize()}: ${price:.2f}")
        item_time.append(item)

    # Optional 10% discount logic
    discount = 0.0
    if subtotal > 10.00:
        discount = subtotal * 0.10

    total = subtotal - discount
    print("--------------------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    if discount > 0:
        print(f"Discount (10%): -${discount:.2f}")
    print(f"Final Total: ${total:.2f}")
    print("________________________________")

display_inventory()
add_to_cart()

while True:
   print(f"Your current cart : {cart}")
   choice2 = input("Type 'add' to add more products \n type 'remove' to remove product from your cart or \n type 'final' to get your bill : " )
   if choice2 == "add":
      display_inventory()
      add_to_cart()
   elif choice2== 'remove':
      item_to_delete = input("Which item would you like to remove from your cart? ").lower().strip()
      delete_product(item_to_delete)
   elif choice2== "final":
      show_bill()
      break
   else:
      print("invalid choice please enter again")
