import sys
input = sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]
t=int(input().rstrip())


def dfs(x, y) :
    matrix[x][y] = 0
    for i in range(4) :
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=m or ny<0 or ny>=n :
            continue
        if matrix[nx][ny] == 1 :
            dfs(nx,ny)

for case in range(t) :
    cnt = 0
    m, n, k = map(int, input().rstrip().split())
    # 0 배열 초기화
    matrix = [[0]*n for _ in range(m)]
    # 배추 위치 입력 받기
    for _ in range(k) :
        a,b = map(int, input().rstrip().split())
        matrix[a][b] = 1
    # 탐색
    for i in range(m) :
        for j in range(n) :
            if matrix[i][j] == 1 :
                cnt+=1
                dfs(i,j)
    print(cnt)
