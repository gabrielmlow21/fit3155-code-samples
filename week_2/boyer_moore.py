def boyer_moore():
    return

# checks if i and j matches until the end of the string
# j cannot be from the beginning
def is_prefix(pattern, index):
    j = 1
    for i in range(index+1, len(pattern)):
        if pattern[i] != pattern[j]:
            return False
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


print(suffix_length('baidai', 2))