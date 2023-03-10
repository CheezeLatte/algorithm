# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYYAGjgqPgcDFARc
T = int(input())


def dfs(num):
    if num and int(num) > N or len(array) > max_len:
        return

    for i in range(10):
        if num == '' and i == 0:
            continue
        new_num = num + str(i)
        value = int(new_num)
        if value > N:
            continue
        array.append(new_num)
        dfs(new_num)


for test_case in range(1, T + 1):
    N = int(input())
    max_len = min(50, N)
    array = []
    dfs('')
    print("#" + str(test_case), end=" ")
    for i in range(max_len):
        print(array[i] + '.png', end=" ")
    print()

#2023.03.10
# dfs, bfs, 재귀 안하면 왜 깨지는지 보여주는 좋은 문제인 것 같음, 못 풀어서 다른분들 코드를 참고했다. 기본적인 알고리즘 상식들 먼저 하고 해야할듯.