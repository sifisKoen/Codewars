def validate_pin(pin):
    """
        isdigit() treats the "-" as non-digit character.
    """
        
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()