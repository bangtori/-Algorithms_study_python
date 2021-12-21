import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) #노드 개수, 간선 개수
start = int(input()) #시작 노드 번호

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
distance = [INF] * (n+1)

#간선 정보 입력 받기
for _ in range(m) :
    a,b,c = map(int, input().split()) #a에서 b로 가는 비용이 c인 간선
    graph[a].append((b,c))

def dijkstra(start) :
    q = [] #우선 순위 큐
    heapq.heappush(q, (0,start)) #처음 정점까지의 거리는 0
    distance[start] = 0
    while q :
        dist, node = heapq.heappop(q)
        if visited[node] == 1 :
            #이미 방문 했다면 무시
            continue
        for i in graph[node] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        visited[node] = 1

dijkstra(start)

for i in range(1, n+1) :
    # 도달할 수 없는 경우, INFINITY출력
    if distance[i] == INF :
        print("INF")
    else : 
        print(distance[i])