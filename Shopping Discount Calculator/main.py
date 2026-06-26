def calculate_discount(price,discount):
  if not isinstance(price,(int,float)):
    return "Price should be a number"
  if not isinstance(discount,(int,float)):
    return "Price"
  if price <= 0:
    return "Price must be greater than 0"
  if discount < 0 or discount >100:
    return "discount must be between 0 and 100"
  discount_amount = price * discount/100
  final_price = price - discount_amount
  return final_price

product_name = "Iphone"
price = 1200
discount = 20
print(f"Product:{product_name}")
print(f"Original Price: {price}")
print(f"Discount: {discount}%")

result = calculate_discount(price,discount)
print(f"Final Price: {result}")
