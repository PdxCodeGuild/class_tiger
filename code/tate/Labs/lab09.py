# unit_converter

user_distance = float(input("What is the distance? : "))
user_units = input('What is the unit? (feet, miles, meters, kilometers, yards, inches) : ')
end_units = input('What would you like to convert to? : ')
meter_conversion = 0

if user_units == 'feet':
    meter_conversion = user_distance * 0.3048
elif user_units == 'miles':
    meter_conversion = user_distance * 1609.34
elif user_units == 'meters':
    meter_conversion = user_distance * 1
elif user_units == 'kilometers':
    meter_conversion = user_distance * 1000
elif user_units == 'yards':
    meter_conversion = user_distance * 0.9144
elif user_units == 'inches':
    meter_conversion = user_distance * 0.0254
else:
    print('you did not enter a valid starting unit')

if end_units == 'feet':
    final_conversion = meter_conversion / 0.3048
elif end_units == 'miles':
    final_conversion = meter_conversion / 1609.34
elif end_units == 'meters':
    final_conversion = meter_conversion / 1
elif end_units == 'kilometers':
    final_conversion = meter_conversion / 1000
elif end_units == 'yards':
    final_conversion = meter_conversion / 0.9144
elif end_units == 'inches':
    final_conversion = meter_conversion / 0.0254
else:
    print('you did not enter a valid end unit')

print(f'{user_distance} {user_units} is {final_conversion} {end_units}')
