#!/usr/bin/env python3

import fileinput
import itertools
import re
from collections.abc import Iterable


def part1(input: Iterable[str]) -> int:
    re_front = r"^.*?(\d)"
    re_back = r".*(\d).*$"

    res = [re.compile(r) for r in (re_front, re_back)]

    s = sum(
        int("".join(m.group(1) for r in res if (m := r.match(line)))) for line in input
    )

    return s


def part2(input: Iterable[str]) -> int:
    number_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    numbers_str = r"|".join(number_map.keys())

    number_r = rf"\d|{numbers_str}"

    re_front = rf"^.*?({number_r})"
    re_back = rf".*({number_r}).*$"

    res = [re.compile(r) for r in (re_front, re_back)]

    s = sum(
        int(
            "".join(
                number_map.get(g := m.group(1), g) for r in res if (m := r.match(line))
            )
        )
        for line in input
    )

    return s


def main() -> None:
    first, second = itertools.tee(fileinput.input())

    print("part1:", part1(first))

    print("part2:", part2(second))


if __name__ == "__main__":
    main()
