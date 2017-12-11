#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 David Haller <davidhaller@mailbox.org>
#
# roll is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# roll is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

"""
Simulates rolling a die like those used in
Dungeons and Dragons, the Pen and Paper role playing game.
"""

from os import fstat
from stat import S_ISREG, S_ISFIFO
from sys import stdin

import random
import re

random.seed()
PATTERN = re.compile(r"^(\d+[\*])?(\d+)?d(\d+)([\+|-]\d+)?$")


def parse(statement: str) -> tuple:
    """
    Extracts information from a roll statement.

    @param statement: One single roll statement.
    @return: A tuple containing how often the roll should be performed,
             how many dice should be rolled each time,
             which die should be rolled and which bonus should be added.
    @raise ValueError: If the statement is malformed or invalid.
    """
    check = PATTERN.match(statement)

    if check is None:
        raise ValueError("Malformed")

    data = check.groups()

    if data[0] is None:
        times = 1
    else:
        times = int(data[0].replace("*", ""))

    if data[1] is None:
        amount = 1
    else:
        amount = int(data[1])

    die = int(data[2])

    if times <= 0 or amount <= 0 or die <= 1:
        raise ValueError("Invalid")

    if data[3] is None:
        bonus = 0
    else:
        bonus = int(data[3])

    return times, amount, die, bonus


def roll(amount: int, die: int):
    """
    Rolls the dice using a generator.

    @param amount: How many dice should be rolled.
    @param die: Which die should be rolled.
    @return: A generator with the result of each roll.
    """

    for _ in range(0, amount):
        yield random.randint(1, die)


def execute(command: str):
    """
    Executes ";"-separated roll statements and returns
    the results in a user-readable form.

    @param command: String containing one or multiple roll statements.
    @return: A generator of user-readable strings containing
             all dice roll results, the bonus and
             the end result (one string per roll).
    """

    for part in command.split(";"):
        statement = part.replace(" ", "")

        if statement == "":
            continue
        elif statement == "exit" or statement == "quit":
            exit()

        try:
            times, amount, die, bonus = parse(statement)

            if bonus < 0:
                string = "{0} - {1} = {2}"
            else:
                string = "{0} + {1} = {2}"

            for _ in range(0, times):
                result = list(roll(amount, die))
                yield string.format(result, abs(bonus), sum(result) + bonus)

        except ValueError as error:
            string = "{0}: {1}"
            yield string.format(error.args[0], part)


if __name__ == "__main__":
    MODE = fstat(stdin.fileno()).st_mode
    if S_ISREG(MODE) or S_ISFIFO(MODE):
        PROMPT = ""
    else:
        PROMPT = "roll> "

    try:
        while True:
            for line in execute(input(PROMPT)):
                print(line)

    except (KeyboardInterrupt, EOFError):
        exit()
