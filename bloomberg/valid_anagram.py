"""
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true
    Example 2:

    Input: s = "rat", t = "car"
    Output: false
"""
from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    sStore = Counter(s)
    tStore = Counter(t)

    return sStore == tStore


if __name__ == '__main__':
    print(isAnagram("anagram", "nagaram"))
    print(isAnagram("rat", "car"))
