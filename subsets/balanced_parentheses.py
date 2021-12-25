"""
    For a given number ‘N’,
    write a function to generate all combination of ‘N’ pairs of balanced parentheses.

    Example 1:
    Input: N=2
    Output: (()), ()()

    (
    (( ()

    Example 2:
    Input: N=3
    Output: ((())), (()()), (())(), ()(()), ()()()
"""

from collections import deque


def generate_valid_parentheses1(num):
    result = []
    permutations = deque()
    permutations.append(["", 0, 0])

    while permutations:
        current = permutations.popleft()
        if current[1] == num and current[2] == num:
            result.append(current[0])
        else:
            if current[1] < num:
                permutations.append([current[0] + "(", current[1] + 1, current[2]])
            if current[1] > current[2]:
                permutations.append([current[0] + ")", current[1], current[2] + 1])

    return result


def generate_valid_parentheses(num):
    result = []

    def generate(nm, current, open, close):
        if open == nm and close == nm:
            result.append(current)
        else:
            if open < nm:
                generate(nm, current + "(", open + 1, close)
            if open > close:
                generate(nm, current + ")", open, close + 1)

    generate(num, "", 0, 0)
    return result


if __name__ == '__main__':
    print(generate_valid_parentheses(2))
    print(generate_valid_parentheses(3))
