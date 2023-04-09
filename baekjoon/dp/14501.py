days = int(input())

works = [list(map(int, input().split())) for i in range(days)]

dp = [0 for i in range(days + 1)]

for i in range(days):
    for n in range(i + works[i][0], days + 1):
        if dp[n] < dp[i] + works[i][1]:
            dp[n] = dp[i] + works[i][1]

print(dp[-1])