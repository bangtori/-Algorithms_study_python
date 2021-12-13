from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
l = [0]*100001
l[n] = 1
q = deque()
q.append(n)


def bfs() :
    while q :
        x= q.popleft()
        if x == k :
            return l[x]
        nx = [x-1, x+1, 2*x]

        for i in nx :
            if i < 0 or i > 100000 :
                continue
            if l[i] == 0 :
                q.append(i)
                l[i] = l[x]+1

print(bfs()-1)

            


