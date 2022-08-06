def subset_for_bitmask(bitmask, values):
    # in binary form, the bitmask looks like this: e.g., 6 -> 110
    # we can use this to tell us to include the values at index 0 and 1, but not 2
    # 110 (include first, include second, don't include third)

    subset = []
    index = len(values) - 1

    while index >= 0:
        if bitmask & 1:
            subset.append(values[index])
        bitmask = bitmask >> 1
        index -= 1

    return sorted(subset)

def subsets(sets):
    bits_needed = len(sets)
    bitmask_max = 2 ** bits_needed

    subsets = []

    for bitmask in range(bitmask_max):
        print("Nums:     {}".format(sets))
        print("Bitmask: %s" % (visualize_bitmask(bitmask, sets)))
        print("Subset:   %s\n" % (subset_for_bitmask(bitmask, sets)))
        subsets.append(subset_for_bitmask(bitmask, sets))

    return subsets

def visualize_bitmask(bitmask, values):
    import copy;
    original_bitmask = copy.deepcopy(bitmask)
    visualized_bitmask = ""

    index = len(values) - 1

    while index >= 0:
        if bitmask & 1:
            visualized_bitmask += " 1 "
        else:
            visualized_bitmask += " 0 "

        bitmask = bitmask >> 1
        index -= 1

    return " " + visualized_bitmask[::-1] + " == as a (decimal) number {}".format(original_bitmask)

print(subsets([1,2,3]))
