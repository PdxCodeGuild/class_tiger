#ROT Cipher
import string as s
def rot13():
    input_prompt = input(f'input a string')
    lower = input_prompt.lower()
    #lower = [lower[i] for i in range(0, len(lower))]
    #splitting jammed together word into list of 1 i.e if 3 pass 3 in range
    rot1 = 'nopqrstuvwxyzabcdefghijklm'
    rot13_list = [rot1[i] for i in range(0, len(rot1))]
    alphabet_list = [s.ascii_lowercase[i] for i in range(0, len(s.ascii_lowercase))]
    rot_dict = {key:value for key,value in zip(alphabet_list,rot13_list)}
    output = ''
    for i in lower:
       if i in rot_dict.keys():
            output += rot_dict[i]
    return output


