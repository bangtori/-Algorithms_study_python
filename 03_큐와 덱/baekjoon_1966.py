import sys
input = sys.stdin.readline
# from queue import PriorityQueue
from collections import deque
t = int(input())

# for i in range(t) :
#   q = PriorityQueue()
#   n, m = map(int, input().rstrip().split())
#   priority = list(map(int, input().rstrip().split()))
#   for j in range(n) :
#     q.put((-priority[j], j))
#   count = 0
#   while q :
#     count +=1
#     if q.get()[1] == m :
#       break
#   print(count)
# 중요도가 낮으면 뒤로가는 연산이 실행되는 것이 아니라 우선 순위가 같은 경우 결과값이 다르게 나옴 

# 덱의 rotate함수를 통해 뒤로 넘기는 연산을 구현하고, 
# pop해야하는 원소를 선택하기 위해 max값과 비교한다.
for i in range(t) :
  n, m = map(int, input().rstrip().split())
  q = deque([(i, n) for i, n in enumerate(list(map(int, input().rstrip().split())))])
  count = 0
  while q :
    if q[0][1] != max(t[1] for t in q) :
      q.rotate(-1)
    else :
      count +=1
      if q.popleft()[0] ==  m:
        print(count)
        break

