"""
    Write a function allConstruct(target, wordBank) that accepts a target string
    and an array of strings.

    The function should return a 2D array containing all the ways that the target
    can be constructed by concatenating elements of the wordank array. Each element
    of the 2D array should represent one combination that construct the target.

    You may reuse elements of the wordBank as many times as needed.
"""


def allConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if len(target) == 0:
        return [[]]

    tempTarget = list(target)
    allCombinations = []
    for word in wordBank:
        prefix, suffix = tempTarget[:len(word)], tempTarget[len(word):]
        if word != "".join(prefix):
            continue
        combinations = allConstruct("".join(suffix), wordBank, memo)
        for combination in combinations:
            allCombinations.append([word, *combination])

    memo[target] = allCombinations
    return memo[target]


"""
    n = len of word bank
    m = len of target
    
    time: O(n^m*m*m)
    space: o(m*m*m)
    
    After memoization
    time: o(n*m*m*m)
    space: o(m*m*m)
"""

if __name__ == '__main__':
    print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "c", "ef"]))
    print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(allConstruct("", ["cat", "dog", "mouse"]))
    print(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e" * e for e in range(1, 7)]))
