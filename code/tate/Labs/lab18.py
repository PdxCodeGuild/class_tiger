'''
Lab 18: Peaks and Valleys
'''
# my_data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8]

my_data = [1,2,3,4,5,4,3,4,5,6,7,6,5,4,5,6,7]

def peaks(input_data):
    store_data = []
    my_peaks = []
    for n in range(len(input_data)):
        store_data.append(input_data[n])
        if n - 1 < 0 or n - 2 < 0:
            continue
        # print((store_data[n-2],store_data[n-1],store_data[n]))
        if store_data[n-2] < store_data[n-1] > store_data[n]:
            my_peaks.append(n-1)
    return my_peaks
print(peaks(my_data))

def valleys(input_data):
    store_data = []
    my_valleys = []
    for n in range(len(input_data)):
        store_data.append(input_data[n])
        if n - 1 < 0 or n - 2 < 0:
            continue
        # print(store_data[n-2],store_data[n-1],store_data[n])
        if store_data[n-2] > store_data[n-1] < store_data[n]:
            my_valleys.append(n-1)
    return my_valleys
#
print(valleys(my_data))

def peaks_and_valleys():
    my_peaks = peaks(my_data)
    my_valleys = valleys(my_data)
    peaks_and_valleys_list = my_peaks
    peaks_and_valleys_list.extend(my_valleys)
    peaks_and_valleys_list.sort()

    return peaks_and_valleys_list

print(peaks_and_valleys())

def draw_my_data(input_data):
    my_peaks = peaks(my_data)
    my_valleys = valleys(my_data)
    horizontal =len(input_data)
    vertical = max(input_data)

    for v in range(vertical):

        print(' ' * 7,end='')
        for h in range(horizontal):

            if  (max(my_peaks)-v) <= h <= (max(my_peaks)+ v) and (input_data[h] >= (vertical - v)) :
                print(' X ', end='')

            elif ((min(my_peaks)-v) <= h <= (min(my_peaks)+ v)) and (input_data[h] >= (vertical - v)):
                print(' X ',end='')
            elif h > (max(my_valleys)-v) and (input_data[h] >= (vertical - v)):
                print(' X ',end='')
            else:
                print(' . ', end='')
        print('\n')
    print(f'data = {input_data}')




draw_my_data(my_data)
