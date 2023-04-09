# https://www.acmicpc.net/problem/17471

# from collections import deque
# import itertools
#
# n = int(input())
#
# populations = list(map(int, input().split()))
#
# connections = [list(map(int, input().split())) for _ in range(n)]
#
# visited = [False for _ in range(n)]
#
# least = int(1e9)
#
#
# def reachable(group):
#     cur_location = group[0]
#     visited = set(group[0])
#
#     q = deque([cur_location])
#
#     while q:
#         cur_location = q.popleft()
#
#         for u in connections[cur_location]:
#
#
#
#
# for i in range(1, n // 2 + 1):
#     groups = list(itertools.combinations(range(n), i))
#
#     for group in groups:
#
#         right, left = 0, 0
#
#         group_comp = [i for i in range(n) if i not in group]
#
#         if reachable(group_comp, group):
#             for i in range(len(group)):
#                 right += populations[group[i]]
#             for i in range(len(group_comp)):
#                 left += populations[group_comp[i]]
#
#             least = min(least, abs(right - left))
#
# print(least)

import sys, itertools, collections

def bfs(same):
    start = same[0]
    q = collections.deque([start])
    visited = set([start])
    _sum = 0
    while q:
        v = q.popleft()
        _sum += pp[v]
        for u in g[v]:
            if u not in visited and u in same:
                q.append(u)
                visited.add(u)
    return _sum, len(visited)

n = int(sys.stdin.readline().strip())
pp = [int(x) for x in sys.stdin.readline().split()]
g = collections.defaultdict(list)
result = float('inf')

for i in range(n):
    _input = [int(x) for x in sys.stdin.readline().split()]
    for j in range(1, _input[0]+1):
        g[i].append(_input[j]-1)

for i in range(1, n//2 + 1):
    combis = list(itertools.combinations(range(n), i))
    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([i for i in range(n) if i not in combi])
        if v1 + v2 == n: #2번의 bfs를 통해 모든 노드가 방문되었는지 확인한다.
            result = min(result, abs(sum1 - sum2))

if result != float('inf'):
    print(result)
else:
    print(-1)