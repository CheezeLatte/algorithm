# https://www.acmicpc.net/problem/2251
import sys, copy
from collections import deque

input = sys.stdin.readline

cups = list(map(int, input().split()))

visited = [[0] * 300 for _ in range(300)]
queue = deque([[0, 0]])
answers = []


# 비울 수 있는 조건?
# 1. 받는 컵이 가득 찬다
# 2. 비우는 컵이 빈다

# 전체 부워버리는 수는 딱 6종류다. 6종류를 다 해볼 수 있도록 짜자
# bfs의 경우 원본은 건들지 않는다.

def pour(x, y):
    if visited[x][y] is not True:
        queue.append([x, y])


def bfs():
    while queue:
        case = queue.popleft()
        a, b = case[0], case[1]

        c = cups[2] - a - b

        if a == 0 and  c not in answers:
            answers.append(c)

        # a -> b
        if a > 0 and cups[1] - b > 0:
            if cups[1] - b >= a:  # b가 더 클때
                pour(0, b + a)
            else:
                pour(a + b - cups[1], cups[1])  # a가 더 클때

        # a -> c
        if a > 0 and cups[2] - c > 0:
            if cups[2] - c >= a:
                pour(0, cups[2] - (a + c))
            # else:
            #     pour(a + c - cups[2], 0)

        # b -> a
        if b > 0 and cups[0] - a > 0:
            if cups[0] - a >= b:
                pour(a + b, 0)
            else:
                pour(cups[0], b - (cups[0] - a))

        # b -> c
        if b > 0 and cups[2] - c > 0:
            if cups[2] - c >= b:
                pour(a, 0)
            # else:
            #     pour(0, 0)

        # c -> a
        if c > 0 and cups[0] - a > 0:
            if cups[0] - a >= c:
                pour(a + c, b)
            else:
                pour(cups[0], b)

        # c -> b
        if c > 0 and cups[1] - b > 0:
            if cups[1] - b >= c:
                pour(a, b + c)
            else:
                pour(a, cups[1])

        visited[a][b] = True


bfs()
for i in sorted(answers):
    print(i, end=' ')
