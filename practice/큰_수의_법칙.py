size, count, limit = map(int, input().split())

array = sorted(map(int, input().split()), reverse=True)

# key, total = 0, 0
#
# for i in range(count):
#     if key < limit:
#         total += array[0]
#         key += 1
#     elif key == limit:
#         total += array[1]
#         key = 0
#
# print(total)

print(int(((count // (limit + 1)) * (array[0] * limit + array[1])) + (count % (limit + 1) * array[0])))

# 어려워 보이는 문제는 규칙을 찾고 해답을 거기에 맞추자. 위 문제처럼 내가 필요한 수열만 가져올 수 있어도 한줄로 코드를 짤 수 있다. for문은 필요도 없고, 이렇게 하면 for문 도는 시간을 획기적으로 아낄 수 있겠지