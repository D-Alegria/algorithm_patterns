"""

"""


def rescue_boats(people, limit):
    people.sort()

    start, end = 0, len(people) - 1
    count = 0

    while start < end:
        if people[start] + people[end] < limit:
            start += 1
        end -= 1
        count += 1
    return count


if __name__ == '__main__':
    peopleQuestion = [[1, 2], [3, 2, 2, 1], [3, 5, 3, 4], [
        5, 5, 5, 5], [1, 2, 3, 4], [1, 2, 3, 4, 5], [3, 4, 5]]
    limitQuestion = [3, 3, 5, 5, 5, 3, 1]
    for i in range(len(peopleQuestion)):
        print(i + 1, "\tWeights = ", peopleQuestion[i], sep="")
        print("\tWeight Limit = ", limitQuestion[i], sep="")
        print("\tThe minimum number of boats required to save people are ",
              rescue_boats(peopleQuestion[i], limitQuestion[i]), sep="")
        print("-" * 100)
