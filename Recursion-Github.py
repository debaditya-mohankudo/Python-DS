#!/usr/bin/env python
# coding: utf-8

# ## Fibonacci  - simplest and most elegant ( not most efficient)

# In[45]:


def fib(n): # not very efficient -> too many duplicate calls with increase in input
    """asssume n> 1"""
    if n==0 or n==1:
        return 1
    else:
        return  fib(n-1) + fib(n-2)


# In[46]:


get_ipython().run_cell_magic('timeit', '', 'fib(33)')


# ![alt text](fib.png "Fibonacci")

# ## Fibonacci using memoization - storing earlier recursion results in a dictionary

# In[47]:


from collections import defaultdict

def fib(n, memoize=None):
    if memoize is None:
        memoize = defaultdict(int)
        
    if n==0 or n==1:
        memoize[n] = 1
        return memoize[n]
    else:
        
        if memoize[n] != 0:
            return memoize[n]
        else:
            memoize[n-1], memoize[n-2] = fib(n-1, memoize), fib(n-2, memoize)
            return memoize[n-1] + memoize[n-2]


# In[48]:


get_ipython().run_cell_magic('timeit', '', 'fib(33)')


# ## fibonacci using simple iteration

# In[49]:


# better than recursion fibonacci ??
def fib(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x+y
    return y


# In[50]:


get_ipython().run_cell_magic('timeit', '', 'fib(33)')


# ## Find all combinations given a string using recursion

# In[10]:


def remainingChar(str_S, char_index):
    return str_S[:char_index] + str_S[char_index+1:] 


# In[11]:


def all_combinations(str_S):
    res_L = []

    if len(str_S) == 1:#base case
        return str_S

    else: #recursive case
        for i, char in enumerate(str_S):
            for combi in all_combinations(remainingChar(str_S, i)):
                res_L.append(char + combi)
        return res_L


# In[12]:


get_ipython().run_cell_magic('timeit', '', "all_combinations('abcde')")


# ## Find all combinations given a string using recursion - list comprehension

# In[13]:


def all_combinations(str_S): #base case
    if len(str_S) <= 1:
        return str_S
    return [char + combinations for i, char in enumerate(str_S) for combinations in all_combinations(remainingChar(str_S, i))]


# In[14]:


get_ipython().run_cell_magic('timeit', '', "all_combinations('abcde')")


# ## Find all combinations given a string using tail recursion

# In[17]:


def all_combinations(str_S, word='', res_L=None):
    if res_L is None:
        res_L = []

    if len(str_S) == 1:#base case
        res_L.append(word + str_S)
        #return str_S no need to return here, tail recursion -> incremental output part of input

    else: #recursive case
        for i, char in enumerate(str_S):
            all_combinations(remainingChar(str_S, i), word + char, res_L)
    return res_L


# In[18]:


get_ipython().run_cell_magic('timeit', '', "all_combinations('abcde')")


# ## Find GCD of two numbers - recursion ( Euclid's algorithm O(log(n))

# In[30]:


def find_gcd(num_N1, num_N2):
    if num_N1 == 0:
        return num_N2
    elif num_N2 == 0:
        return num_N1
    elif num_N1 == 1 or num_N2 == 1:
        return 1
    return find_gcd(min(num_N1, num_N2), max(num_N1, num_N2) % min(num_N1, num_N2))


# In[31]:


find_gcd(3, 27)


# In[32]:


find_gcd(3, 5)


# ## check palindrome

# In[36]:


def is_pal(str_S):
    if len(str_S) == 1 or len(str_S) == 0:#base case
        return True
    else:#recursive case
        if str_S[0] == str_S[-1]:
            return is_pal(str_S[1:-1])
        else:
            return False


# In[39]:


is_pal('racecar')


# In[40]:


is_pal('abddba')


# In[41]:


is_pal('adgdg')


# ## decimal to binary

# In[42]:


def dec_to_binary(number):
    if number < 2:
        return str(number)
    else:
        reminder = number % 2
        remaining = number // 2
        return dec_to_binary(remaining) + str(reminder)


# In[43]:


dec_to_binary(11)


# In[44]:


dec_to_binary(16)


# In[ ]:




