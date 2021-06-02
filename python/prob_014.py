# https://projecteuler.net/problem=14
import pytest

def next_seq(n):
    if n % 2 == 0:
        n = n/2
    else:
        n = (3 * n) + 1
    return n


def get_collatz_seq(n):
    seq = [n]
    next_num = n
    
    if next_num <= 0:
        print("Error: It has to be positive integer.")
    
    while next_num:
        next_num = next_seq(next_num)
        seq.append(int(next_num))

        if next_num == 1:
            break

    return seq


def test_get_collatz_seq():
    result = get_collatz_seq(13)
    expect = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    assert result == expect

def test_get_collatz_seq_2():
    result = get_collatz_seq(1)
    expect = [1, 4, 2, 1]
    assert result == expect


def test_next_seq():
    result = next_seq(19)
    expect = 58
    assert result == expect


def main(max_limit):
    count_chain = [len(get_collatz_seq(i)) for i in range(1, max_limit)]
    longest_chain_start_num = count_chain.index(max(count_chain)) + 1
    return longest_chain_start_num
    

if __name__ == "__main__":
    print(main(10))