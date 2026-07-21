item_name = "Steak"
price = 29.99
quantity = 2

subtotal = price * quantity
subtax = subtotal * 15/100
subtip = subtotal * 10/100
grandtotal = subtotal + subtax + subtip
print(f'Item : {item_name} (x2)')
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax : ${subtax:.2f}")
print(f"Tip : ${subtip:.2f}")
print(f"Grand total: ${grandtotal:.2f}")

