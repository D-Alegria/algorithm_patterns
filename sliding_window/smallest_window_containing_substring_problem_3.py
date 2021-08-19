"""
    Smallest Window containing Substring (hard) #
    Given a string and a pattern, find the smallest substring in the given string which has
    all the characters of the given pattern.

    Example 1:
    Input: String="aabdec", Pattern="abc"
    Output: "abdec"
    Explanation: The smallest substring having all characters of the pattern is "abdec"
    *
    a   b   c

    baac
    baabc

        |               |
    a   a   b   d   e   c
                        ^
    a   a   b   a   b   d   e   c
                                ^
    Example 2:
    Input: String="abdabca", Pattern="abc"
    Output: "abc"
    Explanation: The smallest substring having all characters of the pattern is "abc".

    Example 3:
    Input: String="adcad", Pattern="abc"
    Output: ""
    Explanation: No substring in the given string has all characters of the pattern.
"""


def shortest_substring(s: str, pattern: str) -> str:
    pattern_map = {}
    word = {}
    window = 0
    found = 0
    short = [0, 100000]

    for i in pattern:
        if i not in pattern_map:
            pattern_map[i] = 0
        pattern_map[i] += 1

    for i, val in enumerate(s):
        if val not in word:
            word[val] = 0
        word[val] += 1
        window += 1

        if val in pattern_map:
            found += 1
            # checks if letter in word is grater or the character isn't part of the pattern
            # because for it to be the shortest it has to start and end with a character
            # in the map
            while word[val] > pattern_map[val] or (i > 1 and s[i - (window - 1)] not in pattern_map):
                window -= 1
                word[s[i - window]] -= 1

                if s[i - window] in pattern_map:
                    found -= 1

            if found == len(pattern) and short[1] - short[0] > window:
                short[1], short[0] = i + 1, i - (window - 1)
    return "".join(s[short[0]:short[1]]) if short[1] - short[0] != 100000 else ""


if __name__ == '__main__':
    print(shortest_substring("aabdec", "abc"))
    print(shortest_substring("abdabca", "abc"))
    print(shortest_substring("baac", "abc"))
    print(shortest_substring("baabc", "abc"))
    print(shortest_substring("adcad", "abc"))
