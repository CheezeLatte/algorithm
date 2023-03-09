# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYaf9W8afyMDFAQ9&categoryId=AYaf9W8afyMDFAQ9&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&

cnt = int(input())
input_arr = [input() for _ in range(cnt)]

for t in range(cnt):
    target = int(input_arr[t])
    shortest_path = target * target
    i = 1
    while i * i <= target:
        if target % i == 0 and shortest_path > int(target/i + i - 2):
            shortest_path = int(target/i + i - 2)
        i = i + 1

    print('#'+str(t+1)+' '+str(shortest_path))

# 문제를 잘 읽을것
# General 케이스 속에서 최대한의 효율을 찾을것
