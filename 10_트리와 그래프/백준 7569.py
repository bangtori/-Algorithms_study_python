from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

m, n, h = map(int, input().rstrip().split())
matrix = [[list(map(int, input().rstrip().split())) for _ in range(n)] for _ in range(h)]

q = deque()
result = 0

def bfs() :

    while q :
        x, y, z = q.popleft()
        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h :
                continue
            if matrix[nz][nx][ny] == -1 :
                continue
            if matrix[nz][nx][ny] == 0 :
                matrix[nz][nx][ny] = matrix[z][x][y] + 1
                q.append((nx,ny,nz))

for z in range(h) :
    for i in range(n) :
        for j in range(m) :
            if matrix[z][i][j] == 1 :
                q.append((i,j,z))
bfs()
for l2 in matrix :
    for l in l2 :
        if 0 in l :
            print(-1)
            sys.exit()

if result != -1 :
    for i in matrix :
        for j in i :
            list_max = max(j)
            result = max(result, list_max)

print(result - 1)