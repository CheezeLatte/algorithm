# https://www.acmicpc.net/problem/15656
# n과 M 8번

def insert(n, m):
    if len(array) < m:
        for i in nums:
            if len(array) != 0 and i < array[-1]:
                continue
            array.append(i)
            insert(n, m)
            array.pop()
    else:
        print(' '.join(map(str, array)))


array = []
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
insert(n, m)

#7번 문제와 동일하지만 비내림차순이 적용되어야 한다
#4번 문제처럼 비내림차순으로 하면된다