# https://projecteuler.net/problem=15

import math

def factorial(num):
    return math.factorial(num)


def routes_number(x):
    num = factorial(x * 2)
    denom = factorial(x) ** 2

    result = num // denom
    return result


def test_routes_number():
    result = routes_number(2)
    expect = 6
    assert result == expect
    

if __name__ == "__main__":
    print(routes_number(1))