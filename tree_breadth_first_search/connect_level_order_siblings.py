"""
    Given a binary tree,
    connect each node with its level order successor.
    The last node of each level should point to a null node.
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings(root_node: TreeNode) -> None:  # S = O(N)  T = O(N)
    queue = deque()

    queue.append(root_node)
    while queue:
        lenLevel = len(queue)
        currentNode = None
        for i in range(lenLevel):
            current = queue.popleft()
            if not currentNode:
                currentNode = current
            else:
                currentNode.next = current
                currentNode = currentNode.next

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()
