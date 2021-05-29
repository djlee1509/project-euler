# https://projecteuler.net/problem=5
from math import gcd

def smallest_multiple(n):
    nums = [x for x in range(1, n+1)]
    lcm = 1

    for k in nums:
        lcm = lcm * k // gcd(lcm, k)
    return lcm


if __name__ == "__main__":
    print(smallest_multiple(20))
