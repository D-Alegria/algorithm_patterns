"""
    Given an array of points in the a 2D2D plane, find ‘K’ closest points to the origin.

    Example 1:
    Input: points = [[1,2],[1,3]], K = 1
    Output: [[1,2]]
    Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
    The Euclidean distance between (1, 3) and the origin is sqrt(10).
    Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

    Example 2:
    Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
    Output: [[1, 3], [2, -1]]
"""

import heapq


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def distance_from_origin(self):
        return (self.x * self.x) + (self.y * self.y)

    def print_point(self):
        print("[" + str(self.x) + "," + str(self.y) + "] ", end='')


def find_k_closest_points_to_origin(points, k):
    maxHeap = []

    for i in range(k):
        heapq.heappush(maxHeap, points[i])

    for i in range(k, len(points)):
        if points[i].distance_from_origin() < maxHeap[0].distance_from_origin():
            heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, points[i])

    return list(maxHeap)


def find_k_closest_points_to_origin1(points, k):
    points.sort(key=lambda x: x[0] * x[0] + x[1] * x[1])
    return points[:k]


if __name__ == '__main__':
    result = find_k_closest_points_to_origin([Point(1, 2), Point(1, 3)], 1)
    for j in result:
        j.print_point()
    print()
    print(find_k_closest_points_to_origin1([[1, 2], [1, 3]], 1))
    result = find_k_closest_points_to_origin([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    for j in result:
        j.print_point()
    print()
    print(find_k_closest_points_to_origin1([[1, 3], [3, 4], [2, -1]], 2))
