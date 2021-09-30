# python3
from sys import stdin
# from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def BinarySearch(a, x, direction):
    if len(a) == 0:
        return -1
    left, right = 0, len(a)-1
    while left <= right:
        ave = (left + right) // 2
        if x == a[ave]:
            while left - 1 < ave <= right:
                if x == a[ave]:
                    if direction:
                        ave += 1
                    else:
                        ave -= 1
                else:
                    break
            if direction:
                return ave
            else:
                return ave + 1
        elif x < a[ave]:
            right = ave - 1
        else:
            left = ave + 1
    return right + 1


def points_cover(starts, ends, points):
    cnt = [0] * len(points)
    starts = sorted(starts)
    ends = sorted(ends)

    for i in range(len(points)):
        st = BinarySearch(starts, points[i], 1)
        end = BinarySearch(ends, points[i], 0)

        cnt[i] = st - end
    return cnt


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
