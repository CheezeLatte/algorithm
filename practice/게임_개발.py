map_size = list(map(int, input().split()))

player = list(map(int, input().split()))

game_map = []
visited = []

for i in range(map_size[1]):
    game_map.append(list(map(int, input().split())))


def movable():
    try:
        if player[2] == 0 and game_map[player[1] - 1][player[0]] == 0 and [player[0], player[1] - 1] not in visited and (player[1] - 1) >= 0:
            return True
        elif player[2] == 1 and game_map[player[1]][player[0] + 1] == 0 and [player[0] + 1, player[1]] not in visited and (player[0] + 1) >= 0:
            return True
        elif player[2] == 2 and game_map[player[1] + 1][player[0]] == 0 and [player[0], player[1] + 1] not in visited and (player[1] + 1) >= 0:
            return True
        elif player[2] == 3 and game_map[player[1]][player[0] - 1] == 0 and [player[0] - 1, player[1]] not in visited and (player[0] -1) >= 0:
            return True
        else:
            return False
    except:
        return False


def move():
    if player[2] == 0:
        player[1] -= 1
        visited.append([player[0], player[1]])
    elif player[2] == 1:
        player[0] += 1
        visited.append([player[0], player[1]])
    elif player[2] == 2:
        player[1] += 1
        visited.append([player[0], player[1]])
    elif player[2] == 3:
        player[0] -= 1
        visited.append([player[0], player[1]])


def mover():
    false_counter = 0
    move_counter = 1

    while false_counter < 4:
        if movable():
            move()
            move_counter += 1
            false_counter = 0
        else:
            false_counter += 1
            player[2] -= 1
            if player[2] == -1:
                player[2] = 3

    print(move_counter)


visited.append([player[0], player[1]])
mover()
