# https://projecteuler.net/problem=4

def check_palindrome(num):
    return str(num) == str(num)[::-1]

def max_palindrome(max, min):
    palindrome_list = []
    for x in range(max, min, -1):
        for y in range(max, min, -1):
            if check_palindrome(x * y):
                palindrome_list.append(x * y)
    return palindrome_list


if __name__ == "__main__":
    pal = max_palindrome(999, 99)
    print(max(pal))