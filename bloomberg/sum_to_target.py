"""
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.

    You can return the answer in any order.

    [-6,2,3,7,6,11,15]
    {
    15:1
    7:
    }
"""


def sum_to_target(nums, target):
    res = []
    store = {}

    for idx, num in enumerate(nums):
        if store.get(num) is not None:
            res.append([store[num], idx])
        else:
            store[target - num] = idx
    print(store)
    return res
    # start, end = 0, len(nums) - 1
    # while start < end:
    #     if nums[start] + nums[end] > target:
    #         end -= 1
    #     elif nums[start] + nums[end] < target:
    #         start += 1
    #     else:
    #         return [start, end]


if __name__ == '__main__':
    print(sum_to_target([-6, 2, 3, 7, 6, 11, 15], 9))
