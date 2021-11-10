"""
    Given a binary tree and a number ‘S’,
    find all paths in the tree such that the sum of all the node values of each path equals ‘S’.
    Please note that the paths can start or end at any node but all paths must follow direction
    from parent to child (top to bottom).
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_count(root_node, s, currentPath, count):
    if not root_node:
        return 0

    currentPath.append(root_node.val)
    if not root_node.left and not root_node.right:
        currentSum = 0
        back = 0
        for n in currentPath:
            currentSum += n
            if currentSum == s:
                count[0] = count[0] + 1
            while currentSum > s:
                currentSum -= currentPath[back]
                back += 1

    get_count(root_node.left, s, currentPath, count)
    get_count(root_node.right, s, currentPath, count)

    currentPath.pop()


def count_paths(root_node, s) -> int:
    count = [0]
    get_count(root_node, s, [], count)
    return count[0]


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))

""""
    My phone died 
    wow..but you have powerbank yh?
    yep
    aiit
    
    check the solution though
"""
