from datetime import datetime
import re, string, matplotlib.pyplot as plt

def load_data():
    with open('maplewood.txt', 'r') as f: #note a csv is a text becuz ,seperated
        raw = f.read().split('\n')
        '''remove empty give back lines that don't start and end with space'''
        remove_empty_lines = [line for line in raw if line.strip() != '']
        '''remove unwanted first 7 lines'''
        semi = remove_empty_lines[7:len(remove_empty_lines)]
        '''get header & remove duplicated empty spaces'''
        header = semi.pop(0).strip().split()
        '''only two columns needed'''
        header = header[0:2]
        '''data'''
        semi = semi[1:len(semi)]
        data = [] #create a list
        dates =[]
        values =[]
        for i in range(len(semi)):
            comma_sep_v_list = semi[i].lower().strip().split()
            dates.append(comma_sep_v_list[0])
            values.append(comma_sep_v_list[1])
            data_frame = dict(zip(header, comma_sep_v_list))
            data.append(data_frame ) #make list of dictio
        print(data)
        return data, header, dates, values

data, header, dates, values = load_data()

def date_formatting(dates):
    formatted_date = []
    for date in dates:
        date = datetime.strptime(date, '%d-%b-%Y')
        formatted_date.append(date)
    return formatted_date

def mean(values):
    clean = []
    for i in values:
        if i.isdigit():
            clean.append(int(i))
        #v = re.sub('[^0-9]', '', i)
    print(clean)
    mean = round(sum(clean)/len(clean),2)
    return mean

def get_list(data):
    '''operations on each values of a dict'''
    d =[]
    for day in data:
        a = {k: int(v) if k == 'Total' and v.isdigit() else v for k, v in day.items()}
        d.append(a)

    db =[]
    for days in d:
        ap = {k: datetime.strptime(v, '%d-%b-%Y') if k == 'Date' else v for k, v in days.items()}
        db.append(ap)
    #print(db)
    return db

db = get_list(data)

def x_axis(db):
    x = []
    for i in db:
        for k, v in i.items():
            if k == 'Date':
                x.append(v)
    return x

def y_axis(db):
    y = []
    for i in db:
        for k,v in i.items():
            if k == 'Total':
                y.append(v)
    return y

y = y_axis(db)
x = x_axis(db)


'''all data plot'''
plt.plot(x, y)
plt.show()

'''get years and plot'''

