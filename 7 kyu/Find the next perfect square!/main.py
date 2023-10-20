import math

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    return ((math.sqrt(sq) + 1) ** 2) if math.sqrt(sq) % 1 == 0 else -1
