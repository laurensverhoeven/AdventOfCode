#!/usr/bin/env python3

from pprint import pformat, pprint  # noqa: F401
import math  # noqa: F401


def ReadFile(file_path):

    with open(file_path, "r") as f:
        return f.read().splitlines()


def get_input():

    FilePath = "./"
    FileName = "input.txt"
    # FileName = "input_test.txt"

    InputFile = FilePath + FileName

    return [int(line) for line in ReadFile(InputFile)]


def determine_increasing_count(depth_measurements):

    increasing_count = 0

    last_measurement = depth_measurements[0]
    for depth_measurement in depth_measurements[1:]:
        if depth_measurement > last_measurement:
            increasing_count += 1
        last_measurement = depth_measurement

    return increasing_count


def determine_average_increasing_count(depth_measurements):

    increasing_count = 0

    sums = []
    sums.append(sum(depth_measurements[0:3]))
    sums.append(sum(depth_measurements[1:4]))

    i = 2
    measurements_count = len(depth_measurements)
    while i < measurements_count:
        if sums[1] > sums.pop(0):
            increasing_count += 1
        sums.append(sum(depth_measurements[i - 2 : i + 1]))
        i += 1

    return increasing_count


def main():

    depth_measurements = get_input()

    # answer_1 = determine_increasing_count(depth_measurements)
    # print(f"The first answer is {answer_1}")

    answer_2 = determine_average_increasing_count(depth_measurements)
    print(f"The second answer is {answer_2}")


if __name__ == "__main__":
    main()
