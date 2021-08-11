"""
    Given a string, find the length of the longest substring in it with no more than K distinct characters.
    can be interpreted as

    find the length of longest substring with no more than k different characters

    Example 1:
    Input: String="araaci", K=2
    Output: 4
    Explanation: The longest substring with no more than '2' distinct characters is "araa".

    Example 2:
    Input: String="araaci", K=1
    Output: 2
    Explanation: The longest substring with no more than '1' distinct characters is "aa".

    {c}
    K=1
                    *
    [a , r , a , a , c , i]
                        ^

    Example 3
    Input: String="cbbebi", K=3
    Output: 5
    Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

    {c,b,e}
    k = 3
    *
    [c , b , b , e , b, i] l=4
                        ^
"""


def longestSubstringWithKDistinctCharacters(s: str, k: int) -> int:
    back = 0
    largest = 0
    seen = set()

    for i, val in enumerate(s):
        if len(seen) < k or val in seen:
            seen.add(val)
        else:
            if val not in seen:
                seen.remove(s[back])
                seen.add(val)
                while s[back] not in seen:
                    back += 1
        largest = max(largest, i - back)

    return largest + 1


if __name__ == '__main__':
    print(longestSubstringWithKDistinctCharacters("araaci", 2))
    print(longestSubstringWithKDistinctCharacters("araaci", 1))
    print(longestSubstringWithKDistinctCharacters("cbbebi", 3))
    print(longestSubstringWithKDistinctCharacters("aaaaaaaaabaaaaaaaavaaaaaaaaaaaaaaataaaaa", 2))
