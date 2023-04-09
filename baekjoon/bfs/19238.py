# https://www.acmicpc.net/problem/19238
from collections import deque

n, p, fuel = map(int, input().split())
stop = False
board = []
passengers = []

for i in range(n):
    board.append(list(map(int, input().split())))

initial_y, initial_x = map(int, input().split())

for i in range(p):
    passengers.append(list(map(int, input().split())))


def bfs(init_y, init_x, target_y, target_x):
    global fuel
    queue = deque()

    answer = [target_y - 1, target_x - 1]

    visited = [[0] * n for _ in range(n + 1)]

    cur_location = []

    queue.append([init_y - 1, init_x - 1])

    depth = 0

    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while cur_location != answer:
        q_length = len(queue)
        if q_length == 0:
            fuel = -1
            break
        for _ in range(q_length):
            cur_location = queue.popleft()
            if cur_location == answer:
                break

            y, x = cur_location[0], cur_location[1]

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue

                if board[ny][nx] == 1:
                    continue

                if board[ny][nx] == 0 and visited[y][x] != True:
                    queue.append([ny, nx])

            visited[y][x] = True
        depth += 1

    return depth


def multi_bfs(init_y, init_x):
    global fuel
    queue = deque()

    match = []

    visited = [[0] * n for _ in range(n + 1)]

    for passenger in passengers:
        visited[passenger[0] - 1][passenger[1] - 1] = passenger

    queue.append([init_y - 1, init_x - 1])

    depth = 0

    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while queue:
        q_length = len(queue)

        if len(match) > 0 or len(passengers) == len(match):
            break

        if fuel - depth <= 0:
            fuel = -1
            break

        for _ in range(q_length):
            cur_location = queue.popleft()

            y, x = cur_location[0], cur_location[1]

            if type(visited[y][x]) == list:
                visited[y][x].append(depth + 1)
                match.append(visited[y][x])
                visited[y][x] = 0

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue

                if board[ny][nx] == 1:
                    continue

                if board[ny][nx] == 0 and visited[y][x] != True:
                    queue.append([ny, nx])

            visited[y][x] = True
        depth += 1

    return match


def choose_passenger():
    nearest_candidates = multi_bfs(initial_y, initial_x)

    if len(nearest_candidates) == 0:
        return

    if len(nearest_candidates) > 1:
        lowest_y = min([x[0] for x in nearest_candidates])
        nearest_candidates = list(filter(lambda arr: arr[0] == lowest_y, nearest_candidates))

    if len(nearest_candidates) > 1:
        lowest_x = min([x[1] for x in nearest_candidates])
        nearest_candidates = list(filter(lambda arr: arr[1] == lowest_x, nearest_candidates))

    return nearest_candidates[0]


def drive(nearest_passenger):
    global initial_y, initial_x, fuel, stop

    if nearest_passenger is None:
        fuel = -1
        stop = True
        return
    
    initial_y, initial_x = nearest_passenger[0], nearest_passenger[1]
    fuel -= nearest_passenger[4] - 1
    if fuel <= 0:
        fuel = -1
        stop = True

    shortest_dest = bfs(initial_y, initial_x, nearest_passenger[2], nearest_passenger[3])

    fuel -= shortest_dest - 1

    if fuel < 0:
        fuel = -1
        stop = True
    else:
        fuel += (shortest_dest - 1) * 2

    initial_y, initial_x = nearest_passenger[2], nearest_passenger[3]

    passengers.remove(nearest_passenger)

    for passenger in passengers:
        try:
            if passenger[4]:
                passenger.pop()
        except:
            continue


for _ in range(len(passengers)):
    if stop:
        break
    drive(choose_passenger())

print(fuel)
