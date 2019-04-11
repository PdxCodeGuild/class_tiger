def main():
    ones_digit = 0
    tens_digit = 0
    hundreds_digit = 0
    user_number = 0
    
    while 0 >= user_number or user_number > 999:
        while True:
            try:
                user_number = int(input("Enter a number from 0-999: "))
                break
            except ValueError:
                print("Try again. ")
    hundreds_digit, tens_digit, ones_digit = get_digits(user_number)
    # print(hundreds_digit, tens_digit, ones_digit)
    digits_to_words(ones_digit, tens_digit, hundreds_digit)

def get_digits(num):
    if num > 99:
        hundreds_digit = num // 100
        tens_digit = num // 10 % 10
        ones_digit = num % 10
    elif num > 9:
        hundreds_digit = 0
        tens_digit = num // 10
        ones_digit = num % 10
    else:
        hundreds_digit = 0
        tens_digit = 0
        ones_digit = num % 10
    return hundreds_digit, tens_digit, ones_digit

def digits_to_words(ones, tens, hundreds):
    ones_dict = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    tens_dict = {0:'', 1:'ten', 2:'twenty', 3:'thirty', 4:'fourty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninty'}
    hundreds_dict = {0:'', 1:'one hundred', 2:'two hundred', 3:'three hundred', 4:'four hundred', 
                    5:'five hundred', 6:'six hundred', 7:'seven hundred', 8:'eight hundred', 9:'nine hundred'}
    if tens < 2 and tens > 0:
        ones_dict = {0:'', 1:'eleven', 2:'twelve', 3:'thirteen', 4:'fourteen', 5:'fifteen', 6:'sixteen', 
                    7:'seventeen', 8:'eighteen', 9:'nineteen'}
        print(f"{hundreds_dict[hundreds]} {ones_dict[ones]}")
    else:
        print(f"{hundreds_dict[hundreds]} {tens_dict[tens]} {ones_dict[ones]}")





main()