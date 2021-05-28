# https://projecteuler.net/problem=3
import math

def find_prime_factors(n):
    prime_list = []
    for num in range(2, n + 1):
        if (n % num == 0) and (__check_prime(num)):
            prime_list.append(num)
    return prime_list


def __check_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def test_find_prime_factors():
    result = find_prime_factors(13195)
    expect = [5, 7, 13, 29]
    assert result == expect


if __name__ == "__main__":
    n = 13195
    prime_factors = find_prime_factors(n)
    max_prime_factor = max(prime_factors)
    print(f"prime factors of {n}: {prime_factors}.")
    print(f"Max Prime factor is {max_prime_factor}.")