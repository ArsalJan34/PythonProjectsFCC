print("===============Welcome to Travel Decision System=============")
Distance = int(input("How far is your destination? : "))

Raining = input("Is it raining (YES or NO): ").lower() == "yes"
Bicycle = input("Do you have a bicycle (YES or NO): ").lower() == "yes"
Car = input("Do you have a car (YES or NO): ").lower() == "yes"
Application = input("Do you have a Ride Share application (YES or NO): ").lower() == "yes"
if Distance <= 1:
    if not Raining:
        print("You are recommended to walk.")
    else:
        print("Walking is not recommended.")

elif Distance <= 6:
    if Bicycle and not Raining:
        print("You are recommended to travel by bicycle.")
    else:
        print("Cycling is not recommended.")

else:
    if Car or Application:
        print("You are recommended to travel by car or ride share.")
    else:
        print("There is no suitable transportation available.")
