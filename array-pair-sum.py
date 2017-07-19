
def pair_sum(arr, k):

    if len(arr) < 2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    # For every number in array
    for num in arr:
        # Set target difference
        target = k - num

        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
            print("----")
            print(seen)
            print("----")

        else:
            # add a tuple with the corresponding pair
            output.add( (min(num,target), max(num,target)) )

    # return len(output)
    return '\n'.join(map(str,list(output)))

print(pair_sum([1,3,2,2],4))