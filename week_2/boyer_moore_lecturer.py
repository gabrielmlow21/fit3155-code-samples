import string

# bad character table
def bad_character_table(pattern):
    alphabets = string.ascii_lowercase
    matrix = [-1] * len(pattern)   
    for i in range(len(pattern)): matrix[i] = [-1] * len(alphabets)
    for i in range(len(alphabets)):
        for k in range(len(pattern)):
            R = -1
            for j in range(k):
                if alphabets[i] == pattern[j]:
                    R = j
            matrix[k][i] = R
    return matrix

def good_suffix(pattern):
    for i in range(len(pattern)):


print(bad_character_table('tbapxab'))