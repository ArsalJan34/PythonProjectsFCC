print("=========================================================")
print("=============== Welcome to Movie Theater ==================")
print("Prices:")
print(
    "Seat Types:\n"
    "Premium Seat Ticket: $50\n"
    "Gold Seat Ticket: $30\n"
    "Basic Seat Ticket: $10\n"
    "Evening: +$2\n"
    "Weekend: +$5"
)

user_ticket = input("Which ticket do you want (Premium/Gold/Basic)? ").lower()
user_ticket_time = input("Which show time do you want (Morning/Evening)? ").lower()
user_ticket_day = input("Which day (Weekday/Weekend)? ").lower()
user_age = int(input("Enter Your Age: "))

# Adult
if user_age >= 18:

    if user_ticket == "premium":
        ticket = 50

        if user_ticket_time == "evening":
            ticket += 2

        if user_ticket_day == "weekend":
            ticket += 5

        print(f"Total Price of ticket: ${ticket}")

    elif user_ticket == "gold":
        ticket = 30

        if user_ticket_time == "evening":
            ticket += 2

        if user_ticket_day == "weekend":
            ticket += 5

        print(f"Total Price of ticket: ${ticket}")

    elif user_ticket == "basic":
        ticket = 10

        if user_ticket_time == "evening":
            ticket += 2

        if user_ticket_day == "weekend":
            ticket += 5

        print(f"Total Price of ticket: ${ticket}")

    else:
        print("Invalid ticket type.")

# Under 18
else:

    if user_ticket == "premium":
        ticket = 50

        if user_ticket_time == "evening":
            print("Sorry! You are not eligible for the evening show.")
            cancel_or_not = input("Enter YES to continue with Morning or NO to cancel: ").lower()

            if cancel_or_not == "no":
                print("Thank you!")
                exit()

            user_ticket_time = "morning"

        if user_ticket_day == "weekend":
            ticket += 5

        print(f"Total Price of ticket: ${ticket}")

    elif user_ticket == "gold":
        ticket = 30

        if user_ticket_time == "evening":
            print("Sorry! You are not eligible for the evening show.")
            cancel_or_not = input("Enter YES to continue with Morning or NO to cancel: ").lower()

            if cancel_or_not == "no":
                print("Thank you!")
                exit()

            user_ticket_time = "morning"

        if user_ticket_day == "weekend":
            ticket += 5

        print(f"Total Price of ticket: ${ticket}")

    elif user_ticket == "basic":
        ticket = 10

        if user_ticket_time == "evening":
            print("Sorry! You are not eligible for the evening show.")
            cancel_or_not = input("Enter YES to continue with Morning or NO to cancel: ").lower()

            if cancel_or_not == "no":
                print("Thank you!")
                exit()

            user_ticket_time = "morning"

        if user_ticket_day == "weekend":
            ticket += 5

        print(f"Total Price of ticket: ${ticket}")

    else:
        print("Invalid ticket type.")
