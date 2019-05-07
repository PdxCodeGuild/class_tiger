

num_to_phrase_ones = {"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine", "0":""}
num_to_phrase_tens = {"":"", "1":"teen", "2":"twenty ", "3":"thirty ", "4":"forty ", "5":"fifty ", "6":"sixty ", "7":"seventy ", "8":"eighty ", "9":"ninety ", "0":""}
num_to_phrase_hund = {"":"", "1":"one hundred and ", "2":"two hundred and ", "3":"three hundred and ", "4":"four hundred and ", "5":"five hundred and ", "6":"six hundred and ", "7":"seven hundred and ", "8":"eight hundred and ", "9":"nine hundred and ", "0":""}

def num_to_phrase(num):
    num = str(num)
    if len(num) < 2:
        num = "00" + num
    if len(num) < 3:
        num = "0" + num
    ones_digit = num[-1]
    tens_digit = num[-2]
    hund_digit = num[-3]
    ones_phrase = num_to_phrase_ones[ones_digit]
    tens_phrase = num_to_phrase_tens[tens_digit]
    hund_phrase = num_to_phrase_hund[hund_digit]
    if tens_digit == "1":
        if ones_digit == "0":
            tens_phrase = "ten"
            return hund_phrase + ones_phrase + tens_phrase
        return hund_phrase + ones_phrase + tens_phrase
    else:
        return hund_phrase + tens_phrase + ones_phrase


print(num_to_phrase(810))