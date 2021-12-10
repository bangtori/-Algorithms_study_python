from collections import deque
import sys
input = sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]
n, m = map(int, input().rstrip().split())
matrix=[list(input().rstrip()) for _ in range(n)]

def bfs(x, y) :
    q = deque()
    q.append((x,y))

    while q :
        x, y = q.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
        
            if matrix[nx][ny] == "1" :
                matrix[nx][ny] = int(matrix[x][y]) + 1
                q.append((nx,ny))
                
    return matrix[n-1][m-1]

print(bfs(0,0))