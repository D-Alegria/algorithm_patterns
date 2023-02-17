"""
    Given an integer array nums and an integer k, split nums into k non-empty
    subarrays such that the largest sum of any subarray is minimized.

    Return the minimized the largest sum of the split.

    A subarray is a contiguous part of the array.


    nums = [7,2,5,10,8], k = 1

    nums = [7,2,5,10,8], k = 2

    nums = [7,2,5,10,8], k = 3



    [7,2,5,10,8]



def process():
            total = sum(nums)

            if k == 1:
                return total

        print(nums, k)

        n = len(nums)
        maxGroup = 0
        minDiff = math.inf
        left = []
        right = []

        for i in range(1, n):
            left, right = nums[:i], nums[i:]
            sumOfLeft = sum(left)
            sumOfRight = sum(right)
            if abs(sumOfLeft - sumOfRight) < minDiff:
                maxGroup = max(sumOfLeft, sumOfRight)
                minDiff = min(abs(sumOfLeft - sumOfRight), minDiff)
        if (len(left) >= k):
            self.splitArray(left, k - 1)
        if (len(right) >= k):
            self.splitArray(right, k - 1)
        return maxGroup




"""

