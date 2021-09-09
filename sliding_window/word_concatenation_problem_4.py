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


def word_concatenation1(s: str, words: List[str]) -> List[int]:
    word_map = {word: 0 for word in words}
    word_count = {}
    word_length = len(words[0])
    window = deque()
    not_part = deque()
    current_word = ""
    total = 0
    result = []

    for word in words:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1

    for i, val in enumerate(s):
        current_word += val
        window.append(val)

        if len(current_word) == word_length:
            if current_word in word_map:
                word_map[current_word] += 1
                total += 1
                back = ""

                while word_map[current_word] > word_count[current_word] or len(not_part) > 0:
                    back += window.popleft()

                    if len(back) == word_length:
                        if back in word_map:
                            word_map[back] -= 1
                            total -= 1
                        else:
                            not_part.popleft()
                        back = ""

                if total == len(words):
                    result.append(i - len(window) + 1)
                current_word = ""
            else:
                not_part.append(current_word)
                current_word = ""

    return result


if __name__ == '__main__':
    print(word_concatenation("catfoxcat", ["cat", "fox"]))
    print(word_concatenation("catcatfoxfox", ["cat", "fox"]))
    print(word_concatenation("barfoothefoobarman", ["foo", "bar"]))
    print(word_concatenation("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
