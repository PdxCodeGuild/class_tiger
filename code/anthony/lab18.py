

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    # data = [4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 8]
    peaks_and_valleys = []

    peaks = find_peaks(data)
    valleys = find_valleys(data)
    peaks_and_valleys = find_peaks_and_valleys(peaks, valleys)
    
    print_peaks_and_valleys(data)
    print(f"Peaks: {peaks}")
    print(f"Valleys: {valleys}")
    print(f"Peaks and Valleys: {peaks_and_valleys}")


def print_peaks_and_valleys(data):
    peaks_and_valleys = ""
    current_row = max(data)
    while current_row > 0:
        for x in data:
            peaks_and_valleys += '  '
            if x >= current_row:
                peaks_and_valleys += 'X'
            else:
                peaks_and_valleys += ' '
        current_row -= 1
        peaks_and_valleys += '\n'
    for i in range(len(data)):
        if i < 10:
            peaks_and_valleys += '  ' + str(i)
        else:
            peaks_and_valleys += ' ' + str(i)
    print(peaks_and_valleys)


def find_peaks(data):
    '''
    Finds peaks from given data
    '''
    peaks = []
    x = 0
    while x < len(data):
        if x == 0:
            if data[x] > data[x+1]:
                peaks.append(x)
        elif x == len(data) - 1:
            if data[x] > data[x-1]:
                peaks.append(x)
        else:
            if data[x] > data[x - 1] and data[x] > data[x + 1]:
                peaks.append(x)
        x += 1
    return peaks


def find_valleys(data):
    '''
    Finds valleys from given data
    '''
    valleys = []
    x = 0
    while x < len(data):
        if x == 0:
            if data[x] < data[x+1]:
                valleys.append(x)
        elif x == len(data) - 1:
            if data[x] < data[x-1]:
                valleys.append(x)
        else:
            if data[x] < data[x-1] and data[x] < data[x+1]:
                valleys.append(x)
        x += 1
    return valleys


def find_peaks_and_valleys(peaks, valleys):
    '''
    Joins peak and valley data into one list
    '''
    peaks_and_valleys = []
    if len(peaks) > len(valleys):
        for x in range(0, len(peaks)):
            peaks_and_valleys.append(peaks[x])
            peaks_and_valleys.append(valleys[x])
    else:
        for x in range(0, len(valleys)):
            peaks_and_valleys.append(peaks[x])
            peaks_and_valleys.append(valleys[x])
    peaks_and_valleys.sort()
    return peaks_and_valleys


main()

