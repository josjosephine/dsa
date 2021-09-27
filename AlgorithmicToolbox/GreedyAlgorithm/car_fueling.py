# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    numrefil, currefill, limit = 0, 0, m

    while limit < d:
        if currefill >= len(stops) or stops[currefill] > limit:
            return -1

        while currefill < len(stops) - 1 and stops[currefill + 1] <= limit:
            currefill += 1
        numrefil += 1
        limit = stops[currefill] + m
        currefill += 1

    return numrefil


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
