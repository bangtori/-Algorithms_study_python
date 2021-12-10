from collections import deque
import sys
input = sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]
t=int(input().rstrip())

def bfs(x, y) :
    q = deque()
    q.append((x,y))
    while q :
        x, y = q.popleft()
        matrix[y][x] = 0
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=m or ny<0 or ny>=n :
            continue
        if matrix[ny][nx] == 1 :
            q.popleft(nx,ny)
# def dfs(x, y) :
#     matrix[y][x] = 0
#     for i in range(4) :
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if nx<0 or nx>=m or ny<0 or ny>=n :
#             continue
#         if matrix[ny][nx] == 1 :
#             dfs(nx,ny)

for case in range(t) :
    cnt = 0
    m, n, k = map(int, input().rstrip().split())
    # 0 배열 초기화
    matrix = [[0]*m for _ in range(n)]
    # 배추 위치 입력 받기
    for _ in range(k) :
        x,y = map(int, input().rstrip().split())
        matrix[y][x] = 1
    # 탐색
    for i in range(n) :
        for j in range(m) :
            if matrix[i][j] == 1 :
                cnt+=1
                bfs(i,j)
    print(cnt)
