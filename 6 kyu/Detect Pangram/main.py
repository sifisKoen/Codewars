import string

def is_pangram(s):
    
    letters = string.ascii_lowercase
    
    for letter in s.lower():
        if letter in letters:
            letters = letters.replace(letter, "")
    
    
    if letters == "":
        return True
    else:
        return False