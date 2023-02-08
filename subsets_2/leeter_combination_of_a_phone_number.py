"""
    Given a string having digits from 2 to 9
    inclusive, return all the possible letter combinations that can be made from the numbers in the string.
    Return the answer in any order.
"""
from collections import deque


def letter_combinations(digits):
    # Write your code here
    result = []
    store = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }

    subset = deque()
    subset.append("")

    for i in digits:  # N
        number = int(i)
        letters = store.get(number, "")
        n = len(subset)
        for _ in range(n):  # N * L
            s = subset.popleft()
            for char in letters:  # L
                if len(s) + 1 == len(digits):
                    result.append(s + char)
                else:
                    subset.append(s + char)

    return result



if __name__ == '__main__':
    print(letter_combinations("2"))
    print(letter_combinations("73"))
    print(letter_combinations("426"))
    print(letter_combinations("78"))
    print(letter_combinations("925"))
    print(letter_combinations("39"))
    print(letter_combinations("25"))
