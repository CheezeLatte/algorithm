def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
available_parts = sorted(list(map(int, input().split())))

target = int(input())
required_parts = list(map(int, input().split()))

for i in required_parts:
    results = binary_search(available_parts, i, 0, n-1)

    if results is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')