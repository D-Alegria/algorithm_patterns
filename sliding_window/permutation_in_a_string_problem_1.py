"""
    Permutation in a String (hard) #
    Given a string and a pattern, find out if the string contains any permutation of the pattern.

    Permutation is defined as the re-arranging of the characters of the string. For example, “abc”
    has the following six permutations:

    abc
    acb
    bac
    bca
    cab
    cba
    If a string has ‘n’ distinct characters it will have n!n! permutations.


    Example 1:
    Input: String="oidbcaf", Pattern="abc"
    Output: true
    Explanation: The string contains "bca" which is a permutation of the given pattern.



    Example 2:
    Input: String="odicf", Pattern="dc"
    Output: false
    Explanation: No permutation of the pattern is present in the given string as a substring.

    Example 3:
    Input: String="bcdxabcdy", Pattern="bcdyabcdx"
    Output: true
    Explanation: Both the string and the pattern are a permutation of each other.

    Example 4:
    Input: String="aaacb", Pattern="abc"
    Output: true
    Explanation: The string contains "acb" which is a permutation of the given pattern.


    Algorithm

"""


def permutation1(s: str, pattern: str) -> bool:
    word = {}
    pattern_map = {}
    window = 0

    for val in pattern:
        if val not in pattern_map:
            pattern_map[val] = 0
        pattern_map[val] += 1

    for i, val in enumerate(s):
        if val not in word:
            word[val] = 0
        word[val] += 1
        window += 1
        while window == len(pattern):
            if pattern_map == word:
                return True
            window -= 1
            word[s[i - window]] -= 1
            if word[s[i - window]] == 0:
                word.pop(s[i - window])

    return False


def permutation(s: str, pattern: str) -> bool:
    word = {}
    pattern_map = {}
    window = 0

    for val in pattern:
        if val not in pattern_map:
            pattern_map[val] = 0
        pattern_map[val] += 1

    for i, val in enumerate(s):
        if val not in word:
            word[val] = 0
        if val in pattern_map:
            window += 1
            word[val] += 1

            while word[val] > pattern_map[val]:
                word[val] -= 1
                window -= 1

            if window == len(pattern):
                return True
        else:
            window = 0

    return False


if __name__ == '__main__':
    print(permutation("oidbcaf", "abc"))  # true
    print(permutation("odicf", "dc"))  # false
    print(permutation("bcdxabcdy", "bcdyabcdx"))  # true
    print(permutation("aaacb", "abc"))  # true

    """
    
    a   a   a   c   b
                    ^  
    """
