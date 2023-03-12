# https://www.acmicpc.net/problem/15649
# n과 M 1번
def insert(n, l):
    if len(array) < l:
        for i in range(1, n + 1):
            if i in array:
                continue
            array.append(i)
            insert(n, l)
            array.pop()
    else:
        print(' '.join(map(str, array)))


num, length = map(int, input().split())
array = []
insert(num, length)

#dfs를 잘쓰면 상당히 문제풀이가 쉬워진다는 철학을 배웠음