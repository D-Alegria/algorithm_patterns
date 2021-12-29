package com.ads.subset;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Created by Demilade Oladugba on 12/29/2021
 **/

public class BalanceParentheses {

    public static void main(String[] args) {
        List<String> result = generateValidParentheses(1);
        System.out.println("BalanceParentheses:" + result);

        result = generateValidParentheses(2);
        System.out.println("BalanceParentheses:" + result);

        result = generateValidParentheses(3);
        System.out.println("BalanceParentheses:" + result);
    }

    /*
     * start with an empty string
     * if open is less than num of permutations
     * add an open parentheses
     *
     * if the open parentheses is greater than the close parentheses
     * add closing parentheses
     *
     * */

    public static List<String> generateValidParentheses(int num) {
        List<String> result = new ArrayList<>();
        Queue<Parentheses> parentheses = new LinkedList<>();
        parentheses.add(new Parentheses("", 0, 0));

        while (parentheses.size() > 0) {
            Parentheses current = parentheses.poll();
            if (current.getOpen() == num && current.getClose() == num) {
                result.add(current.getStr());
            } else {
                if (current.getOpen() < num)
                    parentheses.add(new Parentheses(current.getStr() + "(", current.getOpen() + 1, current.getClose()));
                if (current.getOpen() > current.getClose())
                    parentheses.add(new Parentheses(current.getStr() + ")", current.getOpen(), current.getClose() + 1));
            }
        }

        return result;
    }
}

class Parentheses {
    private String str;
    private int open;
    private int close;

    public Parentheses(String str, int open, int close) {
        this.str = str;
        this.open = open;
        this.close = close;
    }


    public int getOpen() {
        return open;
    }

    public void setOpen(int open) {
        this.open = open;
    }

    public String getStr() {
        return str;
    }

    public void setStr(String str) {
        this.str = str;
    }

    public int getClose() {
        return close;
    }

    public void setClose(int close) {
        this.close = close;
    }
}
