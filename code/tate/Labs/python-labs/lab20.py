'''
Lab 20: Credit Card Validation
write a function which returns whether a string containing a credit card number is valid as a boolean. the steps are as follows:
'''
def card_validator(input_string):
    while True:
        try:
            card_int = int(input_string)
            break
        except ValueError:
            return 'Invalid card number'

    card_list = list(input_string)
    card_int_list = []

    for n in card_list:
        card_int_list.append(int(n))

    check_digit = card_int_list[-1]
    card_int_list.pop()
    card_int_list.reverse()
    list_doubled = [card_int_list[n] * 2 if n % 2 == 0 else card_int_list[n] for n in range(len(card_int_list))]
    list_sub_nine = [n - 9 if n > 9 else n for n in list_doubled]
    sum_list = sum(list_sub_nine)
    list_sum_list = list(str(sum_list))

    if int(list_sum_list[1]) == check_digit:

        return 'Valid!'
    else:
        return 'Invalid!'


print(card_validator('4556737586899855'))
