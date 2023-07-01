import re

def to_camel_case(text):
    """
    This function converts a given string into a camel case—dashes or underscores delimit the string words.
    The first word in the final result should be capitalized only if the original word was capitalized.
    The next words should be always capitalized.
    
    Arg:
        text (str) -> The input string that should be camel case.
    
    Returns:
        str -> The final result, is the string camel case.
    """
    # Check if the string is empty.
    if text == "":
        return ""
    
    # Ensure that the input is a string.
    if not isinstance(text, str):
        raise ValueError("Input text must be a string")
    
    # Split the string with - or _ using regular expression.
    # Explanation: split("-|_", text) -> split the text if there is - or _
    splited_text = re.split("-|_", text)
    
    # Create a variable to help us with our final result.
    # And add in this variable the first word.
    final_text = [splited_text[0]]
    
    # First, we capitalize the words of our list. 
    # Except for the first one.
    # And we add each word to our final result list.
    final_text += [ word.capitalize() for word in splited_text[1:]]
    
    # Finally, we join the final result in one word.
    return "".join(final_text)
