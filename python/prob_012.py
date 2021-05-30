# https://projecteuler.net/problem=12

def get_nth_tri_num(n):
    """Returns the nth triangle number."""
    i = 1
    sum = 0

    while i <= n:
        sum += i
        i += 1
    return sum


def get_number_of_factors(sum):
    """Returns the number of factors of integer."""
    factors = [i for i in range(1, sum+1) if sum%i == 0]
    return len(factors)


def main(lim):
    """Returns the first triangle number to have over the limit (number of divisors)."""
    order = 1
    no_factors = 0

    while no_factors <= lim:
        tri_num = get_nth_tri_num(order)
        no_factors = get_number_of_factors(tri_num)
        order += 1
    return tri_num


def test_main():
    result = main(5)
    expect = 28
    assert result == expect

if __name__ == "__main__":
    print(main(5))