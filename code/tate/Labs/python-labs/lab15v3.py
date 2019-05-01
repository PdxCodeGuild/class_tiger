'''
Lab 15: Number to Phrase
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'

V3 outputs Roman Numerals

'''
hundreds = {'1':'C','2':'CC','3':'CCC','4':'CD','5':'D','6':'DC','7':'DCC','8':'DCCC','9':'CM'}
zero_thru_nine = {'0':'','1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI','7':'VII','8':'VIII','9':'IX'}
tens_dict = {'0':'','1':'X','2':'XX','3':'XXX','4':'XL','5':'L','6':'LX','7':'LXX','8':'LXXX','9':'XC'}
user_input = input('Please input a number between 0 and 999 : ')

def return_z_to_9_key(num):
    return zero_thru_nine[num]

def number_to_roman_numeral(num_str):
    list_num = list(num_str)

    if len(list_num) == 1:
        my_string = zero_thru_nine[list_num[0]]
    elif len(list_num) == 2:
        my_ones = zero_thru_nine[(list_num[1])]
        my_tens = tens_dict[(list_num[0])]
        my_string = my_tens + my_ones
    elif len(list_num) == 3:
        my_hundreds = hundreds[list_num[0]]
        my_tens = tens_dict[(list_num[1])]
        my_ones = zero_thru_nine[(list_num[2])]
        my_string = my_hundreds + my_tens + my_ones
    else:
        my_string = 'Invalid input'
    return my_string

user_output = number_to_roman_numeral(user_input)
print(user_output)
