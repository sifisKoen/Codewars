def is_isogram(string):
    string = string.casefold()
    
    for letter in string:
        if (string.count(letter) >= 2):
            
            return False
    
    return True