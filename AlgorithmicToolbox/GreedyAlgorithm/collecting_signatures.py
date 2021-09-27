# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    points = []
    sortedsegs = sorted(segments, key=lambda t: t[1])

    point = sortedsegs[0].end
    points.append(point)
    for s in sortedsegs:
        if s.start > point:
            points.append(s.end)
            point = s.end
    return points


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
