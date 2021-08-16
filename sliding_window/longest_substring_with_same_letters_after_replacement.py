"""
    Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter,
    find the length of the longest substring having the same letters after replacement.

    Example 1:
    Input: String="aabccbb", k=2
    Output: 5
    Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

    {
    a: 2
    b: 1
    c: 2
    }

    maxRep = 0
            *       !
    [a  ,   a   ,   b   ,   c   ,   c    ,   b   ,   b]
    ^
    Example 2:
    Input: String="abbcb", k=1
    Output: 4
    Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

    Example 3:
    Input: String="abccde", k=1
    Output: 3
    Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

    *       !
    [a  ,   b   ,   c   ,   c   ,   d   ,   e]
    ^
"""


def substring_after_replacement(s: str, k: int) -> int:
    letters = {}
    back, longest, window = 0, 0, 0
    mostFreq = s[0]

    for i, val in enumerate(s):
        if val not in letters:
            letters[val] = 0
        letters[val] += 1
        window += 1

        if letters[mostFreq] <= letters[val]:
            mostFreq = val

        while window > letters[mostFreq] + k:
            letters[s[back]] -= 1
            window -= 1
            back += 1

        longest = max(window, longest)

    return longest


if __name__ == '__main__':
    print(substring_after_replacement("aabccbb", 2))  # 5
    print(substring_after_replacement("abbcb", 1))  # 4
    print(substring_after_replacement("abccde", 1))  # 3
