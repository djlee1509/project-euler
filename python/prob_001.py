# https://projecteuler.net/problem=1

def sum_of_multiples(max):
    sum = 0
    for i in range(max):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


if __name__ == "__main__":
    print("Total: {}".format(sum_of_multiples(1000)))