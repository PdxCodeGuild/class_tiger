# unit conversions
units = ['ft', 'mi', 'km', 'yd', 'in', 'm']
distance = int(input("what is the distance? > "))

start_unit = input(f"What are the starting units? {units} > ")
while start_unit not in units:
    start_unit = input(f"Choose from: {units} > ")
if start_unit == "ft":
    convert = distance * 0.3048
elif start_unit == "mi":
    convert = distance * 1609.34
elif start_unit == "km":
    convert = distance * 1000
elif start_unit == "m":
    convert = distance * 1
elif start_unit == "in":
    convert = distance * 0.0254
elif start_unit == "yd":
    convert = distance * 0.9144

end_unit = input(f"What are the end units? ft, mi, km, yd, in > ")
while end_unit not in units:
    end_unit = input(f"Choose from: {units} > ")
if end_unit == "ft":
    distance2 = convert * 3.280839895
elif end_unit == "mi":
    distance2 = convert * 0.0006213689
elif end_unit == "km":
    distance2 = convert * 0.001
elif end_unit == "m":
    distance2 = convert * 1
elif end_unit == "in":
    distance2 = convert * 39.37007874
elif end_unit == "yd":
    distance2 = convert * 1.0936132983

print(f"{distance}{start_unit} is also {distance2}{end_unit}")
