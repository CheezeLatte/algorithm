n, k = map(int, input().split())

arr_1 = sorted(list(map(int, input().split())))
arr_2 = sorted(list(map(int, input().split())), reverse=True)

for i in range(k):
    if arr_1[i] < arr_2[i]:
        arr_1[i] = arr_2[i]
    else:
        break

print(sum(arr_1))
