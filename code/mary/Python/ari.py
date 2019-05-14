#ari.py
with open('little.txt', 'r', encoding="utf-8-sig" ) as f:
    contents = f.read()
import math
file_name = 'little.txt'
characters = contents
characters = list(characters)
while ' ' in characters:
    characters.remove(' ')
characters = len(characters)
words = contents
words = words.replace('\n','')
words = words.split(' ')
while ' ' in words:
    words.remove(' ')
words = len(words)
sentences = contents
sentences = sentences.replace('\n',' ')
sentences = sentences.split('.')
while ' ' in sentences:
    sentences.remove(' ')
sentences = len(sentences)
def ari():
    ari = (float(4.71)*(characters/words))+(float(0.5)*(words/sentences))-float(21.43)
    ari = round(ari)
    if (ari>14):
        return(14)
    return ari()

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
grade_level=ari_scale[ari()]
output=f"The ARI for {file_name} is {ari()}."
output+=f"\nThis corresponds to a {grade_level['grade_level']} level of difficulty"
output+=f"\nthat is suitable for {grade_level['ages']} years old."
print(output)
