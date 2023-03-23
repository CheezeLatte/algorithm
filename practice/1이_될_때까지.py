n, k = map(int, input().split())


count = n % k

n = n - (n % k)

while n != 1:
    n = n / k
    count += 1

print(count)
