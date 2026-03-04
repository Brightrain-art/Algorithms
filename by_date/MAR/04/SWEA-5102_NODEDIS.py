# SWEA - 5102
# 노드의 거리

from collections import deque

# import sys
# sys.stdin = open('input.txt')


def bfs(start, end):
    global info, V, visited

    q = deque()
    q.append(start)


    while q:
        node = q.popleft()

        if node == end:
            print(f'#{test_case} {visited[node]}')
            return

        for nnode in info[node]:
            if visited[nnode] == 0:
                visited[nnode] = visited[node] + 1
                q.append(nnode)

    print(f"#{test_case} 0")

    pass

TC = int(input())
for test_case in range(1, TC+1):
    V, E = map(int, input().split())

    info = [[] for _ in range(V+1)]
    for _ in range(E):
        p, c = map(int, input().split())
        info[p].append(c)
        info[c].append(p)
    
    S, G = map(int, input().split())
    visited = [0] * (V+1)

    bfs(S, G)
