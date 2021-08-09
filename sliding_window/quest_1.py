import time

"""
    Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
    Input
    Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
"""

"""

get the number of sub arrays = 
length - K + 1
9      - 5 + 1 = 5

sub arrays = 
    [1, 3, 2, 6, -1]
    [3, 2, 6, -1, 4]
    [2, 6, -1, 4, 1]
    [6, -1, 4, 1, 8]
    [-1, 4, 1, 8, 2]
"""


def find_averages(k, arr):
    result = []
    for index1 in range(len(arr) - k + 1):  # k
        aver = 0
        for j in range(k):  # k
            aver += arr[index1 + j]
        result.append(aver / k)
    return result


def find_averages_opt(k, arr):
    result = []
    for index2 in range(len(arr) - k + 1):
        result.append(sum(arr[index2:index2 + k]) / k)
    return result


def find_averages_opt2(k, arr):
    result = []
    back = 0
    added = 0
    for index3 in range(len(arr)):
        added += arr[index3]
        if index3 >= k - 1:
            result.append(added / k)
            added -= arr[back]
            back += 1
    return result


time1 = 0
time2 = 0
time3 = 0
testAmount = 10000000
print("Function 1: %s" % (find_averages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])))
start = time.time()
# time.sleep(1)
for i in range(testAmount):
    find_averages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
# time.sleep(1)
end = time.time()
time1 = end - start

print("Function 2: %s" % (find_averages_opt(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])))
start = time.time()
# time.sleep(1)
for i in range(testAmount):
    find_averages_opt(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
# time.sleep(1)
end = time.time()
time2 = end - start

print("Function 3: %s" % (find_averages_opt2(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])))
start = time.time()
# time.sleep(1)
for i in range(testAmount):
    find_averages_opt2(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
# time.sleep(1)
end = time.time()
time3 = end - start

print("Average of Function 1: %s" % time1)
print("Average of Function 2: %s" % time2)
print("Average of Function 3: %s" % time3)

print("Minimum %s" % (min(time1, time2, time3)))
print("Maximum %s" % (max(time1, time2, time3)))
