# https://projecteuler.net/problem=20
import math
import pytest

def factorial_digit_sum(num):
    factorial = math.factorial(num)
    total = 0

    for i in str(factorial):
        total += int(i)
    return total

def test_factorial_digit_sum():
    result = factorial_digit_sum(10)
    expect = 27
    assert result == expect

def test_factorial_digit_sum_1():
    result = factorial_digit_sum(5)
    expect = 3
    assert result == expect


if __name__ == "__main__":
    print(factorial_digit_sum(100))