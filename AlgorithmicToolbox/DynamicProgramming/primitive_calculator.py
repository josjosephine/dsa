# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    cnt = [0] * (n + 1)

    cnt[1] = 1
    for i in range(2, n + 1):
        indices = [i - 1]
        if i % 2 == 0:
            indices.append(i // 2)
        if i % 3 == 0:
            indices.append(i // 3)

        mins = min([cnt[x] for x in indices])

        cnt[i] = mins + 1

    ptr = n
    optimal_seq = [ptr]
    while ptr != 1:

        candidates = [ptr - 1]
        if ptr % 2 == 0:
            candidates.append(ptr // 2)
        if ptr % 3 == 0:
            candidates.append(ptr // 3)

        ptr = min(
            [(c, cnt[c]) for c in candidates],
            key=lambda x: x[1]
        )[0]
        optimal_seq.append(ptr)

    return reversed(optimal_seq)


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = list(compute_operations(input_n))
    print(len(output_sequence) - 1)
    print(*output_sequence)
