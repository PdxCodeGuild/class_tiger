data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peak_list = []
    for x in range(1, len(data)-1):
        if data[x-1] < data[x] > data[x+1]:
            peak_list.append(x)
    return peak_list

def valleys(data):
    valley_list = []
    for x in range(1, len(data)-1):
        if data[x-1] > data[x] < data[x+1]:
            valley_list.append(x)
    return valley_list

def peaks_valleys(data):
    peak_valley_list = []
    for x in range(1, len(data)-1):
        if data[x-1] < data[x] > data[x+1]:
            peak_valley_list.append(x)
        elif data[x-1] > data[x] < data[x+1]:
            peak_valley_list.append(x)
    return peak_valley_list



print(peaks(data))
print(valleys(data))
print(peaks_valleys(data))