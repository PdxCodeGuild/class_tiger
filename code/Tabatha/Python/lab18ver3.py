data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
values = [" " for x in range(len(data))]


def peaks(data):
    peak_list = []
    for x in range(1, len(data)-1):
        if data[x-1] < data[x] > data[x+1]:
            peak_list.append(x)
    return peak_list
    # 6, 14

def valleys(data):
    valley_list = []
    for x in range(1, len(data)-1):
        if data[x-1] > data[x] < data[x+1]:
            valley_list.append(x)
    return valley_list
    # 9, 17

def peaks_valleys(data):
    peak_valley_list = []
    for x in range(1, len(data)-1):
        if data[x-1] < data[x] > data[x+1]:
            peak_valley_list.append(x)
        elif data[x-1] > data[x] < data[x+1]:
            peak_valley_list.append(x)
    return peak_valley_list
    # 6, 9, 14, 17

def draw(data):
    peak_list = peaks(data)
    peak = 10
    while peak > 1:
        # make 10 print lines
        i = 0
        peak -= 1
        # moe to the next line
        while i < len(data):
            # go through each data item
            if data[i] == peak:
                # tell the print to start
                values[i] = "X"
            i += 1 
            peak_index = -1
            # move to the next data item
        for x in peak_list:
            #fill for each peak
            
            if peak == (data[peak_list[peak_index]]):
                # start filling at the begining of the line at the peak
                for x in range(peak_list[peak_index], len(data)):
                    #tell it how many lines to keep filling
                    if values[x] == " ":
                        values[x] = "o"
            peak_index -= 1
        print("  ".join(values))
print(draw(data))




print(peaks(data))
print(valleys(data))
print(peaks_valleys(data))