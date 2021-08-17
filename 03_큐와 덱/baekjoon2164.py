import sys
input = sys.stdin.readline

from collections import deque

n = int(input().rstrip())
q = deque([i for i in range(1,n+1)])

for i in range (n-1) :
  q.popleft()
  q.rotate(-1)

print(q[0])


