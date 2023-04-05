count = int(input())

array = []


def scores(array):
    return array[1]


for i in range(count):
    array.append(list(input().split()))

array.sort(key=scores, reverse=True)

for i in array:
    print(i[0], end=' ')