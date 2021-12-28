"""
    Count of Structurally Unique Binary Search Trees (hard) #
    Given a number ‘n’,
    write a function to return the count of structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’.

    Example 1:
    Input: 2
    Output: 2
    Explanation: As we saw in the previous problem, there are 2 unique BSTs storing numbers from 1-2.

    Example 2:
    Input: 3
    Output: 5
    Explanation: There will be 5 unique BSTs that can store numbers from 1 to 5.
"""


def find_unique_trees1(n):
    my_arr = [i + 1 for i in range(n)]

    def get_count(ar):
        result = []
        if len(ar) == 0:
            return [0]
        for i in range(len(ar)):
            leftSubTree = get_count(ar[:i])
            rightSubTree = get_count(ar[i + 1:])

            for l in leftSubTree:
                for r in rightSubTree:
                    result.append(l + r + 1)
        return result

    return len(get_count(my_arr))


def find_unique_trees(n):
    def get_count(num):
        if num <= 1:
            return 1

        count = 0
        for i in range(1, num + 1):
            leftSubtree = get_count(i - 1)
            rightSubtree = get_count(num - i)
            count += (leftSubtree * rightSubtree)
        return count

    return get_count(n)


if __name__ == '__main__':
    # print(f"len: {find_unique_trees(1)}")
    print(f"len: {find_unique_trees(2)}")
    print(f"len: {find_unique_trees(3)}")
