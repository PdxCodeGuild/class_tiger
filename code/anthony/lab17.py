import string

def anagram_checker(str1, str2):
    str1.lower()
    str2.lower()
    list1 = []
    list2 = []
    for c in str1:
        if c in string.ascii_lowercase:
            list1.append(c)
    for c in str2:
        if c in string.ascii_lowercase:
            list2.append(c)
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    return False

print(anagram_checker("abc123", "c1b2a4"))
def palindrom_checker(palindrome):
    palindrome2 = palindrome
    palindrome = palindrome[::-1]
    if palindrome == palindrome2:
        return True
    return False

print(palindrom_checker('racecar'))