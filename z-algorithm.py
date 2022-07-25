# uses a table to improve performance while searching for the pattern into an array
def z_algorithm():
    return

# create a z-table
def create_z_table(pattern, array):
    z = [None * len(pattern) + len(array) + 1]
    long_string = create_long_string(pattern, array)

    right = 0
    left = 0
    for i in range(len(long_string)):
        if i > right:
            left = right
            left = i
            while right < len(long_string) and right < long_string[right - left] == long_string[right]:
                right = right + 1
            z[i] = right - left
            right = right - 1
        else:
            k = i - left
            if z[k] < (right - i + 1):
                z[i] = z[k]
    return z

# construct long string
# e.g. CAT$TACOCAT
def create_long_string(pattern, array):
    s = [None * len(pattern) + len(array) + 1]
    for i in range(len(pattern)):
        s[i] = pattern[i]
    s[len(pattern)] = '$'
    for i in range(len(array)):
        s[len(pattern) + 1 + i] = array[i]
    return s