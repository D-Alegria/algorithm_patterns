"""
    Scheduling Tasks (hard) #
    You are given a list of tasks that need to be run, in any order,
    on a server. Each task will take one CPU interval to execute but once a task has finished, it has a cooling period during which it can’t be run again. If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that the server needs to finish all tasks.

    If at any time the server can’t execute any task then it must stay idle.

    Example 1:

    Input: [a, a, a, b, c, c], K=2
    Output: 7
    Explanation: a -> c -> b -> a -> c -> idle -> a
    Example 2:

    counter -> {a:3,b:1,c:2}
    heap ->
    queue -> (a,1),(c,0)
    result -> a->c->b->a->c->


    Input: [a, b, a], K=3
    Output: 5
    Explanation: a -> b -> idle -> idle -> a

    counter -> {a:2,b:1}
    heap -> (a,1)
    queue -> (b,0),(idea,0),(idea,0),(a,0)
    result -> a->b->idle->idle->a
"""

from collections import Counter, deque
from heapq import heappush, heappop


def schedule_tasks(tasks, k):
    counter = Counter(tasks)
    maxHeap = []

    for v, c in counter.items():
        heappush(maxHeap, (-c, v))

    count = 0
    queue = deque()
    validTaskInQueue = 0
    while maxHeap or queue:
        if maxHeap:
            c, v = heappop(maxHeap)
            c += 1
            count += 1
            if -c > 0:
                validTaskInQueue += 1
            queue.append((c, v))
            if len(queue) == k + 1:
                c, v = queue.popleft()
                if -c > 0:
                    validTaskInQueue -= 1
                    heappush(maxHeap, (c, v))
        else:
            if not validTaskInQueue:
                break
            heappush(maxHeap, (-1, 'n'))

    return count


def schedule_tasks1(tasks, k):
    if k == 0:
        return len(tasks)

    count = Counter(tasks).most_common()
    maxCount = count[0][1]
    argMaxCount = 1
    i = 1
    while i < len(count):
        if count[i][1] == count[i - 1][1]:
            argMaxCount += 1
        else:
            break
        i += 1

    return max(len(tasks), (k + 1) * (maxCount - 1) + argMaxCount)


if __name__ == '__main__':
    print("Minimum intervals needed to execute all tasks: " + str(schedule_tasks1(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum intervals needed to execute all tasks: " + str(schedule_tasks1(['a', 'b', 'a'], 3)))
    print("Minimum intervals needed to execute all tasks: " + str(schedule_tasks1(["A", "A", "A", "B", "B", "B"], 2)))
    print("Minimum intervals needed to execute all tasks: " + str(schedule_tasks1(["A", "A", "A", "B", "B", "B"], 0)))
    print("Minimum intervals needed to execute all tasks: " + str(
        schedule_tasks(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)))
