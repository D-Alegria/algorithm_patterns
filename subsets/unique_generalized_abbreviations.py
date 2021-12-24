"""
    Given a word, write a function to generate all of its unique generalized abbreviations.

    Generalized abbreviation of a word can be generated by replacing each substring of the word by the count of characters in the substring. Take the example of “ab” which has four substrings: “”, “a”, “b”, and “ab”. After replacing these substrings in the actual word by the count of characters we get all the generalized abbreviations: “ab”, “1b”, “a1”, and “2”.

    Example 1:
    Input: "BAT"
    Output: "BAT", "BA1", "B1T", "B2", "1AT", "1A1", "2T", "3"

    BAT
    q = [["",0,0]]
    q = [["",1,1], ["B",1,0]]
    q = [["",2,2],["1"] ["B",1,0]]
    abword = ["",1,1]



    Example 2:
    Input: "code"
    Output: "code", "cod1", "co1e", "co2", "c1de", "c1d1", "c2e", "c3", "1ode", "1od1", "1o1e", "1o2",
    "2de", "2d1", "3e", "4"


"""

from collections import deque


def generate_generalized_abbreviations(word):
    wordLen = len(word)
    result = []
    queue = deque()
    queue.append((list(), 0, 0))

    while queue:
        abWord = queue.popleft()
        if abWord[1] == wordLen:
            if abWord[2] != 0:
                abWord[0].append(str(abWord[2]))
            result.append(''.join(abWord[0]))
        else:
            queue.append((list(abWord[0]), abWord[1] + 1, abWord[2] + 1))

            if abWord[2] != 0:
                abWord[0].append(str(abWord[2]))

            newWord = list(abWord[0])
            newWord.append(word[abWord[1]])
            queue.append((newWord, abWord[1] + 1, 0))
        print(queue)
    return result


if __name__ == '__main__':
    print(generate_generalized_abbreviations("BAT"))
    print(generate_generalized_abbreviations("code"))
