#!/usr/bin/env python3

from pprint import pformat, pprint  # noqa: F401
import math  # noqa: F401


def read_file(file_path):

    with open(file_path, "r") as f:
        return f.read().splitlines()


def get_input():

    file_path = "./"
    file_name = "input.txt"
    file_name = "input_test.txt"

    return read_file(file_path + file_name)


def parse_input(line):

    return tuple(int(digit) for digit in line)


def b_not(b_num):
    return "".join("1" if digit == "0" else "0" for digit in b_num)


def get_answer_1(input):

    digit_counts_0 = [0] * len(input[0])
    digit_counts_1 = digit_counts_0.copy()

    for number in input:

        digit_counts_1 = [sum(pair) for pair in zip(number, digit_counts_1)]

        number_inverted = tuple((digit - 1) * -1 for digit in number)
        digit_counts_0 = [sum(pair) for pair in zip(number_inverted, digit_counts_0)]

    print(f"0's: {digit_counts_0}")
    print(f"1's: {digit_counts_1}")

    most_common_digit = "".join(
        [
            str(int(counts[0] < counts[1]))
            for counts in zip(digit_counts_0, digit_counts_1)
        ]
    )

    # print("".join(str(digit) for digit in most_common_digit))

    print(most_common_digit)
    print(b_not(most_common_digit))
    # print(int(most_common_digit, 2))

    gamma_rate = int(most_common_digit, 2)
    epsilon_rate = int(b_not(most_common_digit), 2)

    print(gamma_rate)
    print(epsilon_rate)

    return gamma_rate * epsilon_rate


def main():

    input = [parse_input(line) for line in get_input()]

    answer_1 = get_answer_1(input)
    print(f"The first answer is {answer_1}")

    # answer_2 = determine_position_2(steps_1)
    # print(f"The second answer is {answer_2}")


if __name__ == "__main__":
    main()
