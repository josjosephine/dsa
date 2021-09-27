# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def is_great_or_equal(a, b):
    if a + b > b + a:
        return True
    else:
        return False


def largest_number(numbers):
    res = ""
    while len(numbers) > 0:
        max_digit = '0'
        for x in numbers:
            if is_great_or_equal(x, max_digit):
                max_digit = x
        res += max_digit
        numbers.remove(max_digit)
    return res


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
