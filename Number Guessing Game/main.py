import random
number = random.randint(1, 100)
while True:
 try:
    input_num = int(input("Guess the number: "))

    if input_num > number:
        print("Too high")
    elif input_num < number:
        print("Too low")
    else:
        print("Congratulations!")
        break
 except ValueError:
    print("please enter valid number")
