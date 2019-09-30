def is_pal(str_i): #palindrome
    if len(str_i) == 1:
        return True
    else:
        if str_i[0] == str_i[-1]:
            return is_pal(str_i[1:-1])
        else:
            return False
##################################################################################
def fib(n): # not very efficient -> too many duplicate calls with increase in input
    """asssume n> 1"""
    if n==0 or n==1:
        return 1
    else:
        return  fib(n-1) + fib(n-2)
##################################################################################

from collections import defaultdict
def fib(n, memoize=None): # more efficient than the earlier version as it stores the incremental results and reuses
    if memoize is None:
        memoize = defaultdict(int)
        memoize[0] = 1
        memoize[1] = 1
    if n==0 or n==1:
        return 1
    else:
        
        if memoize[n] != 0:
            return memoize[n]
        else:
            memoize[n-1], memoize[n-2] = fib(n-1, memoize), fib(n-2, memoize)
            return memoize[n-1] + memoize[n-2]
################################################################################
# better than recursion fibonacci ??
def fib(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x+y
    return x
#################################################################################
