
def check_pal(word):
    check_word = "".join(reversed(word))
    if check_word == word:
        return True
    else:
        return False
print(check_pal('tacocat'))