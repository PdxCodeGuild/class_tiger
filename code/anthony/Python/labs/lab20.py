def main():
    
    cc_number = input("Enter in the credit card number: ")
    cc_number = [s for s in cc_number if s.isdigit()]
    # cc_number = '4556737586899855'
    # print(cc_number)       
    print(is_valid(cc_number))

def is_valid(cc):
    cc = [int(x) for x in cc]
    check_digit = cc.pop(len(cc) - 1)
    # print(check_digit)
    # print(cc)
    cc.reverse()
    # print(cc)
    cc = [cc[i] * 2 if i % 2 == 0 else cc[i] for i in range(len(cc))]
    # print(cc)
    cc_minus_nine = [cc[i] - 9 if cc[i] > 9 else cc[i] for i in range(len(cc))]
    # print(cc_minus_nine)
    cc_sum = 0
    for n in cc_minus_nine:
        cc_sum += n
    cc_sum = str(cc_sum)
    # print(cc_sum)
    if check_digit == int(cc_sum[1]):
        return True
    return False

main()