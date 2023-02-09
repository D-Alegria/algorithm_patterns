"""
    In a single-player jump game, the player starts at one end of a series of squares, with the goal of reaching the
    last square. At each turn, the player can take up to steps towards the last square, where is the value of the
    current square.

    For example, if the value of the current square is 3, the player can take either 3 steps, or 2 steps, or 1
    step in the direction of the last square. The player cannot move in the opposite direction, that is, away from the
    last square.

    You have been tasked with writing a function to validate whether a player can win a given game or not.

    You’ve been provided with the nums integer array, representing the series of squares.
    The player starts at the first index and, following the rules of the game, tries to reach the last index.

    If the player can reach the last index, your function returns TRUE; otherwise, it returns FALSE.


                    !
    2   3   1   1   4
                ^
"""


def jump_game(nums):
    target = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if target - nums[i] <= i:
            target = i
    if target == 0:
        return True
    return False


if __name__ == '__main__':
    print(jump_game([2, 3, 1, 1, 9]))
    print(jump_game([3, 2, 1, 0, 4]))
    print(jump_game([4, 0, 0, 0, 4]))
    print(jump_game([0]))
    print(jump_game([1]))

    numbers = [
        [3, 2, 2, 0, 1, 4],
        [2, 3, 1, 1, 9],
        [3, 2, 1, 0, 4],
        [0],
        [1],
        [4, 3, 2, 1, 0],
        [1, 1, 1, 1, 1],
        [4, 0, 0, 0, 1],
        [3, 3, 3, 3, 3],
        [1, 2, 3, 4, 5, 6, 7]
    ]

    for j in range(len(numbers)):
        print(j + 1, ".\tInput array: ", numbers[j], sep="")
        print("\tCan we reach the very last index? ",
              "Yes" if jump_game(numbers[j]) else "No", sep="")
        print("-" * 100)
