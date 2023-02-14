def jump_game_two(nums):
    noOfJumps = 0
    longestJump = 0
    currentJump = 0
    n = len(nums)

    for i in range(n):
        longestJump = max(longestJump, nums[i] + i)
        if i == currentJump or i + 1 == n:
            currentJump = longestJump
            noOfJumps += 1
    return noOfJumps - 1


if __name__ == '__main__':
    print(jump_game_two([2, 3, 1, 1, 9]))
    print(jump_game_two([3, 2, 1, 1, 4]))
    print(jump_game_two([4, 0, 0, 0, 4]))
    print(jump_game_two([1, 1]))
    print(jump_game_two([1]))
