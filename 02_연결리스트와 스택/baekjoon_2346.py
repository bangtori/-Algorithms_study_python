from collections import deque

n = int(input())
numbers = [(n, i+1) for i, n in enumerate(list(map(int, input().split())))]
q = deque(numbers)
result = []

while q :
  number, idx = q.popleft()
  result.append(idx)

  if number > 0 :
    q.rotate(-(number-1))
  elif number < 0 :
    q.rotate(-number)

for i in result :
  print(i, end=" ")
  


      
      
      