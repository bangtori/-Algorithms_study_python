import sys
input = sys.stdin.readline
from collections import deque
q = deque()

n= int(input().rstrip())

for i in range(n) :
  inputs = list(input().rstrip().split())
  if len(inputs) == 1 :
    command = inputs[0]
  else :
    command = inputs[0]
    item = inputs[1]

  if command == "push" :
    q.append(item)
  elif command == "pop" :
    if len(q) == 0 :
      print(-1)
    else :
      print(q.popleft())
  elif command == "size" :
    print(len(q))
  elif command == "empty" :
    if len(q) == 0  :
      print(1)
    else :
      print(0)
  elif command == "front" :
    if len(q) == 0 :
      print(-1)
    else:
      print(q[0])
  elif command == "back" :
    if len(q) == 0 :
      print(-1) 
    else :
      print(q[len(q)-1])







