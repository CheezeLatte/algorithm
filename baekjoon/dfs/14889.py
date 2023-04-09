# https://www.acmicpc.net/problem/14889

n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

visited = [False for _ in range(n + 1)]

minimum_diff = int(1e9)

def dfs(idx, level):
    global minimum_diff
    if n // 2 == level:
        team_1, team_2 = 0, 0
        for i in range(n):
            for k in range(n):
                if visited[i] and visited[k]:
                    team_1 += array[i][k]
                elif visited[i] is not True and visited[k] is not True:
                    team_2 += array[i][k]

        minimum_diff = min(minimum_diff, abs(team_1 - team_2))
        return

    for i in range(idx, n):
        if visited[i] is False:
            visited[i] = True
            dfs(i + 1, level + 1)
            visited[i] = False


dfs(0, 0)

print(minimum_diff)

# 전형적인 백트랙킹 문제인데 꼭 visited는 끝나고 나면 False를 해주고 탈출조건을 만들어주자, 재귀는 그거를 잘 해야한다.