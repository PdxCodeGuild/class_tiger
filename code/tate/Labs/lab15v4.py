'''
Lab 15: Number to Phrase
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'

V4 Converts a time given in hours and minutes to a phrase.

'''
teens_etc = {'10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'}
zero_thru_nine = {'0':'clock','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten','11':'eleven','12':'twelve'}
tens_dict = {'0':'','2':'twenty','3':'thirty','4':'forty','5':'fifty'}
user_input = input('Please input a time with the format XX:XX > ')

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

    else:
        my_string = 'I\'m sorry, invalid input'
        return my_string

    return my_string


def time_to_phrase(input_str):
    list_time = list(input_str)

    while ':' not in list_time and len(list_time) != 5:
        print('Incorrect format')
        list_time = list(input('Please input a time with the format XX:XX > '))

    time_string_left = list_time[:2]
    time_string_right = list_time[3:]

    while int(''.join(time_string_left)) > 12 or int(''.join(time_string_right)) > 59:
        print('Incorrect format')
        list_time = list(input('Please input a time with the format XX:XX > '))
        time_string_left = list_time[:2]
        time_string_right = list_time[3:]

    if time_string_left[0] == '0':
        left_side = number_to_phrase(time_string_left[1])
    else:
        time_string_left_joined = ''.join(time_string_left)
        left_side = number_to_phrase(time_string_left_joined)

    time_string_right = list_time[3:]

    if time_string_right[0] == '0':
        right_side = 'o\' ' + number_to_phrase(time_string_right[1])
    else:
        time_string_right_joined = ''.join(time_string_right)
        right_side = number_to_phrase(time_string_right_joined)

    my_time_string = f'The time is {left_side} {right_side}'
    return my_time_string


user_output = time_to_phrase(user_input)
print(user_output)
