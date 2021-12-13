from collections import deque
import sys
input = sys.stdin.readline

t = int(input().rstrip())
red = 1
blue = -1

def bfs(start) :
    q = deque()
    q.append(start)
    if visited[start] == 0 :
        visited[start] = red
    while q :
        n = q.popleft()
        color = visited[n]
        # for i in range(1, v+1) :
        #     if graph[n][i] == 1 :
        #         if visited[i] == 0 :
        #             q.append(i)
        #             if color == red :
        #                 visited[i] = blue
        #             else :
        #                 visited[i] = red
        #         elif visited[i] == color:
        #             print("NO")
        #             return False

        for i in graph[n] :
            if visited[i] == 0 :
                q.append(i)
                if color == red :
                    visited[i] = blue
                else :
                    visited[i] = red
            elif visited[i] == color:
                print("NO")
                return False
    return True



        
for _ in range(t) :
    flag = 0
    v, e = map(int, input().rstrip().split())
    #graph = [[0]*(v+1) for _ in range(v+1)]
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    for i in range(e) :
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v+1) :
        if not bfs(i) :
            #False가 리턴되면
            flag = 1
            break

    if flag == 0  :
        print("YES")
    
