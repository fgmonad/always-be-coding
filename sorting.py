import random

random_items = [random.randint(-50, 100) for c in range(32)]


def buble_sort(items):
    """Implementation of a buble sort """
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j] # swap with right


def insertion_sort(items):
    """Implementation of insertion sort """
    for i in range(1,len(items)):
        j = 1
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j] # swap with left
            j -= 1


print 'Before: ', random_items
buble_sort(random_items)
print 'After : ', random_items
# print range(len(random_items))


for i in range(1,10):
    # print("---------")
    # print(i)
    # print("---------")
    j = i
    while j > 0:
        j -= 1
        # print(j)
        # print("===")

def merge_sort(items):
    """Implementation of mergesort """
    if len(items) > 1:

        mid   = len(items) / 2 # Determine the midpoint and split
        left  = items[0:mid]
        right = items[mid:]

        merge_sort(left)
        merge_sort(right)

        l, r = 0, 0
        for i in range(len(items)):

            lval = left[l] if l < len(left) else None
            rval = right[r] if r < len(right) else None

            if (lval and rval and lval < rval) or rval is None:
                items[i] = lval
                l += 1
            elif (lval and rval and lval > rval) or lval is None:
                items[i] = rval
                r += 1
            else:
                raise Exception('Could not merge, sub array sizes do not match the main array')

def quick_sort(items):
    """Implementation of quick sort"""
    if len(items) > 1:
        pivot_index = len(items) / 2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(items):
            if i != pivot_index:
                if val < items[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        quick_sort(smaller_items)
        quick_sort(larger_items)
        items[:] = smaller_items + [items[pivot_index]] + larger_items



