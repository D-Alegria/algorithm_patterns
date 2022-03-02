"""
    Given a string s, find the length of the longest substring without repeating characters.

    Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    {
        a:1
        b:1
        c:1
    }
"""


def no_repeating_substring(s):
    store = {}
    s = list(s)
    back = 0
    maxi = 0

    for i, l in enumerate(s):
        if l not in store:
            store[l] = 0
        store[l] += 1

        while store[l] > 1:
            store[s[back]] -= 1
            maxi = max(maxi, i - back)
            back += 1
    return maxi


if __name__ == '__main__':
    print(no_repeating_substring("abcabcbb"))
    print(no_repeating_substring("pwwkew"))
