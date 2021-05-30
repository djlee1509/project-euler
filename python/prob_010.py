# https://projecteuler.net/problem=10
import math

def __check_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def get_prime_list_sum(n):
    """Returns the sum of prime numbers below n"""
    prime_list = [i for i in range(1, n) if __check_prime(i) and i != 1]
    return sum(prime_list)


def test_get_prime_list_sum():
    result = get_prime_list_sum(10)
    expect = 17
    assert result == expect


if __name__ == "__main__":
    print(get_prime_list_sum(1000))