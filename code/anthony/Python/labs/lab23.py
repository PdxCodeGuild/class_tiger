
def open_contacts():
    contacts_list = []
    with open('./text_files/contacts.csv', 'r') as f:
        lines = f.read().split('\n')
    for line in lines:
        contacts_list.append(line.split(','))
    return convert_to_dict(contacts_list)

def convert_to_dict(contacts):
    contacts_list = []
    for i in range(1, len(contacts)):
        temp_dict = {}
        for j in range(len(contacts[0])):
            temp_dict[contacts[0][j]] = contacts[i][j]
        contacts_list.append(temp_dict)
    return contacts_list

def convert_to_csv(contacts):
    contact_string = 'name,address,phone'
    for i in range(len(contacts)):
        contact_string += '\n'
        contact_string += contacts[i]['name'] + ',' + contacts[i]['address'] + ',' + contacts[i]['phone']
    save_contacts(contact_string)

def save_contacts(contacts):
    with open('./text_files/contacts.csv', 'w') as f:
        f.write(contacts)

def menu():
    menu_list = ['Create new contact', 'Look up contact', 'Update contact', 'Delete contact', 'Quit']
    choice_list = [1, 2, 3, 4, 5]
    user_choice = ''

    print("Select an option below: \n -------------------------")
    for i in range(len(menu_list)):
        print(f"({choice_list[i]}) {menu_list[i]}")

    while user_choice not in choice_list:
        try:
            user_choice = int(input())
        except ValueError:
            print("That is not a valid option. Try entering 1-5.")
    return user_choice

def create_contact(contacts):
    new_contact = {}
    name = input("Enter the name for your new contact: ")
    address = input("Enter the address of your new contact: ")
    phone = input("Enter the phone number of your new contact: ")

    new_contact = {'name':name, 'address':address, 'phone':phone}
    contacts.append(new_contact)
    return contacts


def retrieve_contact(contacts):
    user_input = input("Enter the contact to be looked up: ")
    if user_input == 'all':
        for contact in contacts:
            print(contact.values())
    else:
        for i in range(len(contacts)):
            if contacts[i]['name'].lower() == user_input.lower():
                print(contacts[i].values())
            

def update_contact(contacts):
    user_input = input("Enter the name of the contact to be updated: ")
    for i in range(len(contacts)):
        if contacts[i]['name'].lower() == user_input.lower():
            print(contacts[i].values())
            contacts[i]['name'] = input("Enter the name for the contact: ")
            contacts[i]['address'] = input("Enter the address for the contact: ")
            contacts[i]['phone'] = input("Enter the phone number for the contact: ")
    return contacts
def delete_contact(contacts):
    user_input = input("Enter the contact to be deleted: ")
    for i in range(len(contacts)):
        if contacts[i]['name'].lower() == user_input.lower():
            contacts.pop(i)
            break
    return contacts

def main():
    contact_list = open_contacts()
    while True:
        
        user_choice = menu()
        if user_choice == 1:
            contact_list = create_contact(contact_list)
        elif user_choice == 2:
            retrieve_contact(contact_list)
        elif user_choice == 3:
           contact_list = update_contact(contact_list)
        elif user_choice == 4:
            contact_list = delete_contact(contact_list)
        else:
            break
         
    convert_to_csv(contact_list)

if __name__ == '__main__':
    main()