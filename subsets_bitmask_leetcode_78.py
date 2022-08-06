def subset_for_bitmask(bitmask, values):
    subset = []
    index = len(values) - 1

    while index >= 0:
        if bitmask & 1:
            subset.append(values[index])
        bitmask = bitmask >> 1
        index -= 1

    return subset

def subsets(sets):
    bits_needed = len(sets)
    bitmask_max = 2 ** bits_needed

    subsets = []

    for bitmask in range(bitmask_max):
        subsets.append(subset_for_bitmask(bitmask, sets))

    return subsets

print(subsets([1,2,3]))
