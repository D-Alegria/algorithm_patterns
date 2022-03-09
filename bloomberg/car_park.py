"""
    The spaces are all the same size and will fit all vehicles that come.

    This car park has one attendant, whose job it is to take the key from arriving drivers, and park the car.
    He will want to park in the first available slot from the start to avoid walking too much.
    Later, when a driver wants to collect his car, the attendant needs to look up the car's location (by a unique ID,
    like registration plate) and retrieve the car for the driver. This will leave an empty slot.
    So for example, after a while, we might have a car park that looks like this:

    A B _ D E _ G _ _ _ _
    So it can be seen that, after a while, the car park becomes fragmented. So as an optimisation,
    when the attendant has free time, he will want to consider a "defrag" operation which will close up the empty slots
    and move the vehicles nearer the start. So for example the above would become:
    A B D E G _ _ _ _ _ _
    or
    A B G D E _ _ _ _ _ _

    Please address the "defrag" operation after you are happy with the park & retrieve operations.
    For verification, we will want "unit tests" (these can just be calls from main) which show the state of the car park
    after each change (park, retrieve, defrag).

    Example 1
    park("A")
    park("B")
    park("C")
    unpark("B")
    park("D")
    Expected output:
    A _ _ _ _ _ _ _ _ _
    A B _ _ _ _ _ _ _ _
    A B C _ _ _ _ _ _ _
    A _ C _ _ _ _ _ _ _
    A D C _ _ _ _ _ _ _

    Example 2
    park("A");
    park("B");
    park("C");
    park("D");
    park("E");
    unpark("D");
    unpark("B");
    defrag();
    *Expected Output:
    A _ _ _ _ _ _ _ _ _
    A B _ _ _ _ _ _ _ _
    A B C _ _ _ _ _ _ _
    A B C D _ _ _ _ _ _
    A B C D E _ _ _ _ _
    A B C _ E _ _ _ _ _
    A _ C _ E _ _ _ _ _
    A E C _ _ _ _ _ _ _
"""

from heapq import *


class CarPark:

    def __init__(self, n):
        self.size = n
        self.garage = ['_'] * n
        self.carPark = {}
        self.available = []

        for i in range(n):
            heappush(self.available, i)

    def park(self, carId):
        space = heappop(self.available)
        self.garage[space] = carId
        self.carPark[carId] = space
        return ''.join(self.garage)

    def unpark(self, carId):
        space = self.carPark[carId]
        self.garage[space] = '_'
        heappush(self.available, space)
        del self.carPark[carId]
        return ''.join(self.garage)

    def rePark(self, carId):
        self.unpark(carId)
        self.park(carId)

    def defrag(self):
        rePark = []
        for carId in self.carPark.keys():
            if self.carPark[carId] > self.available[0]:
                rePark.append(carId)

        for carId in rePark:
            if self.carPark[carId] > self.available[0]:
                self.rePark(carId)
        return ''.join(self.garage)

# def __init__(self):
#     self.size = 10
#     self.garage = {}
#     self.garage_spaces = ["_"] * self.size
#     self.currentSpace = 0
#     self.available_spaces = []
#
# def park(self, carId):
#     if len(self.available_spaces) == 0:
#         self.garage[carId] = self.currentSpace
#         self.garage_spaces[self.currentSpace] = carId
#         self.currentSpace += 1
#     else:
#         space = heappop(self.available_spaces)
#         self.garage[carId] = space
#         self.garage_spaces[space] = carId
#     return ''.join(self.garage_spaces)
#
# def unpark(self, carId):
#     if carId in self.garage:
#         space = self.garage[carId]
#         del self.garage[carId]
#         self.garage_spaces[space] = '_'
#         heappush(self.available_spaces, space)
#     return ''.join(self.garage_spaces)
#
# def repark(self, carId):
#     self.unpark(carId)
#     self.park(carId)
#
# def defrag(self):
#     move_cars = []
#     for i in range(len(self.garage_spaces) - 1, -1, -1):
#         if self.garage_spaces[i] != '_' and i > self.available_spaces[0]:
#             move_cars.append(self.garage_spaces[i])
#
#     for i in move_cars:
#         if self.garage[i] > self.available_spaces[0]:
#             self.repark(i)
#
#     return ''.join(self.garage_spaces)


if __name__ == '__main__':
    carPark1 = CarPark(10)
    print(carPark1.park("A"))
    print(carPark1.park("B"))
    print(carPark1.park("C"))
    print(carPark1.unpark("B"))
    print(carPark1.park("D"))
    print()
    carPark2 = CarPark(10)
    print(carPark2.park("A"))
    print(carPark2.park("B"))
    print(carPark2.park("C"))
    print(carPark2.park("D"))
    print(carPark2.park("E"))
    print(carPark2.unpark("D"))
    print(carPark2.unpark("B"))
    print(carPark2.defrag())
