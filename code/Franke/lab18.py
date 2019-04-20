data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#The indices of a list can be accessed using range().
def peaks():
    new_stuff =[]
    for i in range(1,len(data)-1):
        if data[i-1] < data[i] > data[i+1]: #A peak has a lower number on both the left and the right.
            new_stuff.append(i)
    return new_stuff

print(peaks())

def valleys():
    another_stuff =[]
    for i in range(1,len(data)-1): #exclude extremities
        if data[i-1] > data[i] < data[i+1]: #A valley is a number with a higher number on both the left and the right.
            another_stuff.append(i)
    return another_stuff

print(valleys())

def peaks_and_valleys():
    combined = sorted(peaks() + valleys())
    return combined


