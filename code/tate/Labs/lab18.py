'''
Lab 18: Peaks and Valleys
'''
my_data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8]

def peaks(input_data):
    store_data = []
    my_peaks = []
    for n in range(len(input_data)):
        store_data.append(input_data[n])
        if n - 1 < 0 or n - 2 < 0:
            continue
        # print(store_data[n-2],store_data[n-1],store_data[n])
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
    peak_dif = my_peaks[1] - my_peaks[0]
    # peak_pos0 = -1*(my_peaks[0] - horizontal)
    # peak_pos1 = -1*(my_peaks[1] - horizontal)


    for v in range(vertical):
        print('')
        for h in range(horizontal):
            if h == (max(my_peaks)-v):
                print('X'+ 2 * v * 'X', end='')

            elif h > (max(my_peaks)+v) :
                print('.', end='')

            elif h == min(my_peaks) and input_data[h] >= (vertical-v):
                print('1' + 2 * v * '1',end='')
            else:
                print('.', end='')

    # for v in range(peak_dif):
    #     print((peak_pos0 - v) * '.' + 'X' * 2 * v + 'X'  + (peak_dif - v) * '.' + 'X' * 2 * v + 'X' + (peak_pos1 - v) * '.')

    print('')
    # print(my_peaks[1] * ' ' + 'X' )
    # print((my_peaks[1]-1) * ' ' + 'XXX' )
    # print((my_peaks[1]-2) * ' ' + 'XXXXX' )



# draw_my_data(my_data)
