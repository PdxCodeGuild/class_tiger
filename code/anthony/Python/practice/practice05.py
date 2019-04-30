import string
# Practice 5 Comprehensions

# Problem 1:
# Write a comprehension to generate the first 10 powers of two.
print([pow(2, n) for n in range(10)])

# Problem 2:
# Write a comprehension to generate the first 10 even numbers
print([n for n in range(1, 21) if n % 2 == 0])

# Problem 3:
# Write a dictionary comprehension to swap keys and values of a given dictionary. So {'a': 1, 'b': 2} would become {1:'a', 2:'b'}
test_dict = {'a': 1, 'b': 2}
print({key:value for value, key in test_dict.items()})

# Problem 4:
# Write a dictionary comprehension to print each letter of the alphabet and its corresponding ASCII code
print({c : ord(c) for c in string.ascii_lowercase})