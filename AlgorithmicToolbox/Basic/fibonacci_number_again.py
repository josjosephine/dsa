# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    arr = [0, 1]
    previous = 0
    current = 1

    for i in range(n - 1):
        previous1 = previous
        previous = current % m
        current = (previous1 + current) % m
        arr.append(current)

        if current == 1 and previous == 0:
            index = (n % (i + 1))
            return arr[index]

    return current


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
