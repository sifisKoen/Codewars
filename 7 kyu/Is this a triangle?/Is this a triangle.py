def is_triangle(a, b, c):
    """
    A + B > C    and     
    B + C > A    and
    C + A > B
    Where A, B and C are length of sides of the triangle.
    """
    
    return (a + b > c) and (b + c > a) and (c + a > b)