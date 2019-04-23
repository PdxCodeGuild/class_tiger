'''
Lab 24 : Rain Data
'''

import datetime
import matplotlib.pyplot as plt

# date = datetime.datetime.strptime('25-MAR-2019', "%d-%b-%Y")
# print(date.year)
# print(date.month)
# print(date.day)
# print(date)
# print(date.strftime('%d-%b-%Y'))

my_file = 'rain-data.txt'
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
    contents_totals = [x[1] for x in contents] # the rain accum. totals in a list
    data_mean = sum(contents_totals) / len(contents_totals)
    return data_mean

def find_deviance(contents):
    mean = find_mean(contents)
    contents_totals = [x[1] for x in contents] # the rain accum. totals in a list
    diff_squared_list = [(x-mean)**2 for x in contents_totals]
    deviance = sum(diff_squared_list) / len(diff_squared_list)
    return deviance

def find_most_rain():
    contents_totals = [x[1] for x in contents] # the rain accum. totals in a list
    max_rain = max(contents_totals)
    max_rain_index = contents_totals.index(max_rain)
    max_rain_data = contents[max_rain_index]
    date_of_max = datetime.datetime.strptime(max_rain_data[0], "%d-%b-%Y")
    print(f'\nThe most rain occured on {date_of_max}, with a value of {max_rain}')

def get_num_of_years():
    # shows the num of years in the data
    my_years = []
    for x in contents:
        x_year = datetime.datetime.strptime(x[0], "%d-%b-%Y")
        my_years.append(x_year.year)
    num_of_years = len(set(my_years))
    return num_of_years

def get_by_target(target_year):
    # The below, creates a list of the data within the input year
    contents_by_year = []
    for num in range(len(contents)):
        date = datetime.datetime.strptime(contents[num][0], "%d-%b-%Y")
        if date.year == target_year:
            contents_by_year.append(contents[num])
    return contents_by_year

def get_years_and_means():
    years_and_means = []
    means = []
    for n in range(num_of_years):
        target_year = 2019 - n
        years_and_means.append((target_year,find_mean(get_by_target(target_year))))
        means.append(find_mean(get_by_target(target_year)))
    return years_and_means


def get_highest_mean_year():
    years_and_means = []
    means = []
    for n in range(num_of_years):
        target_year = 2019 - n
        years_and_means.append((target_year,find_mean(get_by_target(target_year))))
        means.append(find_mean(get_by_target(target_year)))

    my_index = means.index(max(means))
    highest_mean_year = years_and_means[my_index][0]
    print(f'\nThe year which had the most rain on average was {highest_mean_year}')
    return (highest_mean_year,years_and_means)

def plot_data(contents):

    x_values = []
    y_values = []

    for num in range(0,len(contents)):
        # date = datetime.datetime.strptime(contents[num][0], "%d-%b-%Y")
        x_values.append(contents[num][0])
        y_values.append(contents[num][1])

    # print(x_values)
    # print(y_values)
    print(f'\nThis plot shows years vs mean rainfall')
    plt.xlabel('Year')
    plt.ylabel('Mean Rainfall')
    plt.title('2033 Harney St. Rain Gage Data')
    plt.plot(x_values,y_values)
    plt.show(block=True)


contents = organize_data()
data_deviance = find_deviance(contents)
total_mean = find_mean(contents)
most_rain_day = find_most_rain()
num_of_years = get_num_of_years()
(highest_mean_year, years_and_means) = get_highest_mean_year()
# print(years_and_means)
plot_data(years_and_means)
