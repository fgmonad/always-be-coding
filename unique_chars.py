import collections

def uni_char(s):
    l = len(s)
    dict = collections.defaultdict(int)

    if l <= 1: return True

    for char in s:
        dict[char] += 1
        if dict[char] > 1: return False

    return True
