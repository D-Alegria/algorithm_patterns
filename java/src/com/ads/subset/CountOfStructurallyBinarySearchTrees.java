package com.ads.subset;

import java.util.HashMap;

/**
 * Created by Demilade Oladugba on 12/29/2021
 **/

public class CountOfStructurallyBinarySearchTrees {

    static HashMap<Integer, Integer> map = new HashMap<>();

    public static void main(String[] args) {
        Integer result = getCountOfTrees(2);
        System.out.println("CountOfStructurallyBinarySearchTrees: " + result);

        result = getCountOfTrees(3);
        System.out.println("CountOfStructurallyBinarySearchTrees: " + result);
    }

    public static Integer getCountOfTrees(int num) {
        if (map.containsKey(num))
            return map.get(num);

        int count = 0;
        if (num <= 1)
            return 1;

        for (int i = 1; i <= num; i++) {
            int leftSubtree = getCountOfTrees(i - 1);
            int rightSubtree = getCountOfTrees(num - i);

            count += leftSubtree * rightSubtree;
        }
        map.put(num, count);
        return count;
    }
}
