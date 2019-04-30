import pandas as pd
import datetime
from matplotlib import pyplot as plt

df = pd.read_csv('./text_files/raindata.csv')
df['date'] = pd.to_datetime(df.Date)
df = df.set_index('date')
df = df.drop(['Date', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'], axis = 1)
df['Total'] = pd.to_numeric(df.Total, errors= 'coerce')
total_rain = df.resample('A').mean()
print(df.head())


plt.plot(total_rain)
plt.show()



# year_2018 = years.loc[years['Date'].str.contains('2018')]

# year_2018.Total = pd.to_numeric(year_2018.Total, errors='coerce')
# sum_year_2018 = year_2018.Total.sum()
# print(sum_year_2018)
# plt.plot(df.Date, df.Total)
# plt.show()