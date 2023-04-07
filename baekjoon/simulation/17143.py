# https://www.acmicpc.net/problem/17143

import sys

input = sys.stdin.readline

y, x, num = map(int, input().split())

sharks = []

fisherman_pos = 0
fishers_fish = 0

# x y speed direction size,
# 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽
# ex) 4 1 3 3 8

for i in range(num):
    sharks.append(list(map(int, input().split())))


def go_fisherman():
    global fisherman_pos
    global fishers_fish

    fisherman_pos += 1
    catchable = []
    ys = []

    for shark in sharks:
        if shark[1] == fisherman_pos:
            catchable.append(shark)

    if len(catchable) > 0:
        if len(catchable) == 1:
            fishers_fish += catchable[0][4]
            sharks.remove(catchable[0])
        else:
            for shark in catchable:
                ys.append(shark[0])

            for shark in catchable:
                if shark[0] == min(ys):
                    fishers_fish += shark[4]
                    sharks.remove(shark)


def move_sharks():
    for shark in sharks:

        temp_speed = shark[2]
        if shark[3] == 1 or shark[3] == 2:
            temp_speed %= (2 * y) - 2
        elif shark[3] == 3 or shark[3] == 4:
            temp_speed %= (2 * x) - 2

        for _ in range(temp_speed):
            if shark[3] == 1:
                if shark[0] == 1:
                    shark[3] = 2
                    shark[0] = 2
                else:
                    shark[0] -= 1

            elif shark[3] == 2:
                if shark[0] == y:
                    shark[3] = 1
                    shark[0] = y - 1
                else:
                    shark[0] += 1

            elif shark[3] == 3:
                if shark[1] == x:
                    shark[3] = 4
                    shark[1] = x - 1
                else:
                    shark[1] += 1

            elif shark[3] == 4:
                if shark[1] == 1:
                    shark[1] = 2
                    shark[3] = 3
                else:
                    shark[1] -= 1


def lets_eat():
    for prey in sharks:
        eatable = []
        sizes = []

        for predator in sharks:
            if prey[0] == predator[0] and prey[1] == predator[1] and prey[4] != predator[4]:
                if prey not in eatable:
                    eatable.append(prey)
                if predator not in eatable:
                    eatable.append(predator)

        if len(eatable) > 1:
            for competitor in eatable:
                sizes.append(competitor[4])

            max_size = max(sizes)

            for shark in eatable:
                if shark[4] != max_size:
                    sharks.remove(shark)


for i in range(x):
    go_fisherman()
    move_sharks()
    lets_eat()

print(fishers_fish)
