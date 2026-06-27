print("========== Secret Message Encoder & Decoder ==========")
def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return "Shift must be an integer value."
    if shift < 1 or shift > 25:
        return "Shift must be an integer between 1 and 25."
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if not encrypt:
        shift = -shift
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)
def encrypt(text, shift):
    return caesar(text, shift)
def decrypt(text, shift):
    return caesar(text, shift, False)
print("\n1. Encrypt Message")
print("2. Decrypt Message")
choice = input("Choose an option (1 or 2): ")
text = input("Enter your message: ")
shift = int(input("Enter shift value (1-25): "))
if choice == "1":
    result = encrypt(text, shift)
    print("\n======== RESULT ========")
    print("Original Message :", text)
    print("Shift Value      :", shift)
    print("Encrypted Message:", result)
elif choice == "2":
    result = decrypt(text, shift)
    print("\n========== RESULT ========")
    print("Encrypted Message:", text)
    print("Shift Value      :", shift)
    print("Decrypted Message:", result)
else:
    print("Invalid choice. Please select 1 or 2.")
print("\nThank you for using the Secret Message Encoder & Decoder")
