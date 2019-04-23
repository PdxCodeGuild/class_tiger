import pandas as pd
from datetime import datetime

crime_2014 = pd.read_csv("crime_incident_data_2014.csv", skiprows = 1)
df = pd.DataFrame(crime_2014)
'''Find if there are any NA's'''
df.isna()

'''select example row with NA'''
r = df.loc[[47262]]
''''(NA's here don't have a meaning so drop'''
df.dropna(how='all')
#df.dropna(subset=['name', 'born'])
'''Select distinct to see any weird value'''
unique = df.drop_duplicates()
print(unique)
'''find most common crime'''
#df.dropna(subset=["Major Offense Type"])
df.iloc[3].value_counts().max()
df.iloc[:,3].value_counts().idxmax()
'''#Larceny is the most common crime'''
df.iloc[:,3].value_counts().idxmin()
'''#Gambling is the least common crime'''
year = pd.to_datetime(df.iloc[:,1]) #string too date
years = year.dt.to_period('Y') #get the year
years.value_counts().idxmax()
'''#2014 is the year with the most crime'''
