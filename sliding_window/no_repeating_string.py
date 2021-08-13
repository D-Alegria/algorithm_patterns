"""
    Given a string, find the length of the longest substring which has no repeating characters.

    Example 1:
    Input: String="aabccbb"
    Output: 3
    Explanation: The longest substring without any repeating characters is "abc".

    {}
                    *
    [a, a , b , c , c , b , b]
                        ^
    Example 2:
    Input: String="abbbb"
    Output: 2
    Explanation: The longest substring without any repeating characters is "ab".

    {a}
                    *
    [a , b , b , b , b]
                    ^

    Example 3:
    Input: String="abccde"
    Output: 3
    Explanation: Longest substrings without any repeating characters are "abc" & "cde".

    {a,b}
                *
    [a, b , c , c , d , e]
                        ^
"""


def no_repeating_string(s: str) -> int:
    back, largest = 0, 0
    seen = {}

    for i, val in enumerate(s):
        if val not in seen:
            seen[val] = 0
        seen[val] += 1

        while seen[val] > 1:
            if s[back] in seen:
                seen[s[back]] -= 1
                if seen[s[back]] == 0:
                    seen.pop(s[back])
            back += 1
        largest = max(i - back, largest)

    return largest + 1


if __name__ == '__main__':
    print(no_repeating_string("aabccbb"))  # 3
    print(no_repeating_string("abbbb"))  # 2
    print(no_repeating_string("abccde"))  # 3
