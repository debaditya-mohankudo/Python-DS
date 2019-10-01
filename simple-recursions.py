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
