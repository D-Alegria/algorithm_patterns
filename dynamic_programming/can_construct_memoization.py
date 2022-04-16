"""
    Write a function 'canConstruct(target, wordBank)' that accepts a target
    string and an array of strings.

    The function should return a boolean indicating whether the 'target' can be
    constructed by concatenating elements of the 'wordBank' array.

    You may reuse elements of 'wordBank' as many times as needed
"""


def canConstructMe(target, wordBank, result=""):
    if target == result:
        return True
    if len(result) > len(target):
        return False

    for word in wordBank:
        if canConstructMe(target, wordBank, result + word):
            return True

    return False


"""
    n = wordBank length
    m = length of target
    time: O(n^m)
    space: O(m)
"""


def canConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "":
        return True
    target = list(target)
    for word in wordBank:
        prefix, newTarget = target[:len(word)], target[len(word):]
        if word != "".join(prefix):
            continue
        if canConstruct("".join(newTarget), wordBank, memo):
            return True

    target = "".join(target)
    memo[target] = False
    return False


"""
    n = wordBank length
    m = length of target
    time: O(n^m*m)
    space: O(m*m)
    
    After memoization
    time: O(n*m*m)
    space: O(m*m)
"""

if __name__ == '__main__':
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(canConstruct("", ["cat", "dog", "mouse"]))
    print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e" * e for e in range(1, 7)]))
