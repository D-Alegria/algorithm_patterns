"""
    You are in charge of preparing a recently purchased lot for one of Amazon's new building.
    The lot is covered with trenches and has a single obstacle that needs to be taken down before the foundation can be
    prepared for the building. The demolition robot must remove the obstacle before progress can be made on the
    building.

    Write an algorithm to determine the minimum distance required for the demolition robot to remove the obstacle.

    Assumption:
    The lot is flat, except for trenches, and can be represented as a two-dimensional grid.
    The demolition robot must start from the top-left corner of the lot, which is always flat, and can move one block
    up, down, left or right at a time.
    The demolition robot cannot enter trenches and cannot leave the lot.
    The flat areas are represented as 1, areas with trenches are represented by 0 and the obstacle is represented by 9.

    Input:
    The input to the function/method consists of one argument: lot, representing the two dimensional grid of integers.

    Output:
    Return an integers representing the minimum distance traversed to remove the obstacle else return -1.

    Constraints
    1 <= rows, columns <= 10^3

    Example:
    Input:
    [[1,0,0],
    [1,0,0],
    [1,9,1]]

                                                    0,0
                            1,0                                             0,1
            2,0                             1,1             1,1                             0,2
                    2,1             2,1          1,2     2,1         1,1                1,2

    queue -> (r,c)

    Output:
    3

    Explanation:
    Starting from the top-left corner, the demolition robot traversed the cells (0,0) -> (1,0) -> (2,0) -> (2,1).
    The robot traversed the total distance 3 to remove the obstacles.

    So, the output is 3.
"""
from collections import deque


def minimum_distance(lot: [[int]]) -> int:
    queue = deque()
    row, column, count = 0, 0, 0
    if len(lot) > 0:
        queue.append((row, column))

    while queue:
        lenLot = len(queue)

        for i in range(lenLot):
            r, c = queue.popleft()

            if lot[r][c] == 9:
                return count

            if c < len(lot[r]) - 1 and lot[r][c + 1] > 0:
                queue.append((r, c + 1))
            if r < len(lot) - 1 and lot[r + 1][c] > 0:
                queue.append((r + 1, c))
        count += 1
    return -1


if __name__ == '__main__':
    print(minimum_distance([[1, 0, 0], [1, 0, 0], [1, 9, 1]]))
    print(minimum_distance([]))
