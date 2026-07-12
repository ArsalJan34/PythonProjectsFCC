# Creating a custom exception class by inheriting from Exception
class InvalidCredentialsError(Exception):
    pass
def secure_gatekeeper(username, password):
    correct_username = "admin"
    correct_password = "password123"
    if username == correct_username and password == correct_password:
         return "Access Granted"
    else:
         raise InvalidCredentialsError("Access Denied")

try:
    result = secure_gatekeeper("admin", "password123")
    print(result)
except InvalidCredentialsError as e:
    print(f"Error caught: {e}")
try:
    result = secure_gatekeeper("admin", "wrong_password")
    print(result)
except InvalidCredentialsError as e:
    print(f"Error caught : {e}")  # Prints: Error caught: Access Denied
