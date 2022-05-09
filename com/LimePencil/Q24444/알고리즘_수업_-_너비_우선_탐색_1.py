import sys
from collections import deque

def DFS(start):
    stack=deque()
    visited=[0]*(n+1)
    stack.append(start)
    cnt=1
    while stack:
        node=stack.popleft()
        if visited[node]!=0:
            continue
        visited[node]=cnt
        cnt+=1
        for new_node in graph[node]:
            if visited[new_node]==0:
                stack.append(new_node)
    return visited



input = sys.stdin.readline
n,m,r = list(map(int,input().split()))
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    graph[i].sort()
print(*DFS(r)[1:],sep="\n")