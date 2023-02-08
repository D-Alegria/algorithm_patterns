"""

"""


def generate_combinations(n):
    result = []
    backtracking(n, 0, 0, result, "")
    return result


def backtracking(n, openCount, closeCount, result, currentGeneration):
    if openCount == closeCount == n:
        result.append(currentGeneration)
        return

    if openCount < n:
        backtracking(n, openCount + 1, closeCount, result, currentGeneration + "(")
    if openCount > closeCount:
        backtracking(n, openCount, closeCount + 1, result, currentGeneration + ")")


if __name__ == '__main__':
    print(generate_combinations(1))
    print(generate_combinations(2))
    print(generate_combinations(3))
    print(generate_combinations(4))
    print(generate_combinations(5))
