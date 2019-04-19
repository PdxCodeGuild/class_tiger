import string, re, math
with open('busterbeartwins.txt', 'r', encoding= 'utf-8') as f: # this is because my file is already in this folder
    book = f.read()# gives one big string

translator = str.maketrans('', '', string.punctuation) #removes all punctuation
no_punct = book.translate(translator)
low_format = no_punct.lower()
word_list = low_format.split()

def count_words():
    count = 0
    for i in word_list:
        count += 1
    return count

def count_char():
    count2 = 0
    for word in word_list:
        for char in word:
            count2 += 1
    return count2

def sentences():
    d = book.replace('\n','')
    d = d.lower()
    sentence_list = re.split(r'[.!?]+', d)  #this determines the limits of sentences
    return sentence_list


ari_score = 4.71 * count_char()/count_words() + 0.5 * count_words()/len(sentences()) - 21.43
ari_score = math.ceil(ari_score)
if ari_score > 14:
    ari_score =14

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

Grade = ari_scale[ari_score]
print(Grade['grade_level'])


print(f'The ARI for busterbeartwins.txt is {ari_score}\nThis corresponds to a {Grade["grade_level"]} of difficulty\nthat is suitable for an average person {Grade["ages"]} years old.')


