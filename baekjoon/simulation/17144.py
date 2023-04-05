# https://www.acmicpc.net/problem/17144

y, x, time = map(int, input().split())

array = []

pu_loc = []

for i in range(y):
    array.append(list(map(int, input().split())))
    if -1 in array[i]:
        pu_loc.append([1, i])


def spread():
    spreadable = []
    for t in range(y):
        for i in range(x):
            if array[t][i] > 4:
                spreadable_temp = []
                if i > 0 and array[t][i - 1] != -1:
                    spreadable_temp.append([t, i - 1])
                if i < x - 1 and array[t][i + 1] != -1:
                    spreadable_temp.append([t, i + 1])
                if t > 0 and array[t - 1][i] != -1:
                    spreadable_temp.append([t - 1, i])
                if t < y - 1 and array[t + 1][i] != -1:
                    spreadable_temp.append([t + 1, i])

                spread_dust = array[t][i] // 5

                array[t][i] = array[t][i] - (spread_dust * len(spreadable_temp))

                for temp in spreadable_temp:
                    temp.append(spread_dust)
                    spreadable.append(temp)

    for block in spreadable:
        array[block[0]][block[1]] += block[2]


def circulate_upper():
    array[pu_loc[0][1] - 1][0] = 0
    for yd in range(pu_loc[0][1] - 1, -1, -1):
        array[yd][0] = array[yd - 1][0]
    for xl in range(x - 1):
        array[0][xl] = array[0][xl + 1]
    for yu in range(pu_loc[0][1]):
        array[yu][x - 1] = array[yu + 1][x - 1]
    for xr in range(x - 1, 0, -1):
        array[pu_loc[0][1]][xr] = array[pu_loc[0][1]][xr - 1]
    array[pu_loc[0][1]][1] = 0


def circulate_lower():
    array[pu_loc[1][1] + 1][0] = 0
    for yu in range(pu_loc[1][1] + 1, y - 1):
        array[yu][0] = array[yu + 1][0]
    for xl in range(x - 1):
        array[y - 1][xl] = array[y - 1][xl + 1]
    for yd in range(y - 1, pu_loc[1][1], -1):
        array[yd][x - 1] = array[yd - 1][x - 1]
    for xr in range(x - 1, 0, -1):
        array[pu_loc[1][1]][xr] = array[pu_loc[1][1]][xr - 1]
    array[pu_loc[1][1]][1] = 0


for i in range(time):
    spread()
    circulate_upper()
    circulate_lower()

dust_sum = 0

for arr in array:
    dust_sum += sum(arr)

print(dust_sum + 2)

#구현은 정신력 싸움, 안되면 왜 안되는지, 뭘 잘못 적었는지 잘 생각해보자
