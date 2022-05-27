"""
    There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’.
    Each task can have some prerequisite tasks which need to be completed before it can be scheduled.
    Given the number of tasks and a list of prerequisite pairs,
    write a method to print all possible ordering of tasks meeting all prerequisites.

    Example 1:
    Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
    Output: [0, 1, 2]
    Explanation: There is only possible ordering of the tasks.

    Example 2:
    Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
    Output:
    1) [3, 2, 0, 1]
    2) [3, 2, 1, 0]
    Explanation: There are two possible orderings of the tasks meeting all prerequisites.

    Example 3:
    Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
    Output:
    1) [0, 1, 4, 3, 2, 5]
    2) [0, 1, 3, 4, 2, 5]
    3) [0, 1, 3, 2, 4, 5]
    4) [0, 1, 3, 2, 5, 4]
    5) [1, 0, 3, 4, 2, 5]
    6) [1, 0, 3, 2, 4, 5]
    7) [1, 0, 3, 2, 5, 4]
    8) [1, 0, 4, 3, 2, 5]
    9) [1, 3, 0, 2, 4, 5]
    10) [1, 3, 0, 2, 5, 4]
    11) [1, 3, 0, 4, 2, 5]
    12) [1, 3, 2, 0, 5, 4]
    13) [1, 3, 2, 0, 4, 5]
"""

from collections import defaultdict, deque


def print_orders(tasks, prerequisites):
    orders = []
    graph = defaultdict(list)
    inDegree = {i: 0 for i in range(tasks)}

    # create the graph
    for prerequisite in prerequisites:
        parent, child = prerequisite[0], prerequisite[1]
        inDegree[child] += 1
        graph[parent].append(child)

    # get sources
    sources = deque()
    for key in inDegree.keys():
        if inDegree[key] == 0:
            sources.append([key])

    # delete 0s
    for source in sources:
        del inDegree[source[0]]

    # get children
    while inDegree:
        currentSource = sources.popleft()
        for child in graph[currentSource[-1]]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append([*currentSource, child])
                del inDegree[child]

    print(sources)


if __name__ == '__main__':
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
