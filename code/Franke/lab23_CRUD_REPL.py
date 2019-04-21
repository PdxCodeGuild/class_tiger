import csv
def loads_data(path):
    '''
    #funct return 2 things request both 72
    '''
    with open(path, 'r') as f: #note a csv is a text becuz ,seperated
        lines = f.read().split('\n') #split into lines
        header = lines[0].split(',') #get the header
        contacts = [] #create a list
        for i in range(1, len(lines)):
            comma_sep_v_list = lines[i].lower().split(',')
            contact_dict = dict(zip(header, comma_sep_v_list))
            contacts.append(contact_dict) #make list of dictio
        return contacts, header

def add_record(contacts, header):
    '''Function uses the two return argument of previous to make change'''
    new_contact = {'Name': '', 'Favorite fruit': '', 'Favorite color': ''}
    for attrib in header:
        value = input(f'Add {attrib} please: ').strip().lower()
        new_contact[attrib] = value
    contacts.append(new_contact)
    return contacts

def retrieve_record(contacts, header):
    record_name = input('what\'s the contact\'s name?').strip().lower()
    for i in range(len(contacts)):
        if contacts[i]['name'].lower() == record_name:
            print(contacts[i].values())
        else:
            alternative = input('There no such record add a new one? (yes/no) ').strip().lower()
            if alternative == 'yes':
                add_record(contacts, header)
            else:
                break

def update_record(contacts):
    record_na = input('what\'s the contact\'s name?').strip().lower()
    column = input('what do you want to change?').strip().lower()
    #index = [i for i, contact in enumerate(contacts) if contact['name'] == record_na]
    for i in range(len(contacts)):
            if contacts[i]['name'] == record_na:
                contacts[i][column] == input('what\'s the new information? ').strip().lower()
    return contacts

def Delete_record(contacts):
    contact_Delete = input('what\'s the contact\'s name?')
    for i in range(len(contacts)):
        print(contacts[i]['name'])
        if contacts[i]['name'] == contact_Delete:
            contacts.pop(i)
            break
    return contacts

def save_contacts(contacts, path, header):
    """
    turn back into big string to be able to save csv
    """
    lines = [','.join(header)]
    for contact in contacts: # loop over contacts
        row = ','.join(contact.values()) # turn contact values into comma separated string
        lines.append(row)  # add row to lines
    big_string = '\n'.join(lines) # turn lines list into string
    with open(path, 'w') as f: #writing changes back to file
        f.write(big_string)


def prompt():
    possible_input = ['add a record', 'retrieve a record', 'delete a record', 'update a record', 'quit', 'help']
    input_rank = [1, 2, 3, 4, 5, 6]
    user_input = ''
    print('What would you like to do?')
    for i in range(len(possible_input)):
        print(f'{input_rank[i]}: {possible_input[i]}')
    try:
        user_input = int(input('enter choice: '))
    except ValueError:
        print('You can only choose between 1 and 6.')
    return user_input

def main():
    path = 'Contacts.csv'
    contacts, header = loads_data(path)
    while True:
        user_input = prompt()
        if user_input == 1:
            add_record(contacts, header)
        elif user_input == 2:
            retrieve_record(contacts, header)
        elif user_input == 3:
            Delete_record(contacts)
        elif user_input == 4:
            update_record(contacts)
        elif user_input == 5:
            break
        elif user_input == 6:
            print(prompt)

    save_contacts(contacts, path, header)

if __name__ == '__main__':
    main()




