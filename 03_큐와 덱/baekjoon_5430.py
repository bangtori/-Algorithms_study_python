import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for i in range(t) :
  command = list(input().rstrip())
  n = int(input())
  x = input().rstrip()
  if x == "[]" :
    x = []
  else :
    x = deque(x[1:-1].split(","))

  error = False
  count = 0
  direction = True #True면 popleft / False면 pop
  for j in range(len(command)) :
    if command[j] == "R" : 
      direction = not direction
      count +=1
    elif command[j] == "D" :
      if not x :
        error = True
        break
      else :
        x.popleft() if direction else x.pop()
  if count % 2 != 0 : x.reverse()
  print("error" if error else "[" + ",".join(x) + "]") 
