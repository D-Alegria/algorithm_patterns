package com.ads.phastmoney;

import java.util.Arrays;
import java.util.List;

/**
 * Created by Demilade Oladugba on 9/2/2022
 **/

public class AutoDebit {

    public static void main(String[] args) {
        Card card1 = new Card("Card 1", 10000);
        Card card2 = new Card("Card 2", 20000);
        Card card3 = new Card("Card 3", 30000);

        double[] values = autoDebit(List.of(card1, card2, card3), 100000);
        System.out.println(Arrays.toString(values));
        System.out.println(Arrays.stream(values).sum());
    }

    public static double[] autoDebit(List<Card> cards, double debitAmount) {
        double debitedAmount = 0;
        for (Card card : cards) {
            double amountDue = debitAmount;
            do {
//                amountDue = Math.round(amountDue * 100.0) / 100.0;
                double amountDebited = card.debitCard(amountDue);
                if (amountDebited > 0) {
                    debitedAmount += amountDebited;
                    debitAmount -= amountDebited;
                    if (amountDue > debitAmount)
                        amountDue = debitAmount;
                    System.out.println(card);
                } else {
                    amountDue /= 2;
                    if (amountDue < 500)
                        break;
                }
            } while (amountDue > 0);
            if (debitAmount <= 0)
                break;
        }
        for (Card card : cards) {
            System.out.println(card);
        }
        return new double[]{debitAmount, debitedAmount};
    }
}

class Card {
    public String name;
    public double amount;

    Card(String name, double amount) {
        this.name = name;
        this.amount = amount;
    }

    public double debitCard(double debitAmount) {
        System.out.println("Debitamount: " + debitAmount + " amount: " + amount);
        if (debitAmount <= amount) {
            amount -= debitAmount;
            return debitAmount;
        }
        return 0;
    }

    @Override
    public String toString() {
        return "Card{" +
                "name='" + name + '\'' +
                ", amount=" + amount +
                '}';
    }

}
