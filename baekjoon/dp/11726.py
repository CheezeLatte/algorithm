# https://www.acmicpc.net/problem/11726

d = [0] * 1001


def rec(n):
    if n == 1: return 1
    if n == 2: return 2
    if d[n] != 0:
        return d[n]
    else:
        d[n] = rec(n - 1) + rec(n - 2)
    return (rec(n - 1) + rec(n - 2)) % 10007


print(rec(int(input())))
