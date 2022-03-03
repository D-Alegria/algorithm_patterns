"""
    3Sum

    Solution
    Given an integer array nums, return all the triplets [nums[i], nums[j],
    nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.



    Example 1:

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
"""
from typing import List


def twoSum(nums: List[int], idx: int) -> List[List[int]]:
    start, end = idx + 1, len(nums) - 1
    result = []

    while start < end:
        if nums[start] + nums[end] + nums[idx] < 0:
            start += 1
        elif nums[start] + nums[end] + nums[idx] > 0:
            end -= 1
        else:
            result.append([nums[idx], nums[start], nums[end]])
            start += 1
            end -= 1
            while start < end and nums[end] == nums[end + 1]:
                end -= 1
            while start < end and nums[start] == nums[start - 1]:
                start += 1

    return result


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    result = []

    for idx in range(n):
        if idx == 0 or nums[idx] != nums[idx - 1]:
            result.extend(twoSum(nums, idx))
    return result


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
