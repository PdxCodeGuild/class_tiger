# Practice problems

# Problem 1:
# Get a string fromt he user, print out another string, doubling every letter.
def double_letters(str):
    doubled_string = ''
    for x in str:
        doubled_string += x*2
    return doubled_string
#print(double_letters("hello"))

# Problem 2:
# Write a function that takes a string, and returns a list of strings, each missing a different character.
def missing_char(str):
    missing_list = []
    for x in str:
        missing_list.append(str.replace(x, '', 1))
    return missing_list
#print(missing_char("kitten"))

# Problem 3:
# Return the letter that appears the latest in teh english alphabet.
def latest_letter(str):
    largest_letter = 'a'
    for x in str:
        if x > largest_letter:
            largest_letter = x
    return largest_letter
#print(latest_letter("pneumonoultramicroscopicsilicovolcanoconiosis"))

# Problem 4:
# Write a function that returns the number of occurances of 'hi' in a given string.
def count_hi(str):
    counter = 0
    for i in range (0, len(str)-1):
        if str[i] == 'h':
            if str[i + 1] == 'i':
                counter += 1
    return (counter)
# print(count_hi("ahibhichi"))

# Problem 5:
# Write a function that returns True if a given string contains the same number of 'cat' as 'dog'
def cat_dog(str):
    start = 0
    end = 3
    cat_count = 0
    dog_count = 0

    while end <= len(str):
        if str[start:end] == 'cat':
            start += 3
            end += 3
            cat_count += 1
        elif str[start:end] == 'dog':
            start += 3
            end += 3
            dog_count += 1
    if cat_count == dog_count:
        return True
    return False
# print(cat_dog("catdogcatdog"))

# Problem 6:
# Return the number of letter occurances in a string
def count_letter(letter, word):
    counter = 0
    for s in word:
        if s == letter:
            counter += 1
    return counter
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis'))

# Problem 7:
# Convert input stings to lowercase without any surrounding whitespace.
def lower_case(str):
    str = str.lower()
    str = str.strip()
    return str
# print(lower_case("        NANNANANANA BATMAN        "))