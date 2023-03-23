col, row = map(int, input().split())

# array = []

max = 0

# for i in range(col):
#     array.append(list(map(int, input().split())))
#
# for i in range(col):
#     if min(array[i]) > max:
#         max = min(array[i])
#
# print(max)

for i in range(col):
    array = list(map(int, input().split()))
    if min(array) > max:
        max = min(array)

print(max)

# 문제 해석에 시간이 좀 걸렸는데 조건만 잘 찾고나면 푸는데는 어렵지 않다. 그리고 후속에 필요하지 않은 데이터는 가지고 있지 말고 바로바로 버리자
