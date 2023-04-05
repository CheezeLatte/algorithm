#https://www.acmicpc.net/problem/14852

num = int(input())

d = [0] * 10001

for i in range(2, num + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
        
