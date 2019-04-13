#number_to_phrase
word_list = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

word_list2= {0: "", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

word_list3={100: "one hundred", 200: "two hundred", 300: "three hundred", 400: "four hundred", 500: "five hundred", 600: "six hundred", 700: "seven hundred", 800: "eight hundred", 900: "nine hundred"}

roman_list={1: "i", 2: "ii", 3:"iii", 4:"iv", 5:"v", 6: "vi", 7: "vii", 8: "viii", 9: "ix", 10: "x"}

def input_num(x):
    ones_digit = x % 10
    tens_digit = (x//10)
    hundreds_digit = (x//100)
    if (x >=0 and x<=19):
        return word_list[x]
    elif (x>=20 and x<= 99):
        return word_list2[x//10*10] +" "+ word_list[x%10]
    elif (x>=100 and x<=999):
        return word_list3[x//100*100] + " " + word_list2[x//100*10] +" "+ word_list[x%10]

def input_roman(x):
    if (x>=1 and x<=10):
        return roman_list[x]


def input_time(hours, mins):
    hours = word_list[hours]
    if (mins>=20 and mins<=59):
        mins = word_list2[mins//10*10] +" "+ word_list[mins%10]
    elif (mins>=0 and mins<=19):
        mins = word_list[mins]
    return hours + " hours"+ " "+mins+" minutes"
