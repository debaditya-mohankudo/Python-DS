def is_pal(str_i): #palindrome
    if len(str_i) == 1:
        return True
    else:
        if str_i[0] == str_i[-1]:
            return is_pal(str_i[1:-1])
        else:
            return False
