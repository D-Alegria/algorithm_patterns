"""
    String Anagrams (hard)
    Given a string and a pattern, find all anagrams of the pattern in the given string.

    Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

    abc
    acb
    bac
    bca
    cab
    cba

    Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

    Example 1:
    Input: String="ppqp", Pattern="pq"
    Output: [1, 2]
    Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

    {
     p: 1
     q: 1
    }

    {
    p: 1
    q: 1
    }

    Example 2:
    Input: String="abbcabc", Pattern="abc"
    Output: [2, 3, 4]
    Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
"""
from typing import List


def string_anagram(s: str, pattern: str) -> List[int]:
    word = {}
    pattern_map = {}
    result = []
    window = 0

    for p in pattern:
        if p not in pattern_map:
            pattern_map[p] = 0
        pattern_map[p] += 1

    for i, val in enumerate(s):
        if val not in word:
            word[val] = 0
        word[val] += 1
        window += 1

        while window == len(pattern):
            window -= 1
            if word == pattern_map:
                result.append(i - window)
            word[s[i - window]] -= 1
            if word[s[i - window]] == 0:
                word.pop(s[i - window])

    return result


def string_anagram1(s: str, pattern: str) -> List[int]:
    # store the word in map
    # store the pattern in map
    word = {}
    pattern_map = {}
    result = []
    window = 0

    for p in pattern:
        if p not in pattern_map:
            pattern_map[p] = 0
        pattern_map[p] += 1

    for i, val in enumerate(s):
        if val not in word:
            word[val] = 0
        window += 1

        if val in pattern_map:
            word[val] += 1

            while word[val] > pattern_map[val]:
                window -= 1
                word[s[i - window]] -= 1
            if window == len(pattern):
                result.append(i - window + 1)
        else:
            word = {}
            window = 0

    return result


if __name__ == '__main__':
    print(string_anagram("ppqp", "pq"))
    print(string_anagram("abbcabc", "abc"))
    print(string_anagram("cbaebabacd", "abc"))  # [0,6]
