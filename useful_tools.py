from math import floor, log10

def roun_to(num, n):
    '''
    Rounding a number to n significant digits
    '''
    return round(num, n - int(floor(log10(abs(num)))) - 1)

def f1():
    print('hello world')

print(roun_to(2344321, 3))
f1()
