"""
    Given a set of n positive integers, find all the possible subsets of integers that sum up to a number k.
"""


def get_k_sum_subsets(set_of_integers, target_sum):
    subsets = [[]]
    result = []

    for integer in set_of_integers:
        lenOfSubset = len(subsets)
        for i in range(lenOfSubset):
            subsetCopy = subsets[i][:]
            subsetCopy.append(integer)
            subsets.append(subsetCopy)

            if sum(subsetCopy) == target_sum:
                result.append(subsetCopy)
    return result


def get_k_sum_subsets_recur(set_of_integers, target_sum):
    subsets = []
    backtracking(set_of_integers, target_sum, subsets, [])
    return subsets


def backtracking(set_of_integers, target_sum, subsets, subset):
    if target_sum == 0:
        subsets.append(list(subset))

    if target_sum < 0:
        return

    for i in range(len(set_of_integers)):
        subset.append(set_of_integers[i])
        new_set_of_integers = set_of_integers[i + 1:]
        backtracking(new_set_of_integers, target_sum - set_of_integers[i], subsets, subset)
        subset.pop()


if __name__ == '__main__':
    print(get_k_sum_subsets([8, 13, 3, 22, 17, 39, 87, 45, 36], 3))
    print(get_k_sum_subsets([8, 13, 3, 22, 17, 39, 87, 45, 36], 47))
    print(get_k_sum_subsets([8, 13, 3, 22, 17, 39, 87, 45, 36], 135))
    print(get_k_sum_subsets([8, 13, 3, 22, 17, 39, 87, 45, 36], 100))
    print(get_k_sum_subsets([8, 13, 3, 22, 17, 39, 87, 45, 36], 270))
    print(get_k_sum_subsets([8, 13, 3, 22, 17, 39, 87, 45, 36], 1))
    print("Recursion")
    print(get_k_sum_subsets_recur([8, 13, 3, 22, 17, 39, 87, 45, 36], 3))
    print(get_k_sum_subsets_recur([8, 13, 3, 22, 17, 39, 87, 45, 36], 47))
    print(get_k_sum_subsets_recur([8, 13, 3, 22, 17, 39, 87, 45, 36], 135))
    print(get_k_sum_subsets_recur([8, 13, 3, 22, 17, 39, 87, 45, 36], 100))
    print(get_k_sum_subsets_recur([8, 13, 3, 22, 17, 39, 87, 45, 36], 270))
    print(get_k_sum_subsets_recur([8, 13, 3, 22, 17, 39, 87, 45, 36], 1))
