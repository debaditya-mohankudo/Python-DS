


def is_happy(int_tc, res = None):
    if res is None:
        res = []
    if len(res) > len(set(res)):
        return False # same series ll continue
    sum_square = sum([digit ** 2 for digit in get_all_digits(int_tc)])

    if sum_square == 1:
        return True
    else:
        res.append(sum_square)
        return is_happy(sum_square, res)
    
def find_next_happy(int_tc):
    if is_happy(int_tc):
        return int_tc
    else:
        return find_next_happy(int_tc + 1)

def get_all_digits(number):
    """gets all the digits from the number right to left"""
    while(number > 0):
        yield int(number % 10)
        number = (number - number % 10) / 10

find_next_happy(6)
>>> 7
