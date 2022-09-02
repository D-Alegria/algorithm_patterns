def canConstruct(target, wordBank):
    target = list(target)
    n = len(target)
    table = [False for _ in range(n + 1)]
    table[0] = True

    for idx in range(n):
        letter = target[idx]

        for word in wordBank:
            word = list(word)
            lenWord = len(word)
            if lenWord > 0 and letter == word[0] and idx + lenWord < n + 1:
                table[idx + lenWord] = True

    return table[-1]


"""
    n = wordBank length
    m = length of target
    time: O(n*m*m)
    space: O(m*m)
"""

if __name__ == '__main__':
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(canConstruct("", ["cat", "dog", "mouse"]))
    print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e" * e for e in range(1, 7)]))
