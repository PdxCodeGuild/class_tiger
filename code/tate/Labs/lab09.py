# unit_converter

distance_input = float(input('What is the distance? > '))
unit_input = input('What units are you using? (feet, miles, meters, or kilometers > ')
# feet_in_meters = user_feet * 0.3048

while unit_input.lower() not in ['feet','miles','meters','kilometers']:

    print('You have not entered a valid unit.')
    unit_input = input('What units are you using? (feet, miles, meters, or kilometers > ')
