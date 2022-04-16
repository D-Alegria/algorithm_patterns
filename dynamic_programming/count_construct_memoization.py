"""
    Write a function countConstruct(target, wordBank) that accepts a target string
    and an array of strings.

    The function should return the number of ways that the target can be constructed
    by concatenating elements of the wordBank array

    You may reuse elements of wordBank as many times as needed.
"""


def countConstruct(target, wordBank, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if len(target) == 0:
        return 1

    target = list(target)
    count = 0
    for word in wordBank:
        prefix, newTarget = target[:len(word)], target[len(word):]
        if word != "".join(prefix):
            continue
        count += countConstruct("".join(newTarget), wordBank, memo)
        target = ''.join(target)
        memo[target] = count

    return count


"""
    n = len of wordbank
    m = len of target 
    
    time: O(n^m*m)
    space: O(m*m)
    
    After memoization
    time: O(n*m*m)
    space: O(m*m)
"""

if __name__ == '__main__':
    print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(countConstruct("", ["cat", "dog", "mouse"]))
    print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e" * e for e in range(1, 7)]))
