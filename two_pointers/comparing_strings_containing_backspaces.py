"""
    Comparing Strings containing Backspaces (medium)
    Given two strings containing backspaces (identified by the character ‘#’),
    check if the two strings are equal.

    Example 1:
    Input: str1="xy#z", str2="xzz#"
    Output: true
    Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
                *
    x   y   #   z
        *
    x   z   z   #

    Example 2:
    Input: str1="xy#z", str2="xyz#"
    Output: false
    Explanation: After applying backspaces the strings become "xz" and "xy" respectively.

    Example 3:
    Input: str1="xp#", str2="xyz##"
    Output: true
    Explanation: After applying backspaces the strings become "x" and "x" respectively.
    In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
    *
    x   p   #
    *
    x   y   #   z   #   #

    Example 4:
    Input: str1="xywrrmp", str2="xywrrmu#p"
    Output: true
    Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
                *
    x   y   w   r   r   m   p
                *
    x   y   w   r   r   m   u   #   p
"""


def compare_strings1(str1: str, str2: str) -> bool:  # time = O(N + M) space O(N + M)
    string1 = []
    string2 = []

    for i in str1:  # N
        if i == "#":
            string1.pop()
        else:
            string1.append(i)

    for i in str2:  # M
        if i == "#":
            string2.pop()
        else:
            string2.append(i)

    for s1, s2 in zip(string1, string2):  # N+ M
        if s1 != s2:
            return False
    return True


def compare_strings(str1: str, str2: str) -> bool:  # time = O(N + M) space O(1)
    front_1 = len(str1) - 1
    front_2 = len(str2) - 1

    while front_1 >= 0 or front_2 >= 0:
        count = 0
        while str1[front_1] == "#":
            count += 1
            front_1 -= 1
        front_1 -= count

        count = 0
        while str2[front_2] == "#":
            count += 1
            front_2 -= 1
        front_2 -= count

        if str1[front_1] != str2[front_2]:
            return False
        front_1 -= 1
        front_2 -= 1

    return True


if __name__ == '__main__':
    print(compare_strings(str1="xy#z", str2="xzz#"))  # true
    print(compare_strings(str1="xy#z", str2="xyz#"))  # false
    print(compare_strings(str1="xp#", str2="xyz##"))  # true
    print(compare_strings(str1="xywrrmp", str2="xywrrmu#p"))  # true
