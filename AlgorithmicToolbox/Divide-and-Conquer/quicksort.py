# python3

from random import randint


def partition3(array, left, right):
    x = array[left]
    y = left

    for i in range(left + 1, right + 1):
        if array[i] <= x:
            y += 1
            array[i], array[y] = array[y], array[i]
    array[left], array[y] = array[y], array[left]

    z = y

    while x == array[z] and z > -1:
        z -= 1
    return z + 1, y


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
