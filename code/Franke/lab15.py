#put all the number in a dictionnary

double_dig1 = {1:'Ten',2:'Twenty',3:'Thirty',4:'Forty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty'
         ,9:'Ninety'}
double_dig2 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
single_digit = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
Dozens_dig3 = {1: 'Eleven', 2: 'Twelve', 3: 'Thirteen', 4: 'Fourteen', 5: 'Fifteen',
         6: 'Sixteen', 7: 'Seventeen', 8: 'Eighteen', 9: 'Nineteen'}

#if you divide x by //10 = 0 then it's 1 digit else it's not

def Number_to_Phrase(num):
    first_part = num//10
    second_part = num % 10
    if num > 99:
        return 'Invalid number. Enter number between 0 and 99.'
    elif first_part == 0 and second_part == 0:
        return 'Zero'
    elif first_part == 0:
        return(f'{single_digit[second_part]}')
    elif first_part > 0 and second_part == 0:
        return(f'{double_dig1[first_part]}')
    elif first_part == 1 and second_part > 0:
        return(f'{Dozens_dig3[second_part]}')
    elif first_part > 1 and second_part > 1:
        return(f'{double_dig1[first_part]}-{double_dig2[second_part]}')
    else:
        pass


print(Number_to_Phrase(8))


double_dig1 = {0: '',1:'Ten',2:'Twenty',3:'Thirty',4:'Forty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty'
         ,9:'Ninety'}
single_digit = {0: '',1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
Dozens_dig3 = {0: '',1: 'Eleven', 2: 'Twelve', 3: 'Thirteen', 4: 'Fourteen', 5: 'Fifteen',
         6: 'Sixteen', 7: 'Seventeen', 8: 'Eighteen', 9: 'Nineteen'}

def Number_to_Phrase_from_100(num):
    h = num // 100
    t = (num % 100) // 10
    o = num % 10
    if  100 > num or num > 999:
       return 'Invalid number. Enter number between 100 and 999.'
    elif t == 1 and 0 < o <= 9 :
        return (f'{single_digit[h]} hundred and {Dozens_dig3[t]}')
    elif t == 0 and o == 0 :
        return (f'{single_digit[h]} hundred')
    else :
        return (f'{single_digit[h]} hundred and {Dozens_dig3[t]}{single_digit[o]}')

print(Number_to_Phrase_from_100(212))
