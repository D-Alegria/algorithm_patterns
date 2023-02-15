"""
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
    the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.

    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
    In this case, the max area of water (blue section) the container can contain is 49.

    maxHeight
    maxDistance


"""
from typing import List


def maxArea(height: List[int]) -> int:
    start, end = 0, len(height) - 1
    largestArea = 0

    while start < end:
        minH = min(height[start], height[end])
        largestArea = max(largestArea, minH * (end - start))
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
    return largestArea


if __name__ == '__main__':
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(maxArea([1, 1]))
