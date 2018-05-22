
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = "{}[]!@#$%^&*()_+-=`~;',./:?< >"
def alphabet_position(letter):
    letter = letter.lower()
    if letter.isalpha():
        return alphabet.find(letter)
    else:
        return letter    

def rotate_character(char, rot):
    if char in punctuation:
        return char
    upper = char.isupper() 
    current_pos = alphabet_position(char)
    newnew = int(current_pos) + int(rot)
    if newnew > 25:
        newnew = newnew - 25
    new_char = alphabet[newnew]
    if upper: 
        return new_char.upper()
    else:    
        return new_char.lower() 
