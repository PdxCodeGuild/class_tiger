'''
Lab 15: Number to Phrase
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'

V2 handles 0 through 999

'''
teens_etc = {'10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'}
zero_thru_nine = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
tens_dict = {'0':'','1':'tens','2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}
user_input = input('Please input a number between 0 and 999 : ')

def return_z_to_9_key(num):
    return zero_thru_nine[num]

def check_teens(num_str):
    if 10 <= int(num_str) < 20:
        my_teens_string = teens_etc[num_str]
        return(my_teens_string)
    else:
        return False

def number_to_phrase(num_str):
    list_num = list(num_str)

    if check_teens(num_str) != False:
        return check_teens(num_str)

    if len(list_num) == 1:
        my_string = zero_thru_nine[list_num[0]]
    elif len(list_num) == 2:
        my_ones = zero_thru_nine[(list_num[1])]
        my_tens = tens_dict[(list_num[0])]
        my_string = my_tens + '-' + my_ones
    elif len(list_num) == 3:
        my_hundreds = zero_thru_nine[list_num[0]] + ' hundred and '

        if check_teens(list_num[1] + list_num[2]) != False:
            my_string = my_hundreds + check_teens(list_num[1] + list_num[2])
            return my_string

        my_tens = tens_dict[(list_num[1])]
        my_ones = zero_thru_nine[(list_num[2])]
        my_string = my_hundreds + my_tens + '-' + my_ones
    else:
        print('I\'m sorry, invalid input')

    return my_string

user_output = number_to_phrase(user_input)
print(user_output)
