#c_list.py


with open('contacts.csv', 'r') as file:
    lines = file.read().strip()
    lines= lines.split('\n')
    contacts =[]
    header=lines[0].split(',')
    for i in range(1, len(lines)):
        rows = lines.pop(1).split(',')
        contacts.append(dict(zip(header, rows)))

def create():
    name_input=input("What is your name? ")
    state_input=input("What state do you live in? ")
    city_input = input("What city do you live in? ")
    c_update=contacts.append({'Name': name_input,'State': state_input, 'City': city_input })

def retrieve():
    get_name =input("What name do you want to find? ")
    for i in contacts:
        if i['Name']==get_name:
            return i
    if get_name != contacts:
        print("Try again")
        return retrieve()
print(retrieve())

def update():
    enter_name=input("What name needs updating? ")
    for i in contacts:
        if i['Name'] == enter_name:
            update_info = input("What info would you like to change? ")
            if ('State')==update_info:
                change_info=input("And what do you want to change it to? ")
                if i['Name'] == enter_name:
                    i['State']=change_info
            if ('City')==update_info:
                change_info=input("And what do you want to change it to? ")
                if i['Name']==enter_name:
                    i['City']=change_info

def delete():
    delete_name = input("What name do you want deleted? ")
    for i in contacts:
        if i['Name'] == delete_name:
            contacts.remove(i)
