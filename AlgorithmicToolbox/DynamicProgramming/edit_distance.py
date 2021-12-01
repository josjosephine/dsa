# python3


def edit_distance(first_string, second_string):
    dist = [[0 for col in range(len(first_string) + 1)] for row in range(len(second_string) + 1)]
    for i in range(len(first_string) + 1):
        dist[0][i] = i
    for i in range(len(second_string) + 1):
        dist[i][0] = i
    for m in range(1, len(first_string) + 1):
        for n in range(1, len(second_string) + 1):
            d1 = dist[n][m-1] + 1
            d2 = dist[n-1][m] + 1
            d3 = dist[n-1][m-1]
            d4 = dist[n-1][m-1] + 1
            if first_string[m-1] == second_string[n-1]:
                dist[n][m] = min(d1, d2, d3)
            else:
                dist[n][m] = min(d1, d2, d4)
    return dist[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
