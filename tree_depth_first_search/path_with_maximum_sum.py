"""
    Find the path with the maximum sum in a given binary tree.
    Write a function that returns the maximum sum.
    A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root.
"""
import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_maximum_path_sum(root_node):
    def calculate_path(root_nod, maximum):
        if not root_nod:
            return 0

        leftSubTree = calculate_path(root_nod.left, maximum)
        rightSubTree = calculate_path(root_nod.right, maximum)

        maximum[0] = max(maximum[0], root_nod.val + max(leftSubTree, 0) + max(rightSubTree, 0))
        return root_nod.val + max(leftSubTree, rightSubTree)

    maxi = [-math.inf]
    calculate_path(root_node, maxi)
    return maxi[0]


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum:  " + str(find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)

    print("Maximum Path Sum:  " + str(find_maximum_path_sum(root)))
    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum:  " + str(find_maximum_path_sum(root)))
