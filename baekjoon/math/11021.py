num = int(input())

for i in range(num):
    arr = list(map(int, input().split()))
    print('Case #{}: {}'.format(i + 1, arr[0] + arr[1]))
