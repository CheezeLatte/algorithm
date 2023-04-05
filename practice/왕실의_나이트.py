initial_position = list(input())

array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
count = 0
possiblities = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

for i in array:
    if initial_position[0] == i:
        initial_position[0] = int(count + 1)
    count += 1

movable = 0

for i in possiblities:
    if int(initial_position[0]) + int(i[0]) > 0 and int(initial_position[1]) + int(i[1]) > 0:
        movable += 1

print(movable)


#구현에 집중, 기교 부리기 보단 뭐든 최대한 빠리빨리 해서 만들기