"""
    Given the head of a LinkedList and a number ‘k’,
    reverse every ‘k’ sized sub-list starting from the head.

    If, in the end, you are left with a sub-list with less than ‘k’ elements,
    reverse it too.
                            p       c
    n   <   1   <   2   <   3   >   4   >   5   >   6   >   7   >   8   > n

                            p       c       n
    n   >   3   >   2   >   1   >   4   >   5   >   6   >   7   >   8   > n

"""


class Node:

    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next_node = next_node

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next_node
        print()


"""

const reverse_every_k_elements = (head, k) => {
    let l = null,
        r = head;

    while (r) {
        let startNode = r,
            i = 0;
        while (r && i < k) {
            let _ = l;
            l = r;
            r = r.next;
            l.next = _;
            i++;
        }
        
        (startNode.next)
            ? startNode.next.next = l
            : head = l;
        startNode.next = r;
        l = startNode
    }
    return head;
}

"""


def reverse_every_k_elements(head_node: Node, k: int) -> Node:  # S = O(1) T = O(N)
    prev = None
    current = head_node

    while current is not None:
        i = 0
        end_of_previous_list = prev
        end_of_new_List = current

        while current is not None and i < k:
            next_node = current.next_node
            current.next_node = prev
            prev = current
            current = next_node
            i += 1

        if end_of_previous_list is not None:
            end_of_previous_list.next_node = prev
        else:
            head_node = prev
        end_of_new_List.next_node = current
        prev = end_of_new_List

    return head_node


if __name__ == '__main__':
    head = Node(1)
    head.next_node = Node(2)
    head.next_node.next_node = Node(3)
    head.next_node.next_node.next_node = Node(4)
    head.next_node.next_node.next_node.next_node = Node(5)
    head.next_node.next_node.next_node.next_node.next_node = Node(6)
    head.next_node.next_node.next_node.next_node.next_node.next_node = Node(7)
    head.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(8)

    print("Original LinkedList are: ", end=" ")
    head.print_list()
    result = reverse_every_k_elements(head, 4)
    print("Reversed LinkedList are: ", end=" ")
    result.print_list()
