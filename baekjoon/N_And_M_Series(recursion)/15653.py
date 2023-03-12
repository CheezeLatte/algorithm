# https://www.acmicpc.net/problem/15653
# n과 M 5번

def insert(n, m):
    if len(array) < m:
        for i in nums:
            if i in array:
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

#1번 문제와 동일하지만 직접 수열을 받아서 처리한다는 점에서 다르다
#처음에 수열을 받아서 미리 정렬 후 같은 형태로 돌리면 수월