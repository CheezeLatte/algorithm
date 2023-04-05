n = int(input())

routes = input().split()

x, y = 1, 1

for i in routes:
    if i == 'R' and i != n:
        x += 1
    if i == 'L' and i != 1:
        x -= 1 
    if i == 'D' and i != n:
        y += 1
    if i == 'U' and i != 1:
        y -= 1

print(x, y)
