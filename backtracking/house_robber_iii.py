def rob(houses):
    n = len(houses)

    def backtracking(node):
        if node > n:
            return [0, 0]  # child, grandchild

        right = backtracking(node * 2 + 1)
        left = backtracking(node * 2)

        # maxChild = max(right[0] + left[0], right[0] + left[1], right[1] + left[0])
        maxChild = max(right) + max(left) # with this you can rob two adjacent houses
        maxGrandChild = right[1] + left[1] + houses[node - 1]

        return [maxGrandChild, maxChild]

    return max(backtracking(1))


if __name__ == '__main__':
    print(rob([9, 7, 11, 1, 8, 10, 12]))
    print(rob([5, 3, 8, 2, 4, 6, 10, 1]))
    print(rob([3]))
    print(rob([8, 7, 10]))
    print(rob([15, 10, 25, 5, 12, 20, 30, 3, 7, 11, 13]))
