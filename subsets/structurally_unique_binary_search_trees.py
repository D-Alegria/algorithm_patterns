"""
    Given a number ‘n’,
    write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?

    Example 1:
    Input: 2
    Output: 2
    Explanation: Here are all the structurally unique BSTs storing all numbers from 1 to 2:


    r = [none]
    p = 3
    l [none]
    result [(3,n,n)]
    [3]

    r []
    p 3
    l[2]
    result [(2,n,(3,n,n))]
    [2,3]

    r[2,3]
    p 1
    l[none]
    res []
    [1,2,3]

    Example 2:
    Input: 3
    Output: 5
    Explanation: Here are all the structurally unique BSTs storing all numbers from 1 to 3:

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def toString(self):
        print(f"Tree node: {self.val},", end=" ")
        if self.left:
            print(f"l:", end=" ")
            self.left.toString()
        if self.right:
            print(f"r:", end=" ")
            self.right.toString()
        print()


def toStringList(arr):
    for ar in arr:
        if ar:
            ar.toString()
        else:
            print(ar)


def find_unique_trees(n):
    def get_unique(ar):

        result = []
        if len(ar) == 0:
            return [None]

        for i in range(len(ar)):
            leftSubtree = get_unique(ar[:i])
            rightSubtree = get_unique(ar[i + 1:])

            for left in leftSubtree:
                for right in rightSubtree:
                    tree = TreeNode(ar[i])
                    tree.right = right
                    tree.left = left
                    result.append(tree)
        return result

    arr = [i + 1 for i in range(n)]
    x = get_unique(arr)
    toStringList(x)
    return len(x)


if __name__ == '__main__':
    # print(f"len: {find_unique_trees(1)}")
    print(f"len: {find_unique_trees(2)}")
    print(f"len: {find_unique_trees(3)}")
