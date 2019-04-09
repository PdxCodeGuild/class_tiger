# unit_converter using a dictionary
meter_dict = {'m': 1, 'ft': 3.28, 'in': 39.37}
in_num = float(input("How many?: "))
in_unit = input("From what unit?: ")
out_unit = input("To what unit?: ")
print(f"{in_num}{in_unit} is {(in_num / meter_dict[in_unit])*meter_dict[out_unit]} {out_unit}.")
