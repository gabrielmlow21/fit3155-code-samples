import string

def boyer_moore(array, pattern):
    # if pattern == None or len(pattern) == 0:
    #     return 0
    # if array == None:
    #     return -1
    bad_character_table = precompute_bad_character_table(pattern)
    suffix_table = preprocess_suffix_table(pattern)    
    i = len(pattern) - 1
    j = len(pattern) - 1
    while i < len(array):
        while pattern[j] == pattern[i]:
            if j == 0:
                return i    # we found the match
            i = i - 1
            j = j - 1
        i = i + max(suffix_table[len(pattern)-1-j], bad_character_table(array[i]))
    return -1

# print(preprocess_suffix_table('baidai')) = [6, 7, 8, 9, 10, 11]
def preprocess_suffix_table(pattern):
    table = [-1] * len(pattern)
    compute_prefix(pattern, table)
    compute_suffix(pattern, table)
    return table

def compute_prefix(pattern, table):
    last_prefix_position = len(pattern)
    # comparing string from right to left (starting from length of pattern)
    # abcdefg
    # abc
    i = len(pattern)
    while i > 0:
        if is_prefix(pattern, i):
            last_prefix_position = i
        table[len(pattern)-i] = last_prefix_position - i + len(pattern)
        i = i - 1

def compute_suffix(pattern, table):
    i = 0
    while i < len(pattern)-1:
        match_length = suffix_length(pattern, i)
        table[match_length] = len(pattern) - 1 - i + match_length
        i = i + 1

# checks if i and j matches until the end of the string
# j cannot be from the beginning
def is_prefix(pattern, index):
    i = index
    j = 0
    while i < len(pattern):
        if pattern[i] != pattern[j]:
            return False
        i = i + 1
        j = j + 1
    return True

def suffix_length(pattern, index):
    match_length = 0
    j = len(pattern) - 1
    i = index
    while i >= 0 and pattern[i] == pattern[j]:
        match_length = match_length + 1
        i = i - 1
        j = j - 1
    return match_length

# adds len(pattern) to every character that is not in the pattern
# adds len(pattern) to the last character of the pattern in case it is unique
def precompute_bad_character_table(pattern):
    table = [None] * len(string.ascii_lowercase)
    for i in range(len(string.ascii_lowercase)):
        table[i] = len(pattern)
    for t in range(len(pattern)-1):
        table[pattern[t]] = max(1, len(pattern)-t-1)
    # if the last character of the pattern is smaller
    # e.g. test (from test) - 121
    if table[pattern[len(pattern)-1]] < len(pattern):   
        table[pattern[len(pattern)-1]] = 1
    return table

# print(suffix_length('baidai', 0))
# print(suffix_length('baidai', 1))
# print(suffix_length('baidai', 2))
# print(suffix_length('baidai', 3))
# print(suffix_length('baidai', 4))

print(boyer_moore('baidai', 'ai'))