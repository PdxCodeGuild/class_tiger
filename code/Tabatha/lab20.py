
input_string = "2556737586899856"
input_list = list(input_string)

def validate(input_list):
    check_digit = input_list.pop(-1)
    input_list.reverse()
    check_list = [int(i) for i in input_list]
    check_list = [check_list[i] * 2 if i % 2 == 0 else check_list[i] for i in range(len(check_list))]
    check_list = [x - 9 if x > 9 else x for x in check_list]
    check_num = sum(check_list)
    check_num = list(str(check_num))
    if check_num[1] == check_digit:
        return True
    else:
        return False
    # print(check_list)
print(validate(input_list))                                                                                             
