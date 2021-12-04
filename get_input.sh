#!/usr/bin/env bash

set -e

cd "$(dirname "$(realpath "${BASH_SOURCE[0]}")")"
cd "$(git rev-parse --show-toplevel)"

default_day="$(date "+%d")"
default_year="2021"

day_padded="$(printf "%02d\n" "${1:-$default_day}")"
year="${2:-$default_year}"

day="$(echo $day_padded | sed 's/^0*//')"

puzzle_folder="$PWD/$year/Day$day_padded"
puzzle_file="$puzzle_folder/input.txt"
puzzle_url="https://adventofcode.com/${year}/day/${day}/input"

echo "Downloading input for $year day $day to $puzzle_file"
mkdir -p "$puzzle_folder"
curl "${puzzle_url}" -H "cookie: session=${AOC_SESSION_COOKIE}" -o "${puzzle_file}" 2>/dev/null



# https://github.com/MikeD89/advent-of-code-typescript/blob/main/login.ts
