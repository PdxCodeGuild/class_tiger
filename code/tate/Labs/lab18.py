'''
Lab 18: Peaks and Valleys
'''
my_data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]
# my_data = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,4,5,6,7,6,5,4,3,4,5,6,7,8,7,6,5,6,7,8]

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

def peaks_and_valleys():
    my_peaks = peaks(my_data)
    my_valleys = valleys(my_data)
    peaks_and_valleys_list = my_peaks
    peaks_and_valleys_list.extend(my_valleys)
    peaks_and_valleys_list.sort()
    return peaks_and_valleys_list

def draw_my_data(input_data):
    my_peaks = peaks(my_data)
    my_valleys = valleys(my_data)
    horizontal =len(input_data)
    vertical = max(input_data)

    for v in range(vertical):

        # Iterate vertically, printing new lines at the end of loop. Will end up with the
        # height equal to the maximum data value

        print(' ' * 7,end='')

        for h in range(horizontal):
            # need to find a way to put the following logic into a for loop so that the program will work
            # regardless of the number of peaks and valleys and what order they come in

            # for each horizontal space, The following conditional statement is applied to print '.' or 'X':
                # Print X's if (this is for the largest peak):

            if  (my_peaks[1] - v) <= h <= (my_peaks[1] + v) and (input_data[h] >= (vertical - v)) :
                # check whether the horizontal iteration is in between largest peak minus the vertical iteration and
                # the largest peak plus the vertical iteration.... and .... that the
                # value of the input data at the index of the horizontal iteration is less than the difference between
                # the overall vertical height and the current vertical iteration
                print(' X ', end='')
            elif ((my_peaks[0]-v) <= h <= (my_peaks[0]+ v)) and (input_data[h] >= (vertical - v)):
                # Also print X's if (this is for the smaller peak):
                # the vertical iteration is in between the smallest peak minus the vertical iteration and
                # the smallest peak plus the vertical iteration .... and .... that the
                # value of the input data at the index of the horizontal iteration is less than the difference between
                # the overall vertical height and the current vertical iteration
                print(' X ',end='')
            elif h > (max(my_valleys)-v) and (input_data[h] >= (vertical - v)):
                # Also print X's if (this is for the bit remaining after the final peak):
                # the horizontal iteration value is greater than the final valley value minus the vertical iteration .... and ....
                # the input data value at the index of the horizontal iteration is greater than the difference
                # between the overall vertical height and the current vertical iteration
                print(' X ',end='')
            elif (my_valleys[0] - v) <= h <= (my_valleys[0] + v) and (input_data[h] <= (vertical + v)):
                # Print 0's if the horizontal iteration is greater than the first peak but less than the second peak
                print(' 0 ',end='')
            else:
                # For everything else print "."'s:
                print(' . ', end='')



        print('\n')
    print(f'data = {input_data}')

print(peaks(my_data))
print(valleys(my_data))
print(peaks_and_valleys())
draw_my_data(my_data)
