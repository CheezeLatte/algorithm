from collections import deque

n = int(input())

board = []

shark_size, fishes_for_bulk_up, seconds = 2, 2, 0

call_help = False

initial_y, initial_x = 0, 0

for i in range(n):
    board.append(list(map(int, input().split())))
    for k in range(n):
        if board[-1][k] == 9:
            initial_y, initial_x = i, k
            board[-1][k] = 0


def bfs(start_y, start_x):
    match = []

    queue = deque()

    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for k in range(n):
            if board[i][k] < shark_size:
                visited[i][k] = board[i][k]

    queue.append([start_y, start_x])

    depth = 0

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while queue:
        q_length = len(queue)

        if len(match) > 0:
            break

        for _ in range(q_length):
            cur_location = queue.popleft()

            y, x = cur_location[0], cur_location[1]

            if type(visited[y][x]) != bool and 0 < visited[y][x] < shark_size:
                match.append([y, x])
                visited[y][x] = True

            # for i in visited:
            #     print(i)
            #
            # print('\n')

            for i in range(4):

                ny = y + dy[i]
                nx = x + dx[i]

                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue

                if board[ny][nx] > shark_size:
                    continue

                if 0 <= board[ny][nx] <= shark_size and visited[y][x] != True:
                    queue.append([ny, nx])

            visited[y][x] = True
        depth += 1

    return [match, depth]


def choose_shark(data):
    if len(data[0]) == 0:
        return

    if len(data[0]) > 1:
        lowest_y = min([x[0] for x in data[0]])
        data[0] = list(filter(lambda arr: arr[0] == lowest_y, data[0]))

    if len(data[0]) > 1:
        lowest_x = min([x[1] for x in data[0]])
        data[0] = list(filter(lambda arr: arr[1] == lowest_x, data[0]))

    return [data[0][0], data[1]]


def lets_eat(data):
    global seconds, fishes_for_bulk_up, shark_size, call_help, initial_y, initial_x
    if data is None:
        call_help = True
        return

    board[data[0][0]][data[0][1]] = 0
    initial_y, initial_x = data[0][0], data[0][1]
    # for i in board:
    #     print(i)
    # print(initial_y, initial_x, data[1])
    # print('\n')
    seconds += data[1] - 1
    fishes_for_bulk_up -= 1
    if fishes_for_bulk_up == 0:
        shark_size += 1
        fishes_for_bulk_up = shark_size


while call_help is False:
    lets_eat(choose_shark(bfs(initial_y, initial_x)))

print(seconds)
