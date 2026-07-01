def password_checker(passwords):
  results = []
  for password in passwords:
    has_upper = False
    has_lower = False
    has_digit = False
    length_ok = False
  if len(password) >= 8:
    length_ok = True
  index = 0
  while index < len(password):
    character = password[index]

    if character.isupper():
      has_upper = True
    if character.inlower():
