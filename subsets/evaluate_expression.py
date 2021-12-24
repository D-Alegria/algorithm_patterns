"""
    Evaluate Expression (hard) #
    Given an expression containing digits and operations (+, -, *),
    find all possible ways in which the expression can be evaluated by grouping the numbers and operators using parentheses.

    Example 1:
    Input: "1+2*3"
    Output: 7, 9
    Explanation: 1+(2*3) => 7 and (1+2)*3 => 9

    Example 2:
    Input: "2*3-4-5"
    Output: 8, -12, 7, -7, -3
    Explanation: 2*(3-(4-5)) => 8, 2*(3-4-5) => -12, 2*3-(4-5) => 7, 2*(3-4)-5 => -7, (2*3)-4-5 => -3

    []
    (1+(2*3))
"""


def diff_ways_to_evaluate_expression(inp):
    result = []
    if '+' not in inp and '-' not in inp and '*' not in inp:
        result.append(int(inp))
    else:
        for i in range(0, len(inp)):
            char = inp[i]
            if not char.isdigit():
                leftParts = diff_ways_to_evaluate_expression(inp[0:i])
                rightParts = diff_ways_to_evaluate_expression(inp[i + 1:])

                for part1 in leftParts:
                    for part2 in rightParts:
                        if char == '+':
                            result.append(part1 + part2)
                        elif char == '-':
                            result.append(part1 - part2)
                        elif char == '*':
                            result.append(part1 * part2)
    return result


if __name__ == '__main__':
    print(str(diff_ways_to_evaluate_expression("1+2*3")))
    print(str(diff_ways_to_evaluate_expression("2*3-4-5")))
