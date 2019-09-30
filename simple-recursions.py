def is_pal(str_i): #palindrome
    if len(str_i) == 1:
        return True
    else:
        if str_i[0] == str_i[-1]:
            return is_pal(str_i[1:-1])
        else:
            return False

def fib(n): # not very efficient -> too many duplicate calls with increase in input
    """asssume n> 1"""
    if n==0 or n==1:
        return 1
    else:
        return  fib(n-1) + fib(n-2)
