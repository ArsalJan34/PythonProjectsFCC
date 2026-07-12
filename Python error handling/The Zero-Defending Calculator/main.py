def safe_divide(numerator, denominator):
  try:
    result = numerator / denominator
    return result
  except ZeroDivisionError:
    return "You cant divide wiht zero"

print(int(safe_divide(22,2)))
