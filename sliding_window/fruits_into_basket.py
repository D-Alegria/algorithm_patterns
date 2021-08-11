"""
    Given an array of characters where each character represents a fruit tree,
    you are given two baskets and your goal is to put maximum number of fruits in each basket.
    The only restriction is that each basket can have only one type of fruit.

    You can start with any tree, but once you have started you can’t skip a tree.
    You will pick one fruit from each tree until you cannot, i.e.,
    you will stop when you have to pick from a third fruit type.

    Write a function to return the maximum number of fruits in both the baskets.

    Example 1:
    Input: Fruit=['A', 'B', 'C', 'A', 'C']
    Output: 3
    Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

    {
     'C': 2
     'A': 1
    }

    ['A', 'B', 'C', 'A', 'C']


    Example 2:
    Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
    Output: 5
    Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
    This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

    {
    'C': 2
    'B': 3
    }

            *
    ['A', 'B', 'C', 'B', 'B', 'C']
                                ^

    {
    'C': 1
    'A': 2
    }

                        *
    ['A' , 'C' , 'B' , 'A' , 'A' , 'C' , 'B' , 'B' , 'C' , 'A']
                                        ^
    {2,3}
                                *
    ['3' , '3' , '3' , '1' , '2' , '1' , '1' , '2' , '3' , '3' , '4']
                                                    ^
"""


def fruits_into_basket(fruits) -> int:
    back = 0
    largest = 0
    basket = set()

    for i, fruit in enumerate(fruits):
        if len(basket) < 2 or fruit in basket:
            basket.add(fruit)
        else:
            if fruit not in basket:
                basket.remove(fruits[back])
                basket.add(fruit)
                while fruits[back] not in basket:
                    back += 1
        largest = max(largest, i - back)
    return largest + 1


def fruits_into_basket2(tree) -> int:
    fruit1 = fruit2 = None
    counter1 = counter2 = 0
    result = 0

    for fruit in tree:
        if fruit != fruit2:
            if fruit != fruit1:
                counter1 = counter2
            fruit1, fruit2 = fruit2, fruit
            counter2 = 0
        counter1 += 1
        counter2 += 1

        if counter1 > result:
            result = counter1

    return result


def fruits_into_basket1(fruits) -> int:
    back = 0
    largest = 0
    basket = {}

    for i, fruit in enumerate(fruits):
        if fruit not in basket:
            basket[fruit] = 0
        basket[fruit] += 1

        while len(basket) > 2:
            if fruits[back] in basket:
                basket[fruits[back]] -= 1
                if basket[fruits[back]] == 0:
                    basket.pop(fruits[back])
            back += 1
        largest = max(i - back, largest)

    return largest + 1


if __name__ == '__main__':
    print(fruits_into_basket1(['A', 'B', 'C', 'A', 'C']))  # 3
    print(fruits_into_basket1(['A', 'B', 'C', 'B', 'B', 'C']))  # 5
    print(fruits_into_basket1(['A', 'C', 'B', 'A', 'A', 'C', 'B', 'B', 'C', 'A']))  # 4
    print(fruits_into_basket1(['3', '3', '3', '1', '2', '1', '1', '2', '3', '3', '4']))  # 5
    print()
    print(fruits_into_basket(['A', 'B', 'C', 'A', 'C']))  # 3
    print(fruits_into_basket(['A', 'B', 'C', 'B', 'B', 'C']))  # 5
    print(fruits_into_basket(['A', 'C', 'B', 'A', 'A', 'C', 'B', 'B', 'C', 'A']))  # 4
    print(fruits_into_basket(['3', '3', '3', '1', '2', '1', '1', '2', '3', '3', '4']))  # 5
    print()
    print(fruits_into_basket2(['A', 'B', 'C', 'A', 'C']))  # 3
    print(fruits_into_basket2(['A', 'B', 'C', 'B', 'B', 'C']))  # 5
    print(fruits_into_basket2(['A', 'C', 'B', 'A', 'A', 'C', 'B', 'B', 'C', 'A']))  # 4
    print(fruits_into_basket2(['3', '3', '3', '1', '2', '1', '1', '2', '3', '3', '4']))  # 5
