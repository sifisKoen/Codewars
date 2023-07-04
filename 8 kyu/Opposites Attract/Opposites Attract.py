def lovefunc( flower1, flower2 ):
    """
        Args:
            flower1 (int)   |
                            |--> Both arguments are integers.
            flower2 (int)   |
        
        In this function we check 
        -> If one of the flower's petals are even and the other is odd. So to return [True]
           See the if statement.
        
        Additional:
            I also add a [try / except] functionality so to make the function more robust.
            So in case one of the inputs are not a number to print a TypeError.
    """
    try:
        if (
                (flower1 % 2 == 0) and (flower2 % 2 != 0)
            ) or \
            (
                (flower1 % 2 != 0) and (flower2 % 2 == 0)
            ):
            return True

        return False
    except TypeError:
        print("Wrong value type! Both values should be integers.")