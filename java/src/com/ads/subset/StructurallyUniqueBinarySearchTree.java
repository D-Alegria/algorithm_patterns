package com.ads.subset;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Demilade Oladugba on 12/29/2021
 **/

public class StructurallyUniqueBinarySearchTree {

    public static void main(String[] args) {
        List<TreeNode> result = generateTree(2);
        System.out.println("StructurallyUniqueBinarySearchTree " + result);

        result = generateTree(3);
        System.out.println("StructurallyUniqueBinarySearchTree " + result);
    }

    public static List<TreeNode> generateTree(int num) {
        return generateTree(1, num);
    }

    public static List<TreeNode> generateTree(int start, int end) {
        List<TreeNode> result = new ArrayList<>();
        if (start > end) {
            result.add(null);
            return result;
        }

        for (int i = start; i <= end; i++) {
            List<TreeNode> leftSubtree = generateTree(start, i - 1);
            List<TreeNode> rightSubtree = generateTree(i + 1, end);

            for (TreeNode left : leftSubtree) {
                for (TreeNode right : rightSubtree) {
                    result.add(new TreeNode(i, left, right));
                }
            }
        }
        return result;
    }
}

class TreeNode {
    private final int val;
    private TreeNode left;
    private TreeNode right;

    public TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    TreeNode(int val) {
        this.val = val;
    }

    @Override
    public String toString() {
        return "TreeNode{" +
                "val=" + val +
                ", left=" + left +
                ", right=" + right +
                '}';
    }
}
