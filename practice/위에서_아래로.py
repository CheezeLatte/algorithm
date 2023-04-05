count = int(input())
array = []
for i in range(count):
    array.append(int(input()))

array.sort(reverse=True)

for t in array:
    print(t, end=' ')