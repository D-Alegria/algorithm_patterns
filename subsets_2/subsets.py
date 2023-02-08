"""
    Statement
    Given a set of integers, find all possible subsets within the set.

    Note: The solution set must not contain duplicate subsets. Return the solution in any order.

    Constraints:
    1 ≤ set.length ≤ 10
    −10 ≤ set[i] ≤ 10
    All the numbers of the set are unique.
"""


def find_all_subsets(v):
    # Write your code here
    result = [[]]
    for i in v:  # N
        subSet = []
        for j in result:  # 2^N
            copyL = j.copy()
            copyL.append(i)
            subSet.append(copyL)
        result.extend(subSet)
    return result


def find_all_subsets_recur(v):
    result = []
    backtracking(v, result, [])
    return result


def backtracking(v, result, subset):
    result.append(list(subset))
    if len(v) == 0:
        return

    for i in range(len(v)):
        subset.append(v[i])
        backtracking(v[i + 1:], result, subset)
        subset.pop()


if __name__ == '__main__':
    print(find_all_subsets([1]))
    print(find_all_subsets([1, 2]))
    print(find_all_subsets([2, 5, 7]))
    print(find_all_subsets([1, 2, 3, 4]))
    print(find_all_subsets([0]))
    print(find_all_subsets([7, 3, 1, 5]))
    print(find_all_subsets([-1, -10, -3, 1, 2, 4]))
    print("Recursive Method")
    print(find_all_subsets_recur([1]))
    print(find_all_subsets_recur([1, 2]))
    print(find_all_subsets_recur([2, 5, 7]))
    print(find_all_subsets_recur([1, 2, 3, 4]))
    print(find_all_subsets_recur([0]))
    print(find_all_subsets_recur([7, 3, 1, 5]))
    print(find_all_subsets_recur([-1, -10, -3, 1, 2, 4]))
