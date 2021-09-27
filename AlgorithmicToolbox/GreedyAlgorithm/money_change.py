# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    cnt = int(money / 10)
    remain = money % 10
    cnt += int(remain / 5)

    remain = remain % 5
    cnt += remain

    return cnt


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
