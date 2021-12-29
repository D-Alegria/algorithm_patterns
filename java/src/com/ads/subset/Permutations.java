package com.ads.subset;

import java.util.*;

/**
 * Created by Demilade Oladugba on 12/29/2021
 **/

public class Permutations {

    public static void main(String[] args) {
        List<List<Integer>> result = findPermutations(new int[]{1, 3, 5});
        System.out.println("Permutations:" + result);

        result = findPermutationsRecursive(new int[]{1, 3, 5});
        System.out.println("Permutations:" + result);

        result = findPermutationsDFS(new int[]{1, 3, 5});
        System.out.println("Permutations:" + result);
    }

    public static List<List<Integer>> findPermutations(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Queue<List<Integer>> permutations = new LinkedList<>();
        permutations.add(new ArrayList<>());

        for (int num : nums) {
            int size = permutations.size();
            for (int i = 0; i < size; i++) {
                List<Integer> current = permutations.poll();
                if (current != null) {
                    for (int j = 0; j < current.size() + 1; j++) {
                        List<Integer> temp = new ArrayList<>(current);
                        temp.add(j, num);
                        if (temp.size() == nums.length) {
                            result.add(temp);
                        } else {
                            permutations.add(temp);
                        }
                    }
                }
            }
        }

        return result;
    }


    public static List<List<Integer>> findPermutationsRecursive(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        findPermutationsRecursive(nums, new ArrayList<>(), 0, result);
        return result;
    }

    /*
     *
     * {[1,3,5], [5,3,1], 2,[]}
     * {[1,3,5], [3,1], 2,[]}
     * {[1,3,5], [1], 1,[]}
     * {[1,3,5], [], 0,[]}
     * */
    public static void findPermutationsRecursive(int[] nums, List<Integer> currentPermutation, int index, List<List<Integer>> result) {
        if (currentPermutation.size() == nums.length) {
            result.add(currentPermutation);
        } else {
            for (int i = 0; i < currentPermutation.size() + 1; i++) {
                List<Integer> temp = new ArrayList<>(currentPermutation);
                temp.add(i, nums[index]);
                findPermutationsRecursive(nums, temp, index + 1, result);
            }
        }
    }

    /*
     * [5]
     * [1,3] ->
     * [1,3,5] -> [5,3,1],[3,5,1],[5,1,3],[1,5,3],[3,1,5],[1,3,5]
     * */
    public static List<List<Integer>> findPermutationsDFS(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums.length == 1) {
            result.add(new ArrayList<>(List.of(nums[0])));
            return result;
        }

        for (int num : nums) {
            int[] temp = Arrays.stream(nums).filter(value -> value != num).toArray();
            List<List<Integer>> permutations = findPermutationsDFS(temp);

            for (List<Integer> permutation : permutations) {
                permutation.add(num);
                result.add(permutation);
            }
        }
        return result;
    }
}
