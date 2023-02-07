"""
    Given a set of distinct numbers, find all of its permutations.

    Permutation is defined as the re-arranging of the elements of the set.
    For example, {1, 2, 3} has the following six permutations:

    {1, 2, 3}
    {1, 3, 2}
    {2, 1, 3}
    {2, 3, 1}
    {3, 1, 2}
    {3, 2, 1}
    If a set has ‘n’ distinct elements it will have n!n! permutations.

    Example 1:
    Input: [1,3,5]
    Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]

    0[]
    1[1]
    3[1,3][3,1]
    5[5,1,3][1,5,3][1,3,5][3,1,5][3,5,1][5,3,1]

    1,3
    [[3,1],[1,3]]
    1 []
    3 [1] 1

    !
    a b c

    queue = [[b,]]


"""

from collections import deque


def permute_word(word):
    result = []
    n = len(word)
    if n == 0:
        return result
    word = list(word)
    queue = deque()
    queue.append([])

    for letter in word:
        currentLengthOfQueue = len(queue)
        for _ in range(currentLengthOfQueue):
            current = queue.popleft()
            cLen = len(current)
            for j in range(cLen + 1):
                permutation = current[:]
                permutation = permutation[:j] + [letter] + permutation[j:]
                if len(permutation) == n:
                    result.append(permutation)
                else:
                    queue.append(permutation)

    return result


if __name__ == '__main__':
    print(permute_word("abcd"))
    print(permute_word("bad"))
    print(permute_word("ab"))
    print(permute_word("xyz"))
    print(permute_word("a"))
