package com.ads.subset;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Demilade Oladugba on 12/29/2021
 **/

public class EvaluateExpression {

    public static void main(String[] args) {
        List<Integer> result = evaluateExpression("1+2*3");
        System.out.println("EvaluateExpression:" + result);

        result = evaluateExpression("2*3-4-5");
        System.out.println("EvaluateExpression:" + result);

        result = evaluateExpression("2+5-6+9");
        System.out.println("EvaluateExpression:" + result);
    }

    public static List<Integer> evaluateExpression(String expression) {
        List<Integer> result = new ArrayList<>();
        if (expression.length() == 1)
            return new ArrayList<>(List.of(Integer.parseInt(expression)));


        for (int i = 0; i < expression.length(); i++) {
            char operator = expression.charAt(i);
            if (!Character.isDigit(operator)) {
                List<Integer> leftSubtree = evaluateExpression(expression.substring(0, i));
                List<Integer> rightSubtree = evaluateExpression(expression.substring(i + 1));

                for (int left : leftSubtree) {
                    for (int right : rightSubtree) {
                        if (operator == '+')
                            result.add(left + right);
                        else if (operator == '-')
                            result.add(left - right);
                        else if (operator == '*')
                            result.add(left * right);
                    }
                }
            }
        }
        return result;
    }
}
