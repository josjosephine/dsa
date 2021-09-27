# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    total = 1
    start = 1
    summands.append(start)

    while n - total > summands[-1]:
        summands.append(summands[-1] + 1)
        total += summands[-1]
    summands[-1] += (n - total)

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
