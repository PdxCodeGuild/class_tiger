#step 1 you cannot multiply
# without concatenating if you want one word back
#you can only add a string in a string and '' is one
#can't do return for ... unless in [] list
def double_letter(word):
    var=''
    for letter in word:
        var += letter*2
    return var

print(double_letter('champion'))
print(double_letter('drag'))

#step 2 Write a function that takes a string,
# and returns a list of strings, each missing a different character.
#return as a list works if returning manipulated word n times
#make a list with a letter position n add remaining letters

def missing_char(word):
    return [word[:letter] + word[letter+1:] for letter in range(len(word))]

print(missing_char('bloody'))


#step 3 Return the letter that appears the latest in the english alphabet.
#function sorted arranges alphabetically and all you do is choose last
def latest_letter(word):
    return sorted(word)[-1]
print(latest_letter('mazda'))

#step 4 Write a function that returns
# the number of occurances of 'hi' in a given string.
#function count gives number of occ

def count_hi(word):
    return word.count('hi')

print(count_hi('hihihihi'))

#step 5 Write a function that returns True if a given string
#  contains the same number of 'cat' as it does 'dog'
# to return true and false just write condition
def cat_dog(word):
    return word.count('cat') == word.count('dog')

print(cat_dog('catdogcat'))

#step 6 Return the number of letter occurances in a string.
#count can take a variable as an arg
def count_letter(letter, word):
        return word.count(letter)
print(count_letter('o','moribond'))

#step 8 Convert input strings to lowercase
#  without any surrounding whitespace.
#two methods follow one another
def lower_case(word):
    return word.strip().lower()

print(lower_case(' HUUUUNNEYYY  '))