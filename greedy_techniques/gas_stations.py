"""
   There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i];

   We have a car with an unlimited gas tank and cost 'costs[i]' of gas to travel from the ith station to it's next
   (i + 1)th station. We begin the journey with an empty tank at one of the gas stations.

   Given two integer arrays, gas and cost, return the starting gas station's index  if we can travel around the circuit
   once in the clockwise direction. Otherwise, return -1
"""


def gas_station_journey(gas, cost):
    result = -1
    if sum(gas) < sum(cost):
        return result

    n = len(gas)

    for i in range(n):
        total_gas = 0
        for j in range(n):
            total_gas += gas[(i + j) % n] - cost[(i + j) % n]
            if total_gas < 0:
                break
        result = i
        if total_gas == 0:
            break

    return result


def gas_station_journey_1(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    n = len(gas)
    total_gas = 0
    result = 0

    for i in range(n):
        total_gas += gas[i] - cost[i]
        if total_gas < 0:
            total_gas = 0
            result = i + 1

    return result


if __name__ == '__main__':
    print(gas_station_journey_1([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(gas_station_journey_1([2, 3, 4], [3, 4, 3]))
    print(gas_station_journey_1([1, 1, 1, 1, 10], [2, 2, 1, 3, 1]))
    print(gas_station_journey_1([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]))
    print(gas_station_journey_1([1], [1]))

    gas_station = [[1, 2, 3, 4, 5], [2, 3, 4], [1, 1, 1, 1, 1], [1, 1, 1, 1, 10], [1, 1, 1, 1, 1], [1, 2, 3, 4, 5]]
    cost_s = [[3, 4, 5, 1, 2], [3, 4, 3], [1, 2, 3, 4, 5], [2, 2, 1, 3, 1], [1, 0, 1, 2, 3], [1, 2, 3, 4, 5]]
    for k in range(len(gas_station)):
        print(k + 1, ".\tGas = ", gas_station[k])
        print("\tCost = ", cost_s[k])
        print("\n \tThe index of the gas station we can start our journey from is ", gas_station_journey(
            gas_station[k], cost_s[k]), " (If it's -1, then that \n \tmeans no solution exists)", sep="")
        print("-" * 100)
