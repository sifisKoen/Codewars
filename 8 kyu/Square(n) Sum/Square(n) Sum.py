def square_sum(numbers):
    """
        number ** 2 -> squares each element in the numbers list. 
        The sum of these squared values is then calculated using the sum() function,
        and assigned to the square variable.
    """
    
    square = sum(number ** 2 for number in numbers)
    
    return square 