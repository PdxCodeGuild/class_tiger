'''
Lab : Roadtrip

'''

city_to_accessible_cities = {
    'Boston' : { 'New York', 'Albany', 'Portland'},
    'New York' : { 'Boston', 'Albany', 'Philedelphia'},
    'Albany' : { 'Boston', 'New York', 'Portland'},
    'Portland' : {'Boston', 'Albany' },
    'Philedelphia' : { 'New York' },
}

def hop(user_input):
    print('\n')
    print(f'Your hop options are {city_to_accessible_cities[user_input]}')
    print('\n')
    accessible_cities = city_to_accessible_cities[user_input]
    for city in accessible_cities:
        print('\n')
        print('********')
        print(city + ' can hop to:')
        print(city_to_accessible_cities[city])

def main():

    while True:
        print('\n')
        user_input = input('Where would you like to go? > ')
        if user_input == 'exit':
            print('Goodbye!')
            break

        if user_input in city_to_accessible_cities:
            hop(user_input)
        else:
            print('Your input was not found in our system')

main()
