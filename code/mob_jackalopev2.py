
import random
import string
jackalopes = [{'name':'george','age':0,'sex':'m','preg':False},{'name':'sally','age':0,'sex':'f','preg':True}]

def is_pregnant(jackalopes):
    # if true change to false and make two babies
    for i in range(len(jackalopes)):
        if jackalopes[i]['preg']:
            jackalopes[i]['preg'] = False
            baby(jackalopes)
            baby(jackalopes)
    return jackalopes


def pregnant(jackalopes):
    # check true/false if pregnant
    for i in range(len(jackalopes)):
        if jackalopes[i]['sex'] == 'f':
            if  3 < jackalopes[i]['age']  < 9:
                if jackalopes[i]['preg'] == False:
                    if i == 0:
                        if jackalopes[i+1]['sex'] == 'm' and 3 < jackalopes[i+1]['age']  < 9:
                            jackalopes[i]['preg'] = True
                    elif i == len(jackalopes)-1:
                        if jackalopes[i-1]['sex'] == 'm' and 3 < jackalopes[i-1]['age']  < 9:
                            jackalopes[i]['preg'] = True
                    else:
                        if jackalopes[i-1]['sex'] == 'm' or jackalopes[i+1]['sex'] == 'm' and 3 < jackalopes[i-1]['age']  < 9 or 3 < jackalopes[i+1]['age']  < 9:
                            jackalopes[i]['preg'] = True
    return jackalopes

def baby(jackalopes):
    sex = random.choice(['m','f'])
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    name = ''
    name += random.choice(consonants) + random.choice(vowels) + random.choice(consonants) + random.choice(vowels)
    new_baby = {'name':name,'age':0,'sex':sex,'preg':False}
    jackalopes.append(new_baby)
    return jackalopes

def age(jackalopes):
    for i in range(len(jackalopes)):
        jackalopes[i]['age'] += 1
    return jackalopes

def die(jackalopes):
    for i in range(len(jackalopes) - 1, -1, -1):
        # print(jackalopes[i]['age'])
        if jackalopes[i]['age'] > 10:
            jackalopes.pop(i)
    return jackalopes

year= 0
population = len(jackalopes)

while population < 1000 and population >= 2:
    population = len(jackalopes)
    year += 1
    jackalopes = die(jackalopes)
    jackalopes = age(jackalopes)
    jackalopes = is_pregnant(jackalopes)
    jackalopes = pregnant(jackalopes)
    random.shuffle(jackalopes)

<<<<<<< HEAD
    print(name)
=======
print(year, population)
print("\n")
>>>>>>> ab4aef2f37f431c992164d7bf17796c1f8a1af45



print('    \\\\ ')
print('     \\\\__ ')
print('     ( _\ ')
print('      / \__ ')
print('     / _/`"` ')
print('     {\  )_ ')
print('        `"""` ')
