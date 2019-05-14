#cc_val.py
cc_num = '5,6,4,5,9,0,2,3,5,5,6,7,8,4,3'
cc_num = cc_num.split(',')
cc_num=[int(i) for i in cc_num]
check_digit=cc_num.pop(-1)
cc_reversed = cc_num.reverse()
def double_list(cc_num):
    for i in range(len(cc_num)):
        if i % 2 == 0:
            cc_num[i]=cc_num[i]*2
    return(cc_num)
def sub_nine(cc_num):
    for i in range(len(cc_num)):
        if cc_num[i]>9:
            cc_num[i]= cc_num[i]-9
    return(cc_num)
cc_num = sum(cc_num)
cc_num = cc_num % 10
if cc_num == check_digit:
    print("True!")
else:
    print("False")
