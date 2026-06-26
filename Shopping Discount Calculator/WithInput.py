print("========== Shopping Discount Calculator ==========")


def calculate_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "Price should be a number."
    if not isinstance(discount, (int, float)):
        return "Discount should be a number."
    elif price <= 0:
        return "Price must be greater than 0."
    elif discount < 0 or discount > 100:
        return "Discount must be between 0 and 100."
    discount_amount = price * discount / 100
    final_price = price - discount_amount

    return final_price
product_name = input("Enter product name: ")
price = float(input("Enter product price: "))
discount = float(input("Enter discount percentage: "))

result = calculate_discount(price, discount)
print("========== RECEIPT ==========")
print(f"Product: {product_name}")
print(f"Original Price: {price}")
print(f"Discount: {discount}%")
print(f"Final Price: {result}")

