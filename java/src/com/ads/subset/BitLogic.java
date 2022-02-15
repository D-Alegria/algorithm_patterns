package com.ads.subset;

/**
 * Created by Demilade Oladugba on 2/10/2022
 **/

public class BitLogic {

    public static void main(String[] args) {
        int result = bitLogic(1, 3, 3);
        System.out.println("Bit Logic: " + result);

        result = bitLogic(3, 5, 6);
        System.out.println("Bit Logic: " + result);
    }

    public static int bitLogic(int low, int high, int k) {
        int count = 0;
        for (int a = low; a < high; a++) {
            for (int b = a + 1; b <= high; b++) {
                int x = a ^ b;
                if (x <= k)
                    count++;
            }
        }
        return count;
    }
}
