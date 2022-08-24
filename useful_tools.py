from math import floor, log10

def roun_to(num, n):
    '''
    Rounding a number to n significant digits
    '''
    return round(num, n - int(floor(log10(abs(num)))) - 1)

print(roun_to(2344321, 3))
