from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input().rstrip())
graph = [[] for _ in range(n+1)]
for _ in range(n-1) :
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n+1)

def dfs(v) : 
    for i in graph[v] :
        if parent[v] != i :
            parent[i] = v
            dfs(i)
            

dfs(1)
for i in range(2,n+1) :
    print(parent[i])