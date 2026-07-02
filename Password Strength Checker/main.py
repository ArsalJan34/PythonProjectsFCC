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
            elif character.islower():
                has_lower = True
            elif character.isdigit():
                has_digit = True
            index += 1
        # Count satisfied conditions
        score = 0
        if has_upper:
            score += 1
        if has_lower:
            score += 1
        if has_digit:
            score += 1
        if length_ok:
            score += 1
        # Decide password strength
        if score == 4:
            results.append("Strong")
        elif score == 3:
            results.append("Good")
        elif score == 2:
            results.append("Weak")
        else:
            results.append("Very Weak")
    return results
passwords = []
num = int(input("How many passwords do you want to check? "))
for i in range(num):
    password = input(f"Enter password {i + 1}: ")
    passwords.append(password)
strengths = password_checker(passwords)
print("\nPassword Strength Results:")
for i, strength in enumerate(strengths):
    print(f"Password {i + 1}: {strength}")
