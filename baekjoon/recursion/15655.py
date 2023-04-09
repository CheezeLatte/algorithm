# https://www.acmicpc.net/problem/15655
# n과 M 7번

def insert(n, m):
    if len(array) < m:
        for i in nums:
            array.append(i)
            insert(n, m)
            array.pop()
    else:
        print(' '.join(map(str, array)))


array = []
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
insert(n, m)

#6번 문제와 동일하지만 중복이 허용된다
#3번 문제처럼 중복을 허용해주면 된다