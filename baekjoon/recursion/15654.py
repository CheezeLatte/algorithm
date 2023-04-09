# https://www.acmicpc.net/problem/15654
# n과 M 6번

def insert(n, m):
    if len(array) < m:
        for i in nums:
            if i in array or (len(array) != 0 and array[-1] > i):
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

#5번 문제와 동일하지만 오름차순을 적용해야 한다
#2번 처럼 오름차순인지 검사해서 넣으면 된다