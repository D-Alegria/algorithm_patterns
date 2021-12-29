package com.ads.subset;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Created by Demilade Oladugba on 12/29/2021
 **/

public class UniqueGeneralizedAbbreviations {

    public static void main(String[] args) {
        List<String> result = generateUniqueGeneralizedAbbreviation("BAT");
        System.out.println("UniqueGeneralizedAbbreviations:" + result);

        result = generateUniqueGeneralizedAbbreviation("code");
        System.out.println("UniqueGeneralizedAbbreviations:" + result);

        result = generateUniqueGeneralizedAbbreviation("Demilade");
        System.out.println("UniqueGeneralizedAbbreviations:" + result);
    }

    /*
     * [(3,""),(0,"2T"),(1,"1A"),(0,"1AT"),(2,"B"),(0,"B1T"),(1,"BA"),(0,"BAT")]
     * [(2,""),(0,"1A"),(1,"B"),(0,"BA")]
     * [(1,""),(0,"B")]
     * [(0,"")]
     * */

    public static List<String> generateUniqueGeneralizedAbbreviation(String word) {
        Queue<Abbreviation> queue = new LinkedList<>();
        queue.add(new Abbreviation(0, ""));

        for (char c : word.toCharArray()) {
            int n = queue.size(); // 1
            for (int i = 0; i < n; i++) {
                Abbreviation current = queue.poll();
                if (current == null)
                    continue;
                queue.add(new Abbreviation(current.getCount() + 1, current.getStr()));

                if (current.getCount() > 0)
                    current.setStr(current.getStr() + current.getCount());

                Abbreviation newWord = new Abbreviation(0, current.getStr());
                newWord.setStr(newWord.getStr() + c);
                queue.add(newWord);
            }
        }

        List<String> result = new ArrayList<>();
        Abbreviation current = queue.poll();
        while (current != null) {
            if (current.getCount() > 0)
                current.setStr(current.getStr() + current.getCount());
            result.add(current.getStr());
            current = queue.poll();
        }
        return result;
    }
}


class Abbreviation {
    private final int count;
    private String str;

    public Abbreviation(int count, String str) {
        this.count = count;
        this.str = str;
    }

    public int getCount() {
        return count;
    }

    public String getStr() {
        return str;
    }

    public void setStr(String str) {
        this.str = str;
    }
}