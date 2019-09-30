"""
Find all combination of chars given a string
"""

def remainingChar(str_S, char_index):
    return str_S[:char_index] + str_S[char_index+1:]    

def all_combinations(str_S):
    res_L = []

    if len(str_S) == 1:#base case
        return str_S

    else: #recursive case
        for i, char in enumerate(str_S):
            for combi in all_combinations(remainingChar(str_S, i)):
                res_L.append(char + combi)
        return res_L

def all_combinations(str_S):
    if len(str_S) <= 1:
        return str_S
    return [char + combinations for i, char in enumerate(str_S) for combinations in all_combinations(remainingChar(str_S, i))]

def all_combinations(str_S, word='', res_L=None):
    if res_L is None:
        res_L = []

    if len(str_S) == 1:#base case
        res_L.append(word + str_S)
        return

    else: #recursive case
        for i, char in enumerate(str_S):
            all_combinations(remainingChar(str_S, i), word + char, res_L)
        return res_L

all_combinations('abc')
>>> ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']