# https://www.acmicpc.net/problem/15652
# n과 M 4번

def insert(n, l):
    if len(array) < l:
        for i in range(1, n + 1):
            if len(array) != 0 and i < array[-1]:
                continue
            array.append(i)
            insert(n, l)
            array.pop()
    else:
        print(' '.join(map(str, array)))


num, length = map(int, input().split())
array = []
insert(num, length)

#2번 문제와 비슷하지만 같은걸 여러번 넣어도 되는 문제
#비내림차순이기에 넣을때 조건만 잘 살펴보면 된다