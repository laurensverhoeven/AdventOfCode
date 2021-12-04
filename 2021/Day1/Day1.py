#!/usr/bin/env python3

from pprint import pformat, pprint  # noqa: F401
import math


def ReadFile(FilePath):

    with open(FilePath, "r") as f:
        Lines = f.read().splitlines()

    return Lines


def CalculateRequiredFuel(DeviceMass):

    Fuel = math.floor(DeviceMass / 3) - 2

    return Fuel


def main():

    FilePath = "./"
    FileName = "input.txt"
    FileName = "input_test.txt"

    InputFile = FilePath + FileName

    Lines = ReadFile(InputFile)

    print([int(Line) for Line in Lines])


if __name__ == "__main__":
    main()
