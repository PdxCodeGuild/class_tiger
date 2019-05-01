

meter_dict = {'m': 1, 'ft': 3.28, 'in': 39.37, 'yd': 1.09, 'km': .001, 'mi': .0006}
base_dict = {'binary': 2, 'decimal': 10, 'hexadecimal': 16}

in_num = float(input("How many?: "))
in_unit = input("From what unit? [m, ft, in, yd, km, mi]: ")
while in_unit not in meter_dict:
    in_unit = input("From what unit? [m, ft, in, yd, km, mi]: ")

out_unit = input("To what unit? [m, ft, in, yd, km, mi]: ")
while out_unit not in meter_dict:
    out_unit = input("To what unit? [m, ft, in, yd, km, mi]: ")

which_base = input("What base would you like to convert to? [binary, decimal, hexadecimal]: ")
while which_base not in base_dict:
    which_base = input("What base would you like to convert to? [binary, decimal, hexadecimal]: ")

converted_num = 0
# print(f"{in_num}{in_unit} is {(in_num / meter_dict[in_unit])*meter_dict[out_unit]} {out_unit}.")
decimal_num = (in_num / meter_dict[in_unit])*meter_dict[out_unit]

if base_dict[which_base] != 10:
    if base_dict[which_base] == 2:
        converted_num = bin(int(decimal_num))
    elif base_dict[which_base] == 16:
        converted_num = hex(int(decimal_num))
else: 
    converted_num = decimal_num

print(f"{in_num}{in_unit} is {decimal_num}{out_unit} and is converted to {converted_num} in {which_base}")
