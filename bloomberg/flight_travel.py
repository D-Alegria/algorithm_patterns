"""
    I had my onsite a few days ago. They started off with introductions
    which took 20 mins and then I gave my introduction. Opened link to
    hackerrank and saw a non leetcode question. You have flights e.g.

    A->B
    B-> C,D
    C-E
    D-E

    Had to implement 2 methods. One was to add a new start and end location.
    The other was to print all locations from a starting point to a destination
    e.g. print all possible travel methods from A to E.
    Follow up: How to make your solution more efficient
    if you knew that an airport was not going to get you to your destination
"""
from collections import defaultdict, deque


class FlightTravel:

    def __init__(self):
        self.routes = defaultdict(list)

    def addRoute(self, start, end):
        self.routes[start].append(end)

    def getAllRoutes(self, start, end):
        queue = deque()
        queue.append([start])
        result = []

        while queue:
            current = queue.popleft()

            if current[-1] == end:
                result.append(current)
            else:
                for place in self.routes[current[-1]]:
                    if place not in current:
                        queue.append(current + [place])
        return result


if __name__ == '__main__':
    travel = FlightTravel()
    travel.addRoute('A', 'B')
    travel.addRoute('A', 'P')
    travel.addRoute('P', 'E')
    travel.addRoute('B', 'C')
    travel.addRoute('B', 'D')
    travel.addRoute('C', 'G')
    travel.addRoute('C', 'A')
    travel.addRoute('G', 'E')
    travel.addRoute('C', 'E')
    travel.addRoute('D', 'E')
    travel.addRoute('E', 'P')
    print(travel.getAllRoutes('A', 'E'))
