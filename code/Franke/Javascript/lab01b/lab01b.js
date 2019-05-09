// #Write a program that prompts the user for a string,
// #  and encodes it with ROT13. For each character, find the corresponding character,
// # add it to an output string. Notice that there are 26 letters in the English language,
// # so encryption is the same as decryption.

// import string as s
// def rot13():
//     input_prompt = input(f'input a string')
//     lower = input_prompt.lower()
// #lower = [lower[i] for i in range(0, len(lower))]
// #splitting jammed together word into list of 1 i.e if 3 pass 3 in range
//     rot1 = 'nopqrstuvwxyzabcdefghijklm'
//     rot13_list = [rot1[i] for i in range(0, len(rot1))] #adding str to list with list comp
//     alphabet_list = [s.ascii_lowercase[i] for i in range(0, len(s.ascii_lowercase))]
//     print(alphabet_list)
//     rot_dict = {key: value for key, value in zip(alphabet_list, rot13_list)}
//     output = ''
//     for i in lower:
//        if i in rot_dict.keys():
//             output += rot_dict[i]
//     return output
//     print(output)
////////////
// for char in text:
//         index = alphabet.find(char)
//         output += alphabet_rotated[index]
//     return output

var input_prompt = prompt('Input a string');
function rot13(input_prompt) {
    let input = input_prompt.toLowerCase();
    var rot = 'nopqrstuvwxyzabcdefghijklm';
    var alphabet = 'abcdefghijklmnopqrstuvwyxz';
    var output = '';
    for (element of input) {
       let index = alphabet.indexOf(element);
       output += rot[index];

    }
alert(`The rot13 of  ${input_prompt} is ${output}`);
}

rot13(input_prompt);