# python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    n = (len(dataset) + 1) // 2
    ma = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        ma[i][i] = int(dataset[2*i])
    mi = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        mi[i][i] = int(dataset[2*i])
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            ma[i][j], mi[i][j] = MinAndMax(i, j, ma, mi, dataset)
    return ma[0][-1]

    return 0

def MinAndMax(i, j, ma, mi, dataset):
    tmin = float("inf")
    tmax = -float("inf")
    for k in range(i, j):
        a = evalt(ma[i][k], ma[k+1][j], dataset[2*k+1])
        b = evalt(ma[i][k], mi[k+1][j], dataset[2*k+1])
        c = evalt(mi[i][k], ma[k+1][j], dataset[2*k+1])
        d = evalt(mi[i][k], mi[k+1][j], dataset[2*k+1])
        tmin = min(tmin, a, b, c, d)
        tmax = max(tmax, a, b, c, d)
    return tmax, tmin


if __name__ == "__main__":
    print(find_maximum_value(input()))
