# https://projecteuler.net/problem=6


def sum_of_sq(n):
    sq_list = [(x ** 2) for x in range(1, n+1)]
    return sum(sq_list)

def sq_of_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
        i += 1
    square_of_sum = sum ** 2
    return square_of_sum

def diff(n):
    diff = sq_of_sum(n) - sum_of_sq(n)
    return diff

def test_sum_of_sq():
    result = sum_of_sq(10)
    expect = 385
    assert result == expect

def test_sq_of_sum():
    result = sq_of_sum(10)
    expect = 3025
    assert result == expect

def test_diff():
    result = diff(10)
    expect = 2640
    assert result == expect

if __name__ == "__main__":
    x, y = 10, 20
    print(diff(x), diff(y))