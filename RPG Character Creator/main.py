def create_character(character_name, strength, intelligence,charisma):
  if not isinstance(character_name, str):
    return "The character name should be string"
  if character_name == "":
    return "The character name should not be empty"
  if len(character_name) > 15:
    return "The character name can not be longer than 10 characters"
  if " " in character_name:
    return "The character name can not cotain spaces"

  if (type(strength) is not int or type(intelligence) is not int or type(charisma)is not int):
    return "All Stats should be integers"
  if strength < 1 or strength > 4 or intelligence < 1 or intelligence > 4 or charisma < 1 or charisma > 4:
    return "All stats should be between 1 and 4"
  if strength + intelligence + charisma != 7:
    return "All of stats should be equal to 7"

  return (
      f"\n===== CHARACTER CREATED =====\n"
      f"Name: {character_name}\n\n"
      f"STRENGTH {'●' * strength}{'○' * (4 -strength)}\n"
      f"INTELLIGENCE {'●' * intelligence}{'○' * (4 - intelligence)}\n"
      f"CHARISMA {'●' * charisma}{'○' * (4 - charisma)}"
    )


character_name = input("Enter The Character name: ")
strength = int(input("Enter the strength of character (1-4): "))
intelligence = int(input("Enter the intelligence of the character (1-4): "))
charisma = int(input("Enter the charisma of the character(1-4) : "))
result = create_character(character_name,strength,intelligence,charisma)
print(result)
