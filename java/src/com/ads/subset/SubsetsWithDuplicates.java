package com.ads.subset;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by Demilade Oladugba on 12/28/2021
 **/

public class SubsetsWithDuplicates {
    public static void main(String[] args) {
        List<List<Integer>> subsets = findSubSetsWithoutDuplicates(new int[]{1, 3, 3});
        System.out.println("Subsets with duplicate" + subsets);

        subsets = findSubSetsWithoutDuplicates(new int[]{1, 5, 3, 3});
        System.out.println("Subsets with duplicate" + subsets);
    }

    public static List<List<Integer>> findSubSetsWithoutDuplicates(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> subsets = new ArrayList<>();
        subsets.add(new ArrayList<>());

        for (int n = 0; n < nums.length; n++) {
            int subsetLength = subsets.size();
            int start = 0;
            if (n > 0 && nums[n - 1] == nums[n]) {
                start = subsetLength / 2;
            }
            for (int i = start; i < subsetLength; i++) {
                List<Integer> set = new ArrayList<>(subsets.get(i));
                set.add(nums[n]);
                subsets.add(set);
            }
        }

        return subsets;
    }
}
