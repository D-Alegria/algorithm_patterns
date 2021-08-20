"""
    Words Concatenation (hard) #
    Given a string and a list of words, find all the starting indices of substrings in the given string
    that are a concatenation of all the given words **exactly once** **without any overlapping** of words.
    ** It is given that all words are of the same length.

    Example 1:
    Input: String="catfoxcat", Words=["cat", "fox"]
    Output: [0, 3]
    Explanation: The two substring containing both the words are "catfox" & "foxcat".

    {
    cat: 0,
    fox: 0,
    }
                *
    c   a   t   f   o   x   c   a   t
                        ^
    Example 2:
    Input: String="catcatfoxfox", Words=["cat", "fox"]
    Output: [3]
    Explanation: The only substring containing both the words is "catfox".

    Algorithm:
    - move through the list and append the
"""
from typing import List
from collections import deque


def word_concatenation(s: str, words: List[str]) -> List[int]:
    word_map = {word: 0 for word in words}
    word_length = len(words[0])
    window = deque()
    current_word = ""
    total = 0
    result = []

    for i, val in enumerate(s):
        current_word += val
        window.append(val)

        if len(current_word) == word_length:
            word_map[current_word] += 1
            total += 1
            back = ""

            while word_map[current_word] > 1:
                back += window.popleft()

                if len(back) == word_length:
                    word_map[back] -= 1
                    total -= 1
                    back = ""

            if total == len(words):
                result.append(i - len(window) + 1)
            current_word = ""
    return result


if __name__ == '__main__':
    print(word_concatenation("catfoxcat", ["cat", "fox"]))
    print(word_concatenation("catcatfoxfox", ["cat", "fox"]))
