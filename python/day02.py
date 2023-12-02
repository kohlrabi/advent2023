#!/usr/bin/env python3

import fileinput
import functools
import itertools
import re
from collections import defaultdict
from collections.abc import Iterable

re_game = re.compile(r"Game (\d+):")

re_cube = re.compile(r"\s*?(\d+) ([a-z])")


def part1(input: Iterable[str]) -> int:
    max_cubes = {
        "r": 12,
        "g": 13,
        "b": 14,
    }

    s = 0

    for line in input:
        match = re_game.match(line)
        if match:
            game_number = int(match.group(1))
        else:
            raise ValueError("Invalid game number")

        games = line.split(":")[1].split(";")

        for game in games:
            cubes = game.split(",")
            invalid = False
            for cube in cubes:
                match = re_cube.match(cube)
                if match:
                    num, color = match.groups()
                    if max_cubes[color] < int(num):
                        invalid = True
                        break
            if invalid:
                break
        else:
            s += game_number

    return s


def part2(input: Iterable[str]) -> int:
    s = 0

    for line in input:
        match = re_game.match(line)

        min_cubes: dict[str, int] = defaultdict(int)

        games = line.split(":")[1].split(";")

        for game in games:
            cubes = game.split(",")
            for cube in cubes:
                match = re_cube.match(cube)
                if match:
                    num, color = match.groups()
                    min_cubes[color] = max(min_cubes[color], int(num))

        s += functools.reduce(lambda x, y: x * y, min_cubes.values())

    return s


def main() -> None:
    first, second = itertools.tee(fileinput.input())

    print("part1:", part1(first))

    print("part2:", part2(second))


if __name__ == "__main__":
    main()
