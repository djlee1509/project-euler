# https://projecteuler.net/problem=2

def fibonacci_seq(limit):
    i, j = 1, 2
    next_seq = 0

    while j < limit:
        if j % 2 == 0:
            next_seq += j
        i, j = j, i + j
    return next_seq


if __name__ == "__main__":
    limit = 4000000
    print(fibonacci_seq(limit))