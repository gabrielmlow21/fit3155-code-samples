def boyer_moore():
    return

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


print(suffix_length('baidai', 0))
print(suffix_length('baidai', 1))
print(suffix_length('baidai', 2))
print(suffix_length('baidai', 3))
print(suffix_length('baidai', 4))

print(preprocess_suffix_table('baidai'))