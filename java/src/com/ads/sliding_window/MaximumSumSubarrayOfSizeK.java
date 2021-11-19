package com.ads.sliding_window;

/**
 * Created by Demilade Oladugba on 11/19/2021
 * <p>
 * Problem Statement
 * Given an array of positive numbers and a positive number ‘k’,
 * find the maximum sum of any contiguous subarray of size ‘k’.
 * <p>
 * Example 1:
 * <p>
 * Input: [2, 1, 5, 1, 3, 2], k=3
 * Output: 9
 * Explanation: Subarray with maximum sum is [5, 1, 3].
 * Example 2:
 * <p>
 * Input: [2, 3, 4, 1, 5], k=2
 * Output: 7
 * Explanation: Subarray with maximum sum is [3, 4].
 **/

/*
                        !
    2   1   5   1   3   2

    s = 5
    m = 9
*/

public class MaximumSumSubarrayOfSizeK {
    public static void main(String[] args) {
        System.out.println("Max sum is " + findMaxSumSubArray(3, new int[]{2, 1, 5, 1, 3, 2}));
        System.out.println("Max sum is " + findMaxSumSubArray(2, new int[]{2, 3, 4, 1, 5}));
    }

    public static int findMaxSumSubArray(int k, int[] arr) {
        // iterate through the array
        int max = 0;
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            // get the sum as we iterate the array
            sum += arr[i];

            // once we've iterated k times we keep a sum as maximum.
            if (i >= k - 1) {
                max = Math.max(max, sum);
                // then we remove the last item add the new item until and confirm it's still the max
                sum -= arr[i - (k - 1)];
            }
        }
        return max;
    }
}
