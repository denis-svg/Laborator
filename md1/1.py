from copy import deepcopy


def helper(array, subset, i, out):
    if i == len(array):
        out.append(deepcopy(subset))
    else:
        helper(array, deepcopy(subset), i + 1, out)
        subset.append(array[i])
        helper(array, deepcopy(subset), i + 1, out)


def all_subsets(array):
    out = []
    helper(array, [], 0, out)
    return out


initial_set = [1, 2, 3, [5, 6]]
print(all_subsets(initial_set))

