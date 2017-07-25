def cumSum(n):

    #Base case
    if n == 0:
        return 0
    else:
        return n + cumSum(n - 1)


print(cumSum(5))