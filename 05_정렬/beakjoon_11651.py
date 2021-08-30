#11650번과 정렬 기준 x,y반대로
import sys
input = sys.stdin.readline

n= int(input().rstrip())
v = []
for i in range(n) :
  x, y = map(int, input().rstrip().split())
  v.append((x,y))

v.sort(key=lambda x:(x[1],x[0]))

for x,y in v :
  print(x,y)