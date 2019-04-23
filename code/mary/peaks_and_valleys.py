#peaks_and_valleys.py
data =[1, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 8, 9]
def peaks(data):
    summit = []
    for i in range(1, len(data)-1):
        if data[i-1]<data[i]>data[i+1]:
            summit = summit.append(i)
        return summit

def valleys(data):
    valley = []
    for i in range(1, len(data) -1):
        if data[i-1]> data[i]< [i+1]:
            valley.append(i)
        return valley

def peaks_and_valleys(data):
    peaks_and_valleys_list = []
    peaks_and_valleys = sorted(peaks(data) + valleys(data))
    return peaks_and_valleys
