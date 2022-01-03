"""
    Given a binary tree and a number ‘S’,
    find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths_recursion(root_node, s, path, allPaths):
    if not root_node:
        return

    path.append(root_node.val)
    if root_node.val == s and not root_node.left and not root_node.right:
        allPaths.append(path.copy())

    find_paths_recursion(root_node.left, s - root_node.val, path, allPaths)
    find_paths_recursion(root_node.right, s - root_node.val, path, allPaths)

    path.pop()


def find_paths(root_node, s):
    allPaths = []
    find_paths_recursion(root_node, s, [], allPaths)
    return allPaths


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    total = 23
    print("Tree paths with sum " + str(total) + ": " + str(find_paths(root, total)))
