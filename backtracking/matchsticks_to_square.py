def matchstick_to_square(matchsticks):
    n = len(matchsticks)
    if n < 4:
        return False
    total = sum(matchsticks)
    if total < 4 and total % 4 != 0:
        return False
    matchsticks.sort(reverse=True)
    one_side_length = total // 4

    def backtracking(sticks):
        if len(sticks) == 0:
            return True

        if sticks[0] == one_side_length:
            return backtracking(sticks[1:])
        elif sticks[0] < one_side_length:
            for i in range(1, len(sticks)):
                temp = sticks[:]
                temp[0] += temp[i]
                if backtracking(temp[:i] + temp[i + 1:]):
                    return True
            return False
        else:
            return False

    return backtracking(matchsticks)


def matchstick_to_square_optimized(matchsticks):
    n = len(matchsticks)
    if n < 4:
        return False
    total = sum(matchsticks)
    if total % 4 != 0:
        return False

    matchsticks.sort(reverse=True)
    sides = [0] * 4

    def backtracking(index):
        if index == n:
            return True

        for j in range(4):
            if sides[j] + matchsticks[index] <= total // 4:
                sides[j] += matchsticks[index]
                if backtracking(index + 1):
                    return True
                sides[j] -= matchsticks[index]
        return False
    return backtracking(0)


if __name__ == '__main__':
    print(matchstick_to_square([1, 1, 2, 2, 2]))
    print(matchstick_to_square([3, 3, 3, 3, 4]))
    print(matchstick_to_square([1, 1, 1, 2, 1]))
    print(matchstick_to_square([3, 4, 4, 1, 2, 2]))
    print(matchstick_to_square([5, 6, 1, 1, 2, 2]))
    print("*" * 10 , "Optimized")
    print(matchstick_to_square_optimized([1, 1, 2, 2, 2]))
    print(matchstick_to_square_optimized([3, 3, 3, 3, 4]))
    print(matchstick_to_square_optimized([1, 1, 1, 2, 1]))
    print(matchstick_to_square_optimized([3, 4, 4, 1, 2, 2]))
    print(matchstick_to_square_optimized([5, 6, 1, 1, 2, 2]))
