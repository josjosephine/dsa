# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    m = len(weights)
    value = [[0 for col in range(capacity + 1)] for row in range(m + 1)]
    for i in range(1, m + 1):
        for cp in range(1, capacity + 1):
            value[i][cp] = value[i-1][cp]
            if weights[i-1] <= cp:
                val = value[i-1][cp - weights[i-1]] + weights[i - 1]
                if val > value[i][cp]:
                    value[i][cp] = val
#    print(value)
    return value[-1][-1]


if __name__ == '__main__':
    input_capacity, m, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == m

    print(maximum_gold(input_capacity, input_weights))
