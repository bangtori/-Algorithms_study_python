from collections import deque

n, k = list(map(int, input().split()))
numbers = [i for i in range(1, n+1)]
q = deque(numbers)
result = []
while q :
  q.rotate(-(k-1))
  result.append(q.popleft())

print("<"+", ".join(map(str, result))+">")