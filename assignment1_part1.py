#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 1 assignment1_part1"""

class ListDivideException(Exception):
    pass


def listDivide(numbers, divide=2):
    divisors = 0
    for number in numbers:
        if number % divide == 0:
            divisors += 1

    return divisors


def testListDivide():
    if listDivide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException()
    if listDivide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException()
    if listDivide([30, 54, 63, 98, 100], divide=10) != 2:
        raise ListDivideException()
    if listDivide([]) != 0:
        raise ListDivideException()
    if listDivide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException()


testListDivide()
