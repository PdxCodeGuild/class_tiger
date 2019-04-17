import string
import math

with open('../../../watchers_of_the_sky.txt') as source_title:
    contents = source_title.read()

def character(x):
    char_num = contents.replace(" ", "")
    char_num = contents.replace("\n", "")
    for i in string.punctuation:
        char_num = contents.replace("i", "")
    char_num = len(char_num)
    return char_num

def words(x):
    word_num = contents.split(" ")
    word_num = len(word_num)
    return word_num

def sentences(x):
    sen_num = contents.replace("!", ".")
    sen_num = contents.replace("?", ".")
    sen_num = contents.split(".")
    sen_num = len(sen_num)
    return sen_num

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
def ari(x):
    char_num = character(x)
    word_num = words(x)
    sen_num = sentences(x)
    ari_score = math.ceil((4.71 * (char_num/word_num)) + (0.5 * (word_num/sen_num)) - 21.43)
    if ari_score > 14:
        ari_score = 14
    # ari_score = int(math.ceil(ari_score))
    return ari_score
i = ari(contents)


# print(ari_scale[i]['ages'])
print(f'The ARI for {source_title.name} is {i}. \nThis corresponds to a {ari_scale[i]["grade_level"]} level of difficulty. \nThat is suitable for an average person {ari_scale[i]["ages"]} years old.')