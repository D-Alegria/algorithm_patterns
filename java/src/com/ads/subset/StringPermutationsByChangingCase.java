package com.ads.subset;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Created by Demilade Oladugba on 12/29/2021
 **/

public class StringPermutationsByChangingCase {
    public static void main(String[] args) {
        List<String> subsets = findLetterChangeCaseStringPermutation("ad52");
        System.out.println("StringPermutationsByChangingCase " + subsets);

        subsets = findLetterChangeCaseStringPermutation("ab7c");
        System.out.println("StringPermutationsByChangingCase " + subsets);
    }

    public static List<String> findLetterChangeCaseStringPermutation(String str) {
        Queue<String> permutations = new LinkedList<>();
        permutations.add(str);

        for (int i = 0; i < str.length(); i++) {
            if (Character.isLetter(str.charAt(i))) {
                int n = permutations.size();
                for (int j = 0; j < n; j++) {
                    String temp = permutations.poll();
                    if (temp != null) {
                        char[] newPermutation = temp.toCharArray();
                        if (Character.isUpperCase(newPermutation[i])) {
                            newPermutation[i] = String.valueOf(newPermutation[i]).toLowerCase().charAt(0);
                        } else {
                            newPermutation[i] = String.valueOf(newPermutation[i]).toUpperCase().charAt(0);
                        }
                        permutations.add(temp);
                        permutations.add(String.valueOf(newPermutation));
                    }
                }
            }
        }

        return new ArrayList<>(permutations);
    }
}
