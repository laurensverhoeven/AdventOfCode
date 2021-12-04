#!/usr/bin/env python3

from pprint import pformat, pprint  # noqa: F401
import math  # noqa: F401


def read_file(file_path):

    with open(file_path, "r") as f:
        return f.read().splitlines()


def get_input():

    file_path = "./"
    file_name = "input.txt"
    # file_name = "input_test.txt"

    return read_file(file_path + file_name)


def parse_direction_1(line):

    step = line.partition(" ")

    direction = str(step[0])
    distance = int(step[2])

    direction_options = {
        "forward": (1, 0),
        "down": (0, 1),
        "up": (0, -1),
    }

    return tuple(distance * unit for unit in direction_options[direction])


def determine_position_1(steps):
    position = (0, 0)
    for step in steps:

        position = tuple(map(sum, zip(position, step)))
        # print(f"Position is {position}")

    return position[0] * position[1]


def determine_position_2(steps):
    position = (0, 0)
    aim = 0
    for forward_change, aim_change in steps:

        aim += aim_change
        depth_change = forward_change * aim
        position = (position[0] + forward_change, position[1] + depth_change)
        print(f"forward_change: {forward_change} , aim_change: {aim_change}")
        print(f"Position is {position}, aim is {aim}")

    return position[0] * position[1]


def main():

    steps_1 = [parse_direction_1(line) for line in get_input()]

    answer_1 = determine_position_1(steps_1)
    print(f"The first answer is {answer_1}")

    answer_2 = determine_position_2(steps_1)
    print(f"The second answer is {answer_2}")


if __name__ == "__main__":
    main()
