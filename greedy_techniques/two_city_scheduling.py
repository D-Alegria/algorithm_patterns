"""

"""


def two_city_scheduling(costs):
    costs.sort(key=lambda x: x[0] - x[1])
    minimumCost = 0

    for j in range(len(costs)):
        minimumCost += costs[j][0] if j < len(costs) // 2 else costs[j][1]

    return minimumCost

if __name__ == '__main__':
    input_costs = [
        [[10, 20],
         [30, 200],
         [400, 50],
         [30, 20]],

        [[259, 770],
         [448, 54],
         [926, 667],
         [184, 139],
         [840, 118],
         [577, 469]],

        [[515, 563],
         [451, 713],
         [537, 709],
         [343, 819],
         [855, 779],
         [457, 60],
         [650, 359],
         [631, 42]],

        [[1, 2],
         [3, 4],
         [5, 6],
         [7, 8]],

        [[1, 2],
         [1, 2],
         [1, 2],
         [1, 2]]]

    for i in range(len(input_costs)):
        print("Test Case #", i + 1)
        print(
            "\nThe minimum cost to send people equally into City A and B when the costs are ", input_costs[i], " is:",
            two_city_scheduling(input_costs[i]))
        print("-" * 100)