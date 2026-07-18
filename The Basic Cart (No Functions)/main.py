inventory = {
  "apple": 1.50,
  "egg": 0.50,
  "coffee": 5.00,
  "tea": 0.50,
  "oodles": 2.50,
  "bread": 1.00
  }

cart = []

print("________Welcome To Our Shop________")
for product, price in inventory.items():
  print(f"{product.capitalize()} : ${price:.2f} ")

while True:
  choice = input("Yype What do You want to purchase (type done to checkout): ").lower().strip()
  if choice == "done":
    break
  elif choice in inventory:
    cart.append(choice)
    print(f"Added '{choice}' in your cart")
  else:
    print("The item you entered isnt available")

if not cart:
  print("Your cart is empty. Total : $0.00 ")
else:
  subtotal = 0
  print("Items purchased: ")
  items_num =[]
  for item in cart:
    if item in items_num:
      continue
    quantity = cart.count(item)

    price = inventory[item]
    item_total = price * quantity
    subtotal += item_total
    print(f"- {quantity}x {item.capitalize()} = ${item_total:.2f}")
    items_num.append(item)
  print(f"total bill : {subtotal}")
  discount = 0
  if subtotal > 10:
    discount = subtotal * 0.10
    final_total = subtotal - discount
    print(f"Your Total Bill With Discount is :{final_total:.2f} ")
  else:
    print(f"Your Total Bill is :{subtotal: .2f} ")
