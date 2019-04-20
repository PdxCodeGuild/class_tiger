"""
Lab 23: Contact List

This version updates the .csv file during the while loop instead of at the end.
"""
my_file = 'contacts.csv'
def read_file(my_file):
    # Reads my_file returns it as a list split by \n
    with open(my_file, 'r') as file:
        lines = file.read().split('\n')
    return lines

def get_headers(lines):
    # gets the headers from the lines
    headers = []
    headers = lines.pop(0)
    headers = headers.split(',')
    return headers

def create_contact_dict(input_list):
    # creates the headers from the lines List
    # and zips it with the input list returning a dictionary
    input_list = input_list.split(',')
    contact_dict = dict(zip(headers,input_list))
    return contact_dict

def get_contacts_list(lines):
    # creates the list of dictionaries that is the contact contents_list
    contact_list = []
    lines = [x for x in lines if x != '']
    for line in lines:
        # print(line)
        item = create_contact_dict(line)
        contact_list.append(item)
        # print(contact_list)
    return contact_list

def create_contact(name,favorite_fruit,favorite_color):
    #Creates a contact and appends it to my_file
    contact = '\n' + name + ',' + favorite_fruit + ',' + favorite_color
    with open(my_file,'a') as file:
        file.write(contact)

def view_contacts(lines):
    # prints out the contacts in more readable fashion then the dictionary
    print('\n')
    my_contacts = lines
    for line in lines:
        output_line = line.split(',')
        for l in output_line:
            print(l,end='      ')
        print('\n')

def retrieve_record(name):
    # retrieve a contact based off the input name
    records = []
    for contact in range(len(contact_list)):
        values_list = list(contact_list[contact].values())
        if name in values_list:
            return contact_list[contact],contact
    if records == []:
        print("The contact was not found")
        return False
    return False

def update_name_func(record_tuple,new_value):
    lines = read_file(my_file)
    contact_list = get_contacts_list(lines)
    record = record_tuple[0]
    record_index = record_tuple[1]
    record['name'] = new_value
    contact_list[record_index] = record
    return contact_list

def update_fruit_func(record_tuple,new_value):
    lines = read_file(my_file)
    contact_list = get_contacts_list(lines)
    record = record_tuple[0]
    record_index = record_tuple[1]
    record['favorite fruit'] = new_value
    contact_list[record_index] = record
    return contact_list

def update_color_func(record_tuple,new_value):
    lines = read_file(my_file)
    contact_list = get_contacts_list(lines)
    record = record_tuple[0]
    record_index = record_tuple[1]
    record['favorite color'] = new_value
    contact_list[record_index] = record
    return contact_list

def update_records(contact_list):
    with open(my_file,'w') as file:
        file.write('')
        file.write('name,favorite fruit,favorite color')
    for item in contact_list:
        name = item['name']
        favorite_fruit= item['favorite fruit']
        favorite_color = item['favorite color']
        create_contact(name,favorite_fruit,favorite_color)
    return contact_list

def delete_record():
    name = input('Name of contact you would like to delete > ')
    records = retrieve_record(name)
    while records == False:
        print('Please Try Again')
        name = input('Who would you like to look up? > ').lower()
        records = retrieve_record(name)

    remove_index = records[1]
    print('\n')
    del (contact_list[remove_index])
    print(f'{name} deleted')
    update_records(contact_list)

######## Global variables ########

lines = read_file(my_file)
headers = get_headers(lines)
contact_list = get_contacts_list(lines)

######## Main while loop ########

def main():
    while True:
        print("\nChoices : 'Create Contact', 'View Contacts', 'Retrieve Record' , 'Update Record','Delete Record','Quit'")
        user_choice = input('What would you like to do? > ').lower()
        if user_choice == 'quit':
            print('Goodbye!')
            break
        elif user_choice == 'create contact':
            print('Enter the following information:')
            name = input('Name > ').lower()
            favorite_fruit = input('Favorite Fruit > ').lower()
            favorite_color = input('Favorite Color > ').lower()
            create_contact(name,favorite_fruit,favorite_color)
        elif user_choice == 'view contacts':
            lines = read_file(my_file)
            view_contacts(lines)
        elif user_choice == 'retrieve record':
            name = input('Who would you like to look up? > ').lower()
            records = retrieve_record(name)
            print(records)
        elif user_choice == 'update record':
            name = input('Who would you like to look up? > ').lower()
            records = retrieve_record(name)
            while records == False:
                print('Please Try Again')
                name = input('Who would you like to look up? > ').lower()
                records = retrieve_record(name)
            print(records)
            print('What would you like to update?')
            update_choice = input('Choices: Name, Favorite Fruit, Favorite Color > ').lower()
            while update_choice not in ['name','favorite fruit','favorite color']:
                print('Invalid input')
                update_choice = input('Choices: Name, Favorite Fruit, Favorite Color > ').lower()
            if update_choice == 'name':
                records_tuple = retrieve_record(name)
                new_value = input('What is the new value? > ').lower()
                contact_list = update_name_func(records_tuple,new_value)
                print(contact_list)
                update_records(contact_list)
                print('Name has been updated')
            elif update_choice == 'favorite fruit':
                records_tuple = retrieve_record(name)
                new_value = input('What is the new value? > ').lower()
                contact_list = update_fruit_func(records_tuple,new_value)
                update_records(contact_list)
                print('Favorite fruit has been updated')
            elif update_choice == 'favorite color':
                records_tuple = retrieve_record(name)
                new_value = input('What is the new value? > ').lower()
                contact_list = update_color_func(records_tuple,new_value)
                update_records(contact_list)
                print('Favorite color has been updated')
            else:
                print('Error')
        elif user_choice == 'delete record':
            delete_record()
        else:
            print('Invalid input, try again\n')
            continue

main()
