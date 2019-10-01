#palindrome
def is_pal(str_S):
    if len(str_S) == 1:#base case
        return True
    else:#recursive case
        if str_S[0] == str_S[-1]:
            return is_pal(str_S[1:-1])
        else:
            return False
        
###########################################

def dec_to_binary(number):
    if number < 2:
        return str(number)
    else:
        reminder = number % 2
        remaining = number // 2
        return dec_to_binary(remaining) + str(reminder)
    
############################################################

def find_gcd(num_N1, num_N2):
    if num_N1 == 0:
        return num_N2
    elif num_N2 == 0:
        return num_N1
    elif num_N1 == 1 or num_N2 == 1:
        return 1
    return find_gcd(min(num_N1, num_N2), max(num_N1, num_N2) % min(num_N1, num_N2))
