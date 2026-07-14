# Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
def multi(num1,num2):
  result = num1 * num2
  if result <= 1000:
    return result
  else:
    return num1 + num2

num1 = int(input("Enter the value of first number: "))
num2 = int(input("Enter the value of second number: "))
result = multi(num1,num2)
print(f"The result is :{result}")
