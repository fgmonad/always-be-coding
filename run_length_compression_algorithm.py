def compress2(s):
    # run length compression algorithm
    r = ""
    l = len(s)

    if l == 0: return ''
    if l == 1: return s + '1'

    last = s[0]
    cnt = 1
    i = 1

    while i < l:
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            r = r + s[i - 1] + str(cnt)

        i += 1

    r = r + s[i - 1] + str(cnt)

    return r