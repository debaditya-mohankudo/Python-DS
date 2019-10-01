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
#decimal to binary
def dec_to_binary(number):
    if number == 1 or number == 0:
        return number
    else:
        reminder = number % 2
        remaining = number // 2
        return str(dec_to_binary(remaining)) + str(reminder)
############################################################
