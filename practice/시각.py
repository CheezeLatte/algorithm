n = int(input())

count = 0
total = 0

for i in range(60):
    for k in range(60):
        if '3' in list(str(i) + str(k)):
            count += 1

for i in range(n + 1):
    if '3' in list(str(i)):
        total += 3600
    else:
        total += count

print(total)