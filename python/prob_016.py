# https://projecteuler.net/problem=16

def get_power_digit_sum(num):
    total = 0

    for i in str(num):
        total += int(i)
    return total


def test_get_power_digit_sum():
    result = get_power_digit_sum(2 ** 5)
    expect = 5
    assert result == expect


if __name__ == "__main__":
    num = 2 ** 1000
    print(get_power_digit_sum(num))