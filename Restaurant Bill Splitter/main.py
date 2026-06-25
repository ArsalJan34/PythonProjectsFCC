Latte = 37.89
Cappicino = 57.34
Espresso = 50.21
Tea = 39.39
Chocolate_cookie = 64.21
print("Welcome To Starbucks")
print("==========MENU============")
print(f"Latte : {Latte}")
print(f"Cappicino : {Cappicino}")
print(f"Espresso : {Espresso}")
print(f"Tea : {Tea}")
print(f"Chocolate Cookie : {Chocolate_cookie}")
number_of_friends = int(input("Enter Number of friends : "))
Cappicino_item = int(input("Enter the number of cappucino you want : "))
Tea_item = int(input("Enter the number of Tea you want : "))
Chocolate_cookie_item = int(input("Enter the number of Chocolate Cookie you want : "))
Latte_item = int(input("Enter the number of Latte you want : "))
Espresso_item = int(input("Enter the number of Espresso you want : "))
total_espresso_price = Espresso * Espresso_item
total_cappucino_price = Cappicino * Cappicino_item
total_tea_price =  Tea * Tea_item
total_latte_price = Latte * Latte_item
total_chocolate_cookie_price = Chocolate_cookie * Chocolate_cookie_item
total_price = total_cappucino_price + total_chocolate_cookie_price + total_espresso_price+ total_latte_price + total_tea_price
tax = 0.25
total_tax_price = total_price * tax
total_final_price = total_tax_price + total_price
splitted_friends_bill = total_final_price / number_of_friends
Final_bill_without_tax = round(total_price,2)
Final_bill_with_tax = round(total_final_price,2)
Final_splitted_bill = round(splitted_friends_bill,2)
print(f"Total Price Without Tax : {Final_bill_without_tax} ")
print(f"Total Price With Tax : {Final_bill_with_tax} ")
print(f"Total Bill on each person: {Final_splitted_bill}")
