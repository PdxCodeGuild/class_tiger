#########Step 1########################
Distance = int(input("what's the distance in feet? "))
Output_unit1 = Distance * 0.3048
print(f'{Distance} ft is {Output_unit1} m')

#########Step 2########################
Distance2 = int(input("what's the distance? "))
Unit2 = input("what are the units? ")
feet_in_meter = Distance2 * 0.3048
miles_in_meter = Distance2 * 1609.34
kilometer_in_meter = Distance2 * 1000

if Unit2 == "feet":
    print(f'{Distance2} {Unit2} is {feet_in_meter} m')
elif Unit2 == "miles":
    print(f'{Distance2} {Unit2} is {miles_in_meter} m')
elif Unit2 == "kilometers":
    print(f'{Distance2} {Unit2} is {kilometer_in_meter} m')
else:
    print(f'{Distance2} {Unit2} is {Distance2} m')

#########Step 3########################
Distance3 = int(input("what's the distance? "))
Unit3 = input("what are the units? ")
feet_in_meter2 = Distance3 * 0.3048
miles_in_meter2 = Distance3 * 1609.34
kilometer_in_meter2 = Distance3 * 1000
yard_in_meter2 = Distance3 * 0.9144
inch_in_meter2 = Distance3 * 0.0254

if Unit3 == "feet":
    print(f'{Distance3} {Unit3} is {feet_in_meter2} m')
elif Unit3 == "miles":
    print(f'{Distance3} {Unit3} is {miles_in_meter2} m')
elif Unit3 == "kilometers":
    print(f'{Distance3} {Unit3} is {kilometer_in_meter2} m')
elif Unit3 == "yard":
    print(f'{Distance3} {Unit3} is {yard_in_meter2} m')
elif Unit3 == "inch":
    print(f'{Distance3} {Unit3} is {inch_in_meter2} m')
else:
    print(f'{Distance3} {Unit3} is {Distance3} m')

#########Step 4########################
Distance4 = int(input("what's the distance? "))
Input_unit4 = input("what are the input units? ")
Output_unit4 = input("what are the output units? ")
feet_in_meter3 = Distance4 * 0.3048
miles_in_meter3 = Distance4 * 1609.34
kilometer_in_meter3 = Distance4 * 1000
yard_in_meter3 = Distance4 * 0.9144
inch_in_meter3 = Distance4 * 0.0254
meter_feet = feet_in_meter3 / 0.3048
meter_feet = miles_in_meter3 / 1609.34
meter_kilometer= kilometer_in_meter3/ 1000
meter_yard = yard_in_meter3 / 0.9144
meter_inch= inch_in_meter3 / 0.0254

if Input_unit4 == "feet":
    print(f'{Distance3} {Unit3} is {feet_in_meter2} m')
elif Input_unit4 == "miles":
    print(f'{Distance3} {Unit3} is {miles_in_meter2} m')
elif Input_unit4 == "kilometers":
    print(f'{Distance3} {Unit3} is {kilometer_in_meter2} m')
elif Input_unit4 == "yard":
    print(f'{Distance3} {Unit3} is {yard_in_meter2} m')
elif Input_unit4 == "inch":
    print(f'{Distance3} {Unit3} is {inch_in_meter2} m')
else:
    print(f'{Distance3} {Unit3} is {Distance3} m')