"""
    Interviewer drew out the illustration exactly as shown below
    <----- 0-----0--0----
    ----1-----1--------1->

    On a 2 ways lane, there are cars driving west-bound (0) and cars driving east-bound (1),
    write a function that returns the amount of times that the cars will pass by each other.

    The above illustration was turned into an array [1,0,1,0,0,1] as input and should return 5
    (first "1" will drive by 3 "0", second will drive by 2, and third will drive by 0).
"""


def num_cross(cars):
    total = 0
    my_car = 0
    for i in reversed(cars):
        if i == 0:
            my_car += 1
        else:
            total += my_car
    return total


if __name__ == '__main__':
    print(num_cross([1, 1, 0, 0]))  # 4
    print(num_cross([1, 0]))  # 1
    print(num_cross([0, 1]))  # 0
    print(num_cross([1, 0, 1, 0, 0, 1]))  # 5
