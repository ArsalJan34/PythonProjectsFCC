def inspect_coversion(text_to_convert):
  try:
    number = int(text_to_convert)
    return number
  # Catch ValueError and save the error object inside the variable 'e'
  except ValueError as e:
    return f"Caught an error : {e}"

print(inspect_coversion("400"))
print(inspect_coversion("abc"))
