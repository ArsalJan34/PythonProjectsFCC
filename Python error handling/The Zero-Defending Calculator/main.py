def safe_divide(numerator, denominator):
  # open try block to watch fro potential runtime errors
  try:
    result = numerator / denominator
    return result
  # intercept a zerodivisionerror specifically if the denominator is 0
  except ZeroDivisionError:
    return "You cant divide wiht zero"

print(int(safe_divide(22,2)))
