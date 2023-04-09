# https://www.acmicpc.net/problem/15650
# n과 M 2번

def printer():
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return
    print(' '.join(map(str, array)))


def insert(n, l):
    if len(array) < l:
        for i in range(1, n + 1):
            if i in array:
                continue
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

#1번 문제와 비슷하지만 오름차순으로 만들어야 하는 문제,
#처음 배열에 넣을때 오름차순으로 할 수 있고 아니면 프린트 할때 조건을 확인할 수도 있지만 시간복잡도를 따져봤을때 처음 배열에 넣을때 오름차순으로 하는게 훨씬 빠른 것 같다.