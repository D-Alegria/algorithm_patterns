"""
    Given a string, find all of its permutations preserving the character sequence but changing case.

    Example 1:

    Input: "ad52"
    Output: "ad52", "Ad52", "aD52", "AD52"
    Example 2:

    ad52
    ad52 Ad52
    ad52 aD52 Ad52 AD52

    Input: "ab7c"
    Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"

    ab7c

    Ab7c aB7c ab7C
    AB7c Ab7C AB7c aB7C Ab7C aB7C
    AB7C
"""

from collections import deque


def find_letter_case_string_permutations(s: str):
    permutations = deque()
    permutations.append(s)
    # iterate through the string
    for idx, letter in enumerate(s):
        if letter.isalpha():
            n = len(permutations)
            for _ in range(n):
                current = permutations.popleft()
                currentList = list(current)
                currentList[idx] = currentList[idx].capitalize()
                permutations.append(current)
                permutations.append("".join(currentList))

    return list(permutations)


if __name__ == '__main__':
    print(find_letter_case_string_permutations("ad52"))
    print(find_letter_case_string_permutations("ab7c"))
