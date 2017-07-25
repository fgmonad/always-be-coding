# Increase space complexity in exchange of time complexity
def factorial(n):
    lookup_table = {}
    if n < 2:
        return 1
    if n in lookup_table:
        return lookup_table[n]
    else:
        x = factorial(n - 1) * n
        lookup_table[n] = x
        return x


print(factorial(5))


factorial_memo = {}
def factorial2(k):
    if k < 2:
        return 1

    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k -1)

    return factorial_memo[k]

print(factorial2(5))
