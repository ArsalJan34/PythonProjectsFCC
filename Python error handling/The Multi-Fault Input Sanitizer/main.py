def sanitize_and_divide(raw_input):
  try:
    raw_input_int = int(raw_input)
    result = int(22/ raw_input_int)
    return result
  except ZeroDivisionError:
    return "You cannot divide by zero!"
  except ValueError:
    return "Pleae enter an valid number!"

number = input("Enter an number: ")
print(sanitize_and_divide(number))

