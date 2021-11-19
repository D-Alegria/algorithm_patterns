package com.ads.sliding_window;

/**
 * Created by Demilade Oladugba on 11/19/2021
 **/

/*
                *       !
    2   1   5   2   3   2

    s = 5
    m = 2
*/

public class SmallestSubArrayWIthAGivenSum {

    public static void main(String[] args) {
        System.out.println("Min length is " + findMinSubArray(7, new int[]{2, 1, 5, 2, 3, 2}));
        System.out.println("Min length is " + findMinSubArray(7, new int[]{2, 1, 5, 2, 8}));
        System.out.println("Min length is " + findMinSubArray(8, new int[]{3, 4, 1, 1, 6}));
    }

    public static int findMinSubArray(int s, int[] arr) {
        int sum = 0, back = 0;
        int min = Integer.MAX_VALUE;
        // iterate through the arr
        for (int i = 0; i < arr.length; i++) {
            // sum each item until it's greater than s
            sum += arr[i];

            while (sum >= s) {
                // store the length of the items
                min = Math.min(min, (i - back) + 1);
                // remove items from the back while the sum is greater than s
                sum -= arr[back++];
            }
        }
        return min;
    }
}
