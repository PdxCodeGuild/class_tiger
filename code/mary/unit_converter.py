# unit_converter.py
user_distance = input("What is the distance?")
user_distance = int(user_distance)
user_input = input("What are the input units?")
user_output = input("What are the output units?")
if user_input == "ft":
    user_meters = user_distance * 0.3048
elif user_input == "mi":
    user_meters = user_distance * 1609.34
elif user_input == "m":
    user_meters = user_distance * 1
elif user_input == "km":
    user_meters = user_distance * 1000
elif user_input == "yd":
    user_meters = user_distance * 0.9144
elif user_input == "in":
    user_meters = user_distance * 0.0254
if user_input == user_output:
    print(user_distance)
elif user_output == "ft":
    print(user_meters / 0.3048)
elif user_output == "mi":
    print(user_meters / 1609.34)
elif user_output == "m":
    print(user_meters / 1)
elif user_output == "km":
    print(user_meters / 1000)
elif user_output == "yd":
    print(user_meters / 0.9144)
elif user_output == "in":
    print(user_meters / 0.0254)
