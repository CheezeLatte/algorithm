# https://www.acmicpc.net/problem/2178
from collections import deque

n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int, input())))

depth = 0


def bfs(x, y):
    global depth

    answer = [n - 1, m - 1]
    cur_location = []
    visited = [[0] * m for _ in range(n)]

    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # deque 생성
    queue = deque()
    queue.append([y, x])

    while cur_location != answer:
        q_length = len(queue)
        for _ in range(q_length):
            cur_location = queue.popleft()
            if cur_location == answer:
                break

            y, x = cur_location[0], cur_location[1]
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue

                if board[ny][nx] == 0:
                    continue

                if board[ny][nx] == 1 and visited[y][x] != True:
                    queue.append([ny, nx])

            visited[y][x] = True
        depth += 1


bfs(0, 0)
print(depth)

#입력이 큰 상관이 없을 것 같을때는 sys 안 써도 할만하다
#visited 같이 캐싱용 배열을 쓸때는 2차원 배열을 써서 인덱스를 바로 확인할 수 있도록 하자 in 이런거 쓰면 너무 느리다