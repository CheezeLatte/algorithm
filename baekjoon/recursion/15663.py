# https://www.acmicpc.net/problem/15663
# n과 M 9번

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
strings = []
n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
insert(n, m)

#5번 문제와 동일하지만 받는 배열에 중복 문자가 있을 수 있으니 제거해야한다
#가장 쉬운 방법은 역시 set인 것 같다 정렬도 자동으로 해준다는데 파이썬 버전이 안맞는건지 그건 안되는 것 같고...