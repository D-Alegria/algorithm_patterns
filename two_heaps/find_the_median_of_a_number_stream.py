"""
    Design a class to calculate the median of a number stream.
    The class should have the following two methods:

        1. insertNum(int num): stores the number in the class
        2. findMedian(): returns the median of all numbers inserted in the class

    If the count of numbers inserted in the class is even,
    the median will be the average of the middle two numbers.
"""

from heapq import *


class MedianOfAStream:

    def __init__(self):
        self.heap = []
        self.count = 0
        heapify(self.heap)

    def insert_num(self, num):
        heappush(self.heap, num)
        self.count += 1

    def find_median(self):
        if self.count % 2 == 0:
            return self.heap[len(self.heap) // 2] + self.heap[(len(self.heap) // 2) - 1] / 2
        else:
            return self.heap[len(self.heap) // 2]


if __name__ == '__main__':
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))
