import sys
input = sys.stdin.readline
from collections import deque
q = deque()

n= int(input().rstrip())

for i in range(n) :
  command = list(input().rstrip().split())
  
  if command[0] == "push_front" :
    q.appendleft(command[1])
  elif command[0] == "push_back" :
    q.append(command[1])
  elif command[0] == "pop_front" :
    if not q :
      print(-1) 
    else :
      print(q.popleft())
  elif command[0] == "pop_back" :
    #삼항 연산자 사용 -> 참인경우 값 if 조건 else 거짓인경우 값
    print(-1 if not q else q.pop())
    # if not q:
    #   print(-1) 
    # else :
    #   print(q.pop())
  elif command[0] == "size" :
    print(len(q))
  elif command[0] == "empty" :
    if not q :
      print(1) 
    else :
      print(0)
  elif command[0] == "front" :
    if q :
      print(q[0])
    else :
      print(-1)
  elif command[0] == "back" :
    if q :
      print(q[-1])
    else :
      print(-1)
