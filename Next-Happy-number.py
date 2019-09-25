"""
For a given non-negative integer N, find the next smallest Happy Number.
A number is called happy if it leads to 1 after a sequence of steps where in each step number is replaced by sum of squares of its digit 
that is if we start with Happy Number and keep replacing it with digits square sum, we reach 1.
"""



def is_happy(int_tc, sum_squares=None, res = None):
    if res is None:
        res = []
    if sum_squares is None:
        sum_squares = int_tc
    sum_squares = sum([digit ** 2 for digit in get_all_digits(sum_squares)])

    if sum_squares == 1:
        return True
    
    if sum_squares in res:
        return False # same series continues infinitely
    else:
        res.append(sum_squares)
        return is_happy(int_tc, sum_squares, res)
    
def find_next_happy(int_tc):
    int_tc += 1
    if is_happy(int_tc):
        return int_tc
    else:
        return find_next_happy(int_tc)

def get_all_digits(number):
    """gets all the digits from the number right to left"""
    while(number > 0):
        yield int(number % 10)
        number = (number - number % 10) / 10


find_next_happy(6)
>>> 7
