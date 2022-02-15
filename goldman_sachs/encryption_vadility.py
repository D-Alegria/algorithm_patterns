"""

    1 3
    1,2
    1,3
    2,3

"""


def encryptionValidity(instructionCount, validityPeriod, keys):
    pass


def bitLogic(low, high, k):
    count = 0
    for a in range(low, high):
        for b in range(a + 1, high + 1):
            if a ^ b <= k:
                count += 1

    return count


if __name__ == '__main__':
    print(encryptionValidity(1000, 10000, [2, 4, 8, 2]))
    print(bitLogic(1, 3, 3))
