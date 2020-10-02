#Substitution Ciphers
#How to transform data from one thing to another
#Take some kind of info and map it to something else
#You want to send a secret message to your generals in the field, but you don't want your enemies to know what it says if they capture it. So you create a mapping system for each letter to map to a secret letter.
"""
Dictionaries are very helpful for re-mapping something to something else.
Map a fixed amount of data to another fixed amount of data.
Ask yourself what are you storing in the key and value and can you use that to help you in the mapping?
"""

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

#this will make our decode table. we can take the items and reverse the value and the key
decode_table = {}

for key, value in encode_table.items():
    decode_table[value] = key


def encode(plain_text):
    cipher = ''

    for char in plain_text:
        if char.isspace():
            cipher += ' '
        else: cipher += encode_table[char.upper()]

    return cipher

def decode(cipher_text):
    plain_text = ' '
    for char in cipher_text:
        if char.isspace():
            plain_text += ' '
        else: 
            plain_text += decode_table[char.upper()]
    return plain_text

cipher = encode("Dictionaries are awesome")
print(cipher)

reversed_plain_text = decode(cipher)
print(reversed_plain_text)

#print(encode("Dictionaries are awesome"))