import sys
input = sys.stdin.readline

e = int(input().rstrip())
v = int(input().rstrip())
graph = [[0]*(e+1) for _ in range(e+1)]
visited = [0] *(e+1)

def dfs(node) :
    visited[node] = 1
    for i in range(1, e+1) :
        if visited[i]==0 and graph[node][i]==1 :
            dfs(i)

for _ in range(v) :
    a, b = map(int, input().rstrip().split())
    graph[a][b] = graph[b][a] = 1

dfs(1)
print(visited.count(1)-1)