"""
    Frequency Stack (hard) #
    Design a class that simulates a Stack data structure,
    implementing the following two operations:

    push(int num): Pushes the number ‘num’ on the stack.
    pop(): Returns the most frequent number in the stack.
    If there is a tie, return the number which was pushed later.

    Example:
    After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)

    1. pop() should return 2, as it is the most frequent number
    2. Next pop() should return 1
    3. Next pop() should return 2

    {1:2,2:3,3:1,5:1}
    []
    [2,1,5,3]
    pop
    [1,2,5,3]

"""

from heapq import heappush, heappop


class FrequencyStack:

    def __init__(self):
        self.frequencyMap = {}
        self.maxHeap = []
        self.sequence = 0

    def push(self, num):
        self.frequencyMap[num] = self.frequencyMap.get(num, 0) + 1
        heappush(self.maxHeap, [-self.frequencyMap[num], -self.sequence, num])
        self.sequence += 1

    def pop(self):
        num = heappop(self.maxHeap)[2]
        if self.frequencyMap[num] > 0:
            self.frequencyMap[num] -= 1
        else:
            del self.frequencyMap[num]
        self.sequence -= 1
        return num


if __name__ == '__main__':
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())
