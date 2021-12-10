from collections import deque
import sys
input = sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]
m, n = map(int, input().rstrip().split())
matrix=[list(map(int, input().rstrip().split())) for _ in range(n)]
q = deque()
result = 0


def bfs() :

    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            if matrix[nx][ny] == -1 :
                continue
            if matrix[nx][ny] == 0 :
                matrix[nx][ny] = matrix[x][y] + 1
                q.append((nx,ny))

for i in range(n) :
    for j in range(m) :
        if matrix[i][j] == 1 :
            q.append((i,j))
bfs()

for l in matrix :
    if 0 in l :
    # 안익은 토마토(0)이 1개 이상이라도 있다면 모두 익지 못함
        result = -1

if result != -1 :
    result = max(map(max, matrix))-1

print(result)

