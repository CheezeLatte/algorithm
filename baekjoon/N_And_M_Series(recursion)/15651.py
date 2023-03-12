# https://www.acmicpc.net/problem/15651
# n과 M 3번

def insert(n, l):
    if len(array) < l:
        for i in range(1, n + 1):
            array.append(i)
            insert(n, l)
            array.pop()
    else:
        print(' '.join(map(str, array)))


num, length = map(int, input().split())
array = []
insert(num, length)

#1번 문제와 비슷하지만 같은걸 여러번 넣어도 되는 문제
#이게 1번이었어야 하지 않을 정도로 재귀에 대해 명확하면서도 기초적인걸 알려주는 수준