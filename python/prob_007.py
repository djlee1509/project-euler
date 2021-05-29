# https://projecteuler.net/problem=7

import math

def __check_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def get_nth_prime(n):
    i = 1
    prime_list = []

    while len(prime_list) < n:
        if __check_prime(i):
            if i != 1:
                prime_list.append(i)
        i += 1

    return prime_list[n-1]


def test_get_nth_prime():
    result = get_nth_prime(6)
    expect = 13
    assert result == expect


if __name__ == "__main__":
    print(get_nth_prime(10001))