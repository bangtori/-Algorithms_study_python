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
    x = deque(map(int, x[1:-1].split(",")))
  error = False
  for j in range(len(command)) :
    if command[j] == "R" : 
      x.reverse()
    elif command[j] == "D" :
      if not x :
        error = True
        break
      else :
        x.popleft()
  print("error" if error else list(x)) 
