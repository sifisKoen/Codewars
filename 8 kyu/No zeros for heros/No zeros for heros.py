def no_boring_zeros(n):
    
    # 1st Checks if this number n is 0, then returns 0.
    # 2nd Converts the n into string and using the rstrip() method, of python,
    # removes all the zeros from the end of the number.
    # 3rd, we convert the final number into int and return it.
    return int(str(n).rstrip("0")) if n != 0 else 0