package com.ads.subset;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Demilade Oladugba on 12/28/2021
 **/

public class SubSets {

    public static void main(String[] args) {
        List<List<Integer>> subsets = findSubSets(new int[]{1, 3});
        System.out.println("Subsets " + subsets);

        subsets = findSubSets(new int[]{1, 5, 3});
        System.out.println("Subsets " + subsets);
    }

    public static List<List<Integer>> findSubSets(int[] nums) {
        List<List<Integer>> subsets = new ArrayList<>();
        subsets.add(new ArrayList<>());

        for (int num : nums) {
            int subsetLength = subsets.size();
            for (int i = 0; i < subsetLength; i++) {
                List<Integer> set = new ArrayList<>(subsets.get(i));
                set.add(num);
                subsets.add(set);
            }
        }

        return subsets;
    }
}


