'''
Lab 24 : Rain Data
'''

import datetime

# date = datetime.datetime.strptime('25-MAR-2019', "%d-%b-%Y")
# print(date.year)
# print(date.month)
# print(date.day)
# print(date)
# print(date.strftime('%d-%b-5Y'))

my_file = 'test-rain-data.txt'
def read_file():
    with open(my_file,'r') as f:
        contents = f.read()
    return contents

def organize_data():
    # removes information before the first date. Returns a list of tuples,
    # where the first value is the date, and the second is the daily total
    contents = read_file()
    contents = contents.split('------------------------------------------------------------------------------------------------------------------')
    contents.pop(0)
    contents = ''.join(contents)
    contents = contents.split('\n')
    c = []
    for item in contents:
        a = item.split('   ')
        c.append(a)
    c = [x for x in c if len(x) > 1]
    contents = []
    for item in c:
        tuple_date = item[0]
        tuple_total = int(item[1].replace(' ',''))
        contents.append((tuple_date,tuple_total))
    return contents

def find_mean(contents):
    # Takes in a list of tuples, and returns the average of the rainfall data stored in index [1]
    data_mean = sum(contents_totals) / len(contents_totals)
    return data_mean

def find_deviance(contents):
    mean = find_mean(contents)
    diff_squared_list = [(x-mean)**2 for x in contents_totals]
    deviance = sum(diff_squared_list) / len(diff_squared_list)
    return deviance

def find_most_rain():
    max_rain = max(contents_totals)
    max_rain_index = contents_totals.index(max_rain)
    max_rain_data = contents[max_rain_index]
    date_of_max = datetime.datetime.strptime(max_rain_data[0], "%d-%b-%Y")
    print(f'The most rain occured on {date_of_max}, with a value of {max_rain}')

contents = organize_data()
contents_totals = [x[1] for x in contents] # the rain accum. totals in a list
data_deviance = find_deviance(contents)
find_most_rain()
